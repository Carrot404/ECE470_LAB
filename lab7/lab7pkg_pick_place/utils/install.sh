#!/bin/sh

if [ -d /etc/udev/rules.d/];then
    cp 90-ckusb.rules /etc/udev/rules.d/
fi
