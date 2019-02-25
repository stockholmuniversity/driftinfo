#!/usr/bin/env bash
pidfile="/local/driftinfo/driftinfo.pid"
if [[ -f ${pidfile} ]]; then
    PID=$(cat ${pidfile})
    kill ${PID}
    if [[ "${?}" == "0" ]]; then
        rm ${pidfile}
        exit 0
    else
        echo "Could not kill process with pid: ${PID}"
        exit 1
    fi
fi
echo "${pidfile} not found, trying pkill flask"
pkill flask
