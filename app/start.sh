#!/bin/bash

#Set the root password as resin device UUID if not set as an ENV variable
export PASSWD=${PASSWD:=$RESIN_DEVICE_UUID}

echo $PASSWD
#Set the root password
echo "root:$PASSWD" | chpasswd

#Spawn dropbear
dropbear -E -F
