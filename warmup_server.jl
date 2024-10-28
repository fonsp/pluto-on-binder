@info("instantiate from setup.py")
import Pkg
Pkg.instantiate()

@info("import Pluto from setup.py")
import Pluto

@info("starting new notebook from setup.py")
sesh = Pluto.ServerSession(options=Pluto.Configuration.from_flat_kwargs(; include("pluto_server_config.jl")...))
nb = Pluto.SessionActions.new(sesh; run_async=false)


@info("shutting down notebook from setup.py")
Pluto.SessionActions.shutdown(sesh, nb; async=false)
@info("setup.py done");
