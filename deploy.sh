#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi

apt-get update
apt-get -y install python3 sqlite3

BASEDIR="/local/driftinfo"
venv="${BASEDIR}/venv"
mkdir -p "${BASEDIR}/db"
sqlite3 "${BASEDIR}/db/driftinfo.db" "$(cat conf/table.sql)"
if [[ ! -d "${venv}" ]]; then
    python3 -m venv "${venv}"
    source "${venv}/bin/activate"
    pip install --upgrade pip
    pip install flask
    pip install flask_sqlalchemy
    pip install pyyaml
    pip install sqlalchemy
    
fi
cp -a app ${venv}
cp -a conf ${BASEDIR}
export FLASK_APP=${venv}/app/main.py
flask run
