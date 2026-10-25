#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
build_dir=$(mktemp -d)
trap 'rm -rf "$build_dir"' EXIT

curl -fL --retry 3 https://github.com/proot-me/proot/archive/refs/tags/v5.5.0.tar.gz -o "$build_dir/proot.tar.gz"
echo "287cfb27f58e100b0153006cb352268225bb9ad9d41d9b52ed56d01a22c13e6f  $build_dir/proot.tar.gz" | sha256sum --check
tar -xzf "$build_dir/proot.tar.gz" -C "$build_dir"
source_dir="$build_dir/proot-5.5.0"

# RTD may have SWIG installed; the optional Python extension is not needed.
make -C "$source_dir/src" HAS_SWIG= HAS_PYTHON_CONFIG= VERSION=5.5.0 loader.elf loader-m32.elf build.h
make -C "$source_dir/src" -j2 HAS_SWIG= HAS_PYTHON_CONFIG= VERSION=5.5.0 proot
install -m 755 "$source_dir/src/proot" "$HOME/proot"
