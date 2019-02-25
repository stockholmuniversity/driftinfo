#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi
HOST=$(hostname --fqdn)
apt-get update
apt-get -y install python3 python3-venv sqlite3 apache2 certbot python-certbot-apache 
a2enmod proxy proxy_http
systemctl restart apache2

BASEDIR="/local/driftinfo"
venv="${BASEDIR}/venv"
mkdir -p ${BASEDIR}/{db,logs}
sqlite3 "${BASEDIR}/db/driftinfo.db" "$(cat conf/table.sql)"
if [[ ! -d "${venv}" ]]; then
    python3 -m venv "${venv}"
    source "${venv}/bin/activate"
    pip install --upgrade pip
    pip install flask
    pip install flask_sqlalchemy
    pip install pyyaml
    pip install sqlalchemy
else
    source "${venv}/bin/activate"
    pip install --upgrade flask
    pip install --upgrade flask_sqlalchemy
    pip install --upgrade pyyaml
    pip install --upgrade sqlalchemy
    
fi
cp -a app ${venv}
cp -a assets ${BASEDIR}
cp -a bin ${BASEDIR}
cp -a conf ${BASEDIR}
sed 's/%%HOST%%/'${HOST}'/g' ${BASEDIR}/conf/apache.conf.in > /etc/apache2/sites-enabled/000-default-le-ssl.conf 
certbot --apache -d ${HOST} --non-interactive --agree-tos --email 'sunet-scs@su.se'
