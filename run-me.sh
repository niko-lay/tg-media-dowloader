#!/usr/bin/env bash

set -e

BASEDIR=$(realpath $(dirname $0))
cd $BASEDIR
source ./PyVenv/bin/activate && python3 downloader.py
# source ./PyVenv/bin/activate && python3
