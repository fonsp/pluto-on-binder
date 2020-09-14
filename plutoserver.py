def setup_plutoserver():
  return {
    "command": ["julia", "-e", "import Pluto; Pluto.run(host=\"0.0.0.0\", port={port}, launch_browser=false, require_token_for_open_links=false)"],
    "timeout": 60,
    "launcher_entry": {
        "title": "Pluto.jl",
    },
  }