import os

def setup_plutoserver():
  mydir = os.path.dirname(os.path.realpath(__file__))
  iconpath = os.path.join(mydir, 'icons', 'pluto-logo.svg')
  return {
    "command": ["julia", "-e", "import Pluto; Pluto.run(\"0.0.0.0\", {port}, configuration=Pluto.ServerConfiguration(launch_browser=false), security=Pluto.ServerSecurity(false))"],
    "timeout": 60,
    "launcher_entry": {
        "title": "Pluto.jl",
        "icon_path": iconpath
    },
  }
