#!/bin/sh
set -eu

mkdir -p "$HOME/.config/nix" "$HOME/.local/share/nix"
cat >"$HOME/.config/nix/nix.conf" <<'EOF'
experimental-features = nix-command flakes
store = local
build-users-group =
sandbox = false
EOF

cat >"$HOME/proot-env" <<'EOF'
#!/bin/sh
exec "$HOME/proot" -b "$HOME/.local/share/nix:/nix" "$@"
EOF
chmod +x "$HOME/proot-env"
