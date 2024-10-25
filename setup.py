import setuptools

setuptools.setup(
  name="jupyter-pluto-proxy",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['plutoserver'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'pluto = plutoserver:setup_plutoserver',
      ]
  },
  install_requires=['jupyter-server-proxy @ git+http://github.com/fonsp/jupyter-server-proxy@470e13ae0f7a8961202c76ea6bcbcfd27ed07e6a'],
)

# Start Pluto, open new notebook, shut down notebook.
# This should precompile the PlutoRunner boot environment.
import os
os.system('julia --optimize=0 -e "@info("instantiate from setup.py"); import Pkg; Pkg.instantiate(); @info("import Pluto from setup.py"); import Pluto; @info("starting new notebook"); sesh = Pluto.ServerSession(options=Pluto.Configuration.from_flat_kwargs(; pkgimages="no")); nb = Pluto.SessionActions.new(sesh; run_async=false); @info("shutting down notebook"); Pluto.SessionActions.shutdown(sesh, nb; async=false); @info("setup.py done");"')
