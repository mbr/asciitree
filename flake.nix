{
  description = "Draws ASCII trees";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    flake-utils.url = "github:numtide/flake-utils";
    treefmt-nix.url = "github:numtide/treefmt-nix";
    treefmt-nix.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      treefmt-nix,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python3;
        pyproject = builtins.fromTOML (builtins.readFile ./pyproject.toml);
        treefmt = treefmt-nix.lib.evalModule pkgs {
          projectRootFile = "flake.nix";
          programs = {
            black.enable = true;
            nixfmt.enable = true;
            mdformat.enable = true;
            taplo.enable = true;
            shfmt.enable = true;
          };
        };
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
            myst-parser
            furo
          ];
          nativeCheckInputs = [ python.pkgs.pytestCheckHook ];
          pythonImportsCheck = [ "asciitree" ];
        };

        formatter = treefmt.config.build.wrapper;
        checks.formatting = treefmt.config.build.check self;

        devShells.default = pkgs.mkShell {
          inputsFrom = [ self.packages.${system}.default ];
          packages = [ treefmt.config.build.wrapper ];
        };
      }
    );
}
