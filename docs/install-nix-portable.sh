#!/bin/sh
set -eu

curl -fL --retry 3 https://github.com/DavHau/nix-portable/releases/download/v012/nix-portable-x86_64 -o "$HOME/nix-portable"
echo "b409c55904c909ac3aeda3fb1253319f86a89ddd1ba31a5dec33d4a06414c72a  $HOME/nix-portable" | sha256sum --check
chmod +x "$HOME/nix-portable"

cat >"$HOME/nix" <<'EOF'
#!/bin/sh
export NP_RUNTIME=proot NP_PROOT="$HOME/proot" NP_GIT=/usr/bin/git
exec "$HOME/nix-portable" nix "$@"
EOF
chmod +x "$HOME/nix"
