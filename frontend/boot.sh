#!/bin/sh

echo "window.settings ={backendUrl: '$BACKEND_URL'};" > /usr/share/nginx/html/env.js
sed "s/\$PORT/${PORT}/g" < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"
