#/bin/bash

export MDEXPORTER_HOME=/cygdrive/h/tmp/md-exporter

cd $MDEXPORTER_HOME/bin

./md-exporter --rdb ../../../Dev/projects/vnavigator-content/VNAVIGATOR-RDB --out ../../../UPDATES/export-2

