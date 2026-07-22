{
  description = "A flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-26.05";
    nixpkgs-unstable.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      nixpkgs,
      nixpkgs-unstable,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
        unstable = import nixpkgs-unstable {
          inherit system;
          config.allowUnfree = true;
        };

        xits-font = pkgs.stdenv.mkDerivation {
          pname = "xits-font";
          version = pkgs.texlivePackages.xits.version;

          src = pkgs.texlivePackages.xits;
          dontUnpack = true;
          dontBuild = true;

          installPhase = ''
            runHook preInstall
            mkdir -p $out/share/fonts/opentype
            find $src -name "*.otf" -exec cp {} $out/share/fonts/opentype/ \;
            runHook postInstall
          '';
        };

        fonts =
          with pkgs;
          [
            stix-two
            xits-math
            cm_unicode
            lato
          ]
          ++ [ xits-font ];
      in
      {
        devShells.default = pkgs.mkShell {
          LD_LIBRARY_PATH =
            with pkgs;
            lib.makeLibraryPath [
              stdenv.cc.cc
              zlib
              glib
              libxcb
              libglvnd
            ];

          packages = pkgs.lib.flatten [
            (with pkgs; [
              fontconfig
              bun
              uv
            ])
            fonts
            (with unstable; [
              typst
              tinymist
              typstyle
            ])
          ];

          buildInputs = [ pkgs.bashInteractive ];

          shellHook = ''
            unset SOURCE_DATE_EPOCH
          '';

          env = {
            FONTCONFIG_FILE = pkgs.makeFontsConf {
              fontDirectories = fonts;
            };
          };
        };
      }
    );
}
