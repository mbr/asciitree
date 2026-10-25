#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
build_dir=$(mktemp -d)
trap 'rm -rf "$build_dir"' EXIT

curl -fL --retry 3 https://github.com/proot-me/proot/archive/refs/tags/v5.4.0.tar.gz -o "$build_dir/proot.tar.gz"
echo "29248aac2a7ce10c3bd5ee5602742ec33b2532310ff9cf73b79f3c133e5a5f68  $build_dir/proot.tar.gz" | sha256sum --check
tar -xzf "$build_dir/proot.tar.gz" -C "$build_dir"
source_dir="$build_dir/proot-5.4.0"
patch --batch --fuzz=0 -d "$source_dir" -p1 <docs/proot-fchmodat2.patch

# RTD may have SWIG installed; the optional Python extension is not needed.
make -C "$source_dir/src" HAS_SWIG= HAS_PYTHON_CONFIG= VERSION=5.4.0-fchmodat2 loader.elf loader-m32.elf build.h
make -C "$source_dir/src" -j2 HAS_SWIG= HAS_PYTHON_CONFIG= VERSION=5.4.0-fchmodat2 proot
install -m 755 "$source_dir/src/proot" "$HOME/proot"
