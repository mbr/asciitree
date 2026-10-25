{
  description = "Draws ASCII trees";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python3;
        pyproject = builtins.fromTOML (builtins.readFile ./pyproject.toml);
        docsPackages = with python.pkgs; [
          sphinx
          furo
        ];
        docs =
          pkgs.runCommand "${pyproject.project.name}-docs-${pyproject.project.version}"
            {
              src = ./.;
              nativeBuildInputs = [ (python.withPackages (_: docsPackages)) ];
            }
            ''
              cd "$src"
              export PYTHONPATH="$PWD"
              sphinx-build -W --keep-going -b html -d "$TMPDIR/doctrees" docs "$out"
            '';
      in
      {
        packages.default = python.pkgs.buildPythonPackage {
          pname = pyproject.project.name;
          version = pyproject.project.version;
          src = ./.;
          pyproject = true;

          build-system = [ python.pkgs.setuptools ];
          nativeCheckInputs = [ python.pkgs.pytestCheckHook ];
          pythonImportsCheck = [ "asciitree" ];
        };

        packages.docs = docs;
        checks.docs = docs;

        devShells.default = pkgs.mkShell {
          packages = [ (python.withPackages (ps: [ ps.pytest ] ++ docsPackages)) ];
        };
      }
    );
}
