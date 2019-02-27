#!/usr/bin/env bash
BASEDIR="/local/driftinfo"
venv="${BASEDIR}/venv"
source "${venv}/bin/activate"
export FLASK_APP=${venv}/app/main.py
flask run >> /local/driftinfo/logs/driftinfo.log 2>&1 &
