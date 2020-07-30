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
petalinux-build
