#!/bin/bash
set -e

case $1 in
    supervisor)
        /usr/bin/supervisord -n -c supervisor-app.conf
    ;;
    celery)
        export QUEUE_NAME=$3
        celery worker -A ureport -Q sync,celery --workdir=/app/ -l INFO --autoscale=12,1
    ;;
esac

exec "$@"