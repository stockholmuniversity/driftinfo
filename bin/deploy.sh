#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi
mydir=$(pwd)
tempdir=$(mktemp -d)
cd ${tempdir}
HOST=$(hostname --fqdn)
apt-get update
apt-get -y install python3 python3-venv sqlite3 apache2 certbot python-certbot-apache git
a2enmod proxy proxy_http
systemctl restart apache2

BASEDIR="/local/driftinfo"
venv="${BASEDIR}/venv"
noclobber="${BASEDIR}/conf/config_file.yml ${BASEDIR}/conf/.htpasswd ${BASEDIR}/db/driftinfo.db"
mkdir -p ${BASEDIR}/{db,logs}
if [[ ! -d "${venv}" ]]; then
    python3 -m venv "${venv}"
    source "${venv}/bin/activate"
    pip install --upgrade pip
    pip install flask
    pip install flask_sqlalchemy
    pip install pyyaml
    pip install sqlalchemy
    pip install python-twitter
else
    source "${venv}/bin/activate"
    pip install --upgrade flask
    pip install --upgrade flask_sqlalchemy
    pip install --upgrade pyyaml
    pip install --upgrade sqlalchemy
    pip install --upgrade python-twitter
    
fi
mkdir saved
for i in ${noclobber}; do
    if [[ -f ${i} ]]; then
        short="saved/$(echo ${i} | sed 's_.*/__')"
        cp ${i} ${short}
    fi
done
git clone https://github.com/stockholmuniversity/driftinfo.git
cd driftinfo
cp -a app ${venv}
cp -a assets ${BASEDIR}
cp -a bin ${BASEDIR}
cp -a conf ${BASEDIR}
cp -a plugins ${venv}
cp ${BASEDIR}/conf/driftinfocronjobs /etc/cron.d/
cp ${BASEDIR}/conf/driftinfo.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable driftinfo.service
sqlite3 "${BASEDIR}/db/driftinfo.db" "$(cat conf/table.sql)"
cd ..
certbot --apache -d ${HOST} --non-interactive --agree-tos --email 'sunet-scs@su.se'
sed 's/%%HOST%%/'${HOST}'/g' ${BASEDIR}/conf/apache.conf.in > /etc/apache2/sites-enabled/000-default-le-ssl.conf 
chown -R www-data:www-data ${BASEDIR}/assets
chown -R nobody:root ${BASEDIR}/db/
chown -R nobody:root ${BASEDIR}/logs/
for i in ${noclobber}; do
    if [[ -f ${i} ]]; then
        short="saved/$(echo ${i} | sed 's_.*/__')"
        cp ${short} ${i}
    fi
done
cd "${mydir}"
rm -r "${tempdir}"
if [[ ! -f ${BASEDIR}/conf/.htpasswd ]]; then
    touch "${BASEDIR}/conf/.htpasswd"
fi
systemctl restart apache2
