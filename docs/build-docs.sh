#!/bin/sh
set -eu

mkdir -p "$READTHEDOCS_OUTPUT/html"
nix build "^doc" -L
cp -R result-doc/share/doc/*/html/. "$READTHEDOCS_OUTPUT/html/"
