#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
build_dir=$(mktemp -d)

source_dir="$build_dir/proot"
git clone --depth=1 --revision=25dc6a3134891f98a79f57ce1c2c1b23ff15cad1 \
  https://github.com/proot-me/proot.git "$source_dir"

make -C "$source_dir/src" WITHOUT_PYTHON=1 VERSION=5.5.0 loader.elf loader-m32.elf build.h
make -C "$source_dir/src" -j2 WITHOUT_PYTHON=1 VERSION=5.5.0 proot
install -m 755 "$source_dir/src/proot" "$HOME/proot"
