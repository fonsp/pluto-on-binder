def setup_plutoserver():
  return {
    "command": ["julia", "--optimize=0", "-e", "import Pluto; Pluto.run(host=\"0.0.0.0\", port={port}, pkgimages=\"no\", workspace_use_distributed_stdlib=false, launch_browser=false, require_secret_for_open_links=false, require_secret_for_access=false, warn_about_untrusted_code=false, dismiss_update_notification=true, show_file_system=false)"],
    "timeout": 60,
    "launcher_entry": {
        "title": "Pluto.jl",
    },
  }
