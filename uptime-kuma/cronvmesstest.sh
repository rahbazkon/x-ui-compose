#!/bin/bash

vmess="$1"
uptime_kuma_base_api_url="$2"
ping_count=10
ping_delay=5
api_interval=900
down_message="NotOK"
up_message="OK"

avg_ping_time=$(./vmessping_amd64_linux -c $ping_count -i $ping_delay $vmess | grep "rtt min/avg/max" | awk -F '/' '{print $4}')

if [ $avg_ping_time -eq 0 ]
then
  curl "$uptime_kuma_base_api_url?status=down&msg=$down_message"
else
  curl "$uptime_kuma_base_api_url?status=up&msg=$up_message&ping=$avg_ping_time"
fi
echo ""
sleep $api_interval   # Add delay between iterations