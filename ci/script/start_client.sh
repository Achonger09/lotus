#! /bin/bash

CURRENTPATH=$(cd "$(dirname "$0")"; pwd)

sleep 5s
cd ${CURRENTPATH}/../../src/test/
python start_client.py > ./client.log 2>&1
sleep 10s
