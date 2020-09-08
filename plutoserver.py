def setup_plutoserver():
  return {
    "command": ["julia", "-e", "import Pluto; Pluto.run(\"0.0.0.0\", {port}; security=Pluto.ServerSecurity(false))"],
    "timeout": 60,
    "launcher_entry": {
        "title": "Pluto.jl",
    },
  }