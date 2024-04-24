#!/bin/sh
nginx
while true
do
 ls /etc/reload/need_reload 2>/dev/null && nginx -t && nginx -s reload && rm -rf /etc/reload/need_reload
 sleep 1
done
