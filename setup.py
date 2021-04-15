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
  install_requires=['jupyter-server-proxy @ git+http://github.com/fonsp/jupyter-server-proxy@3a58aa5005f942d0c208eab9a480f6ab171142ef'],
)

# because this is a demo of Pluto, we add some popular packages to the global package env and precompile
import os
os.system('julia -e "import Pkg; Pkg.add([\\"DataFrames\\", \\"CSV\\", \\"Plots\\"]); Pkg.precompile()"')