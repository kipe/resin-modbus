#!/bin/bash
# Set the root password as resin device UUID if not set as an ENV variable
export PASSWD=${PASSWD:=$RESIN_DEVICE_UUID}
echo "root:$PASSWD" | chpasswd
dropbear -E

/usr/bin/env python /app/app.py

while [[ true ]]; do
    echo "Crashed, just sleeping...."
    sleep 60
done
