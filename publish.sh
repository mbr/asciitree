#!/bin/sh
set -eu

cd "$(dirname "$0")"
nix flake check -L

dist_dir=$(mktemp -d)
trap 'rm -rf "$dist_dir"' EXIT

pyproject-build --no-isolation --outdir "$dist_dir"
twine check --strict "$dist_dir"/*
twine upload "$dist_dir"/*
