#!/bin/bash

# cape_enable=capemgr.enable_partno=BB-UART4
# echo BB-UART4 > /sys/devices/platform/bone_capemgr/slots

# Start dropbear, if running on resin.io
if [ -z "$RESIN_DEVICE_UUID" ]; then
    # Set the root password as resin device UUID if not set as an ENV variable
    export PASSWD=${PASSWD:=$RESIN_DEVICE_UUID}
    echo "root:$PASSWD" | chpasswd
    dropbear -E
fi


while [[ true ]]; do
    /usr/bin/env python /app/app.py
    echo "Crashed, sleeping for 1 minute...."
    sleep 60
done
