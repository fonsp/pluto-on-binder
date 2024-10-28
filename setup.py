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
