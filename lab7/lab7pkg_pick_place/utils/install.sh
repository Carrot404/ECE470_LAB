#!/bin/sh
if [ -d /etc/udev/rules.d/ ];then
    sudo cp 90-ckusb.rules /etc/udev/rules.d/
fi

if [ -d /usr/local/lib/ ];then
    sudo cp ./lib/x64/libCKCameraSDK.so /usr/local/lib/
fi
