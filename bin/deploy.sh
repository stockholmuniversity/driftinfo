#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi

apt-get update
apt-get -y install python3 sqlite3 apache2 certbot python-certbot-apache -t stretch-backports
certbot --apache

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
cp -a bin ${BASEDIR}
cp -a conf ${BASEDIR}
