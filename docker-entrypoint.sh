#!/bin/bash

set -e

APP_CELERY_INIT="ureport"

if [[ "start" == "$1" ]]; then
    echo "Starting Gunicorn..."
    exec gosu "${APP_UID}:${APP_GID}" gunicorn ureport.wsgi:application \
        --max-requests 5000 \
        --bind "0.0.0.0:${APP_PORT}" \
        --capture-output \
        --error-logfile - \
        -c $PROJECT_PATH/gunicorn.conf.py
elif [[ "celery-worker" == "$1" ]]; then
    echo "Starting Celery Worker..."
    exec gosu "${APP_UID}:${APP_GID}" celery -A "${APP_CELERY_INIT}" worker --loglevel=INFO -E
elif [[ "celery-beat" == "$1" ]]; then
    echo "Starting Celery Beat..."
    exec gosu "${APP_UID}:${APP_GID}" celery -A "${APP_CELERY_INIT}" beat --loglevel=INFO
elif [[ "healthcheck-celery-worker" == "$1" ]]; then
    HEALTHCHECK_OUT=$( gosu "${APP_UID}:${APP_GID}" celery -A "${APP_CELERY_INIT}" inspect ping -d "celery@${HOSTNAME}" 2>&1 )
    echo "${HEALTHCHECK_OUT}"
    fgrep -qs "celery@${HOSTNAME}: OK" <<<"${HEALTHCHECK_OUT}" || exit 1
    exit 0
elif [[ "healthcheck-http-get" == "$1" ]]; then
    gosu "${APP_UID}:${APP_GID}" curl -SsLf "${2}" -o /tmp/null --connect-timeout 3 --max-time 20 \
        -w "%{http_code} %{http_version} %{response_code} %{time_total}\n" || exit 1
    exit 0
elif [[ "healthcheck" == "$1" ]]; then
    gosu "${APP_UID}:${APP_GID}" curl -SsLf "http://127.0.0.1:${APP_PORT}/" -o /tmp/null --connect-timeout 3 --max-time 20 \
        -w "%{http_code} %{http_version} %{response_code} %{time_total}\n" || exit 1
    exit 0
fi

exec "$@"
