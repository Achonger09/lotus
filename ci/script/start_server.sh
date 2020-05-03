#! /bin/bash

CURRENTPATH=$(cd "$(dirname "$0")"; pwd)

cd ${CURRENTPATH}/../../src/test/
python start_server.py > ./server.log
sleep 10s
