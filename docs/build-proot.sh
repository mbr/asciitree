#!/bin/sh
# This script builds PRoot 5.5.0, which fixes `fchmodat2` handling:
# https://github.com/proot-me/proot/issues/387
# Required apt packages: `build-essential`, `pkg-config`, `libtalloc-dev`,
# `git`, and `ca-certificates`.
set -eu

cd "$(dirname "$0")/.."
build_dir=$(mktemp -d)

source_dir="$build_dir/proot"
git clone --depth=1 --revision=25dc6a3134891f98a79f57ce1c2c1b23ff15cad1 \
  https://github.com/proot-me/proot.git "$source_dir"

make -C "$source_dir/src" WITHOUT_PYTHON=1 VERSION=5.5.0 loader.elf loader-m32.elf build.h
make -C "$source_dir/src" -j2 WITHOUT_PYTHON=1 VERSION=5.5.0 proot
install -m 755 "$source_dir/src/proot" "$HOME/proot"
