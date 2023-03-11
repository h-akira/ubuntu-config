#!/bin/sh
#
# Created:      2023-03-11 23:44:23
set -eu

if [ -n "$(ps -C dropbox -o pid --no-heading)" ]; then
  # ~/.dropbox-dist/dropboxd
  echo "Dropbox: ON"
else
  echo "Dropbox: OFF"
fi
