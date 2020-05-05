#!/bin/sh

sed "s/\$PORT/${PORT}/g" < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"
