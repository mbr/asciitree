{
  description = "Draws ASCII trees";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
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
      in
      {
        packages.default = python.pkgs.buildPythonPackage {
          pname = pyproject.project.name;
          version = pyproject.project.version;
          src = ./.;
          pyproject = true;
          outputs = [
            "out"
            "doc"
          ];

          build-system = [ python.pkgs.setuptools ];
          nativeBuildInputs = with python.pkgs; [
            sphinxHook
            furo
          ];
          nativeCheckInputs = [ python.pkgs.pytestCheckHook ];
          pythonImportsCheck = [ "asciitree" ];
        };

        devShells.default = pkgs.mkShell {
          inputsFrom = [ self.packages.${system}.default ];
        };
      }
    );
}
