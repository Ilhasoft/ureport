#!/bin/bash
set -e

case $1 in
    supervisor)
        /usr/bin/supervisord -n -c supervisor-app.conf
    ;;
    celery)
        case $2 in
            beat)
                /usr/bin/supervisord -n -c celery/celery-beat.conf
            ;;
        esac
    /usr/bin/supervisord -n -c celery/celery-$6.conf
    ;;
esac

exec "$@"
