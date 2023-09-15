#!/bin/sh
# Dropboxを起動
if [ -z "$(ps -C dropbox -o pid --no-heading)" ] || [ -e ~/.dropbox-dist/dropboxd ]; then
  ~/.dropbox-dist/dropboxd
fi
