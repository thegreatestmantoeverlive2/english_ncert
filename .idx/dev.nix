# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.novnc
    pkgs.tigervnc # Provides the vncserver command
    pkgs.xorg.xinit # Provides a basic X server environment
    pkgs.xterm
    pkgs.fluxbox
    pkgs.inetutils # Provides the 'hostname' command
  ];
  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "google.gemini-cli-vscode-ide-companion"
    ];
    # Enable previews
    previews = {
      enable = true;
      previews = {
        vnc = {
          # The command to run for this preview.
          # We wrap this in `sh -c` to allow for shell features like output redirection (`&>`)
          # and command chaining (`&&`).
          command = [ "sh" "-c" "vncserver -listen tcp -xstartup fluxbox &> /tmp/vnc.log && novnc -v -L --listen $PORT --vnc localhost:5901" ];
          manager = "web";
        };
      };
    };
    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ ".idx/dev.nix" "README.md" ];
      };
      # Runs when the workspace is (re)started
      onStart = {
      };
    };
  };
}
