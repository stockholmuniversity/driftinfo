#!/usr/bin/env bash

BASEDIR="/local/driftinfo"
venv="${BASEDIR}/venv"
mkdir -p "${BASEDIR}/db"
sqlite3 "${BASEDIR}/db/driftinfo.db" "$(cat conf/table.sql)"
if [[ ! -d "${venv}" ]]; then
    apt-get update
    apt-get -y install python3 sqlite3

    python3 -m venv "${venv}"
    source "${venv}/bin/activate"
    pip install flask
fi
cp -a app ${BASEDIR}
