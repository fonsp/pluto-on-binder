from subprocess import Popen
def load_jupyter_server_extension(nbapp):
    Popen(["julia", "-e", "import Pluto; Pluto.run(\"0.0.0.0\", 1234)"])
