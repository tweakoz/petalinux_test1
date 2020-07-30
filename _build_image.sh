#!/usr/bin/env sh

rm -rf /tmp/pluxbuild
mkdir /tmp/pluxbuild
cd /tmp/pluxbuild

petalinux-create \
 --type project \
 --template zynqMP \
 --name PLUX

cd PLUX
petalinux-config --get-hw-description=/data/hardware
cat /data/local.conf >> /tmp/pluxbuild/PLUX/build/conf/local.conf
petalinux-build
