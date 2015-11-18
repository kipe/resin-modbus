#!/bin/bash

echo BB-UART4 > /sys/devices/platform/bone_capemgr/slots

# Start dropbear, if running on resin.io
if [ -z "$RESIN_DEVICE_UUID" ]; then
    # Set the root password as resin device UUID if not set as an ENV variable
    export PASSWD=${PASSWD:=$RESIN_DEVICE_UUID}
    echo "root:$PASSWD" | chpasswd
    dropbear -E
fi

/usr/bin/env python /app/app.py

while [[ true ]]; do
    echo "Crashed, just sleeping...."
    sleep 60
done
