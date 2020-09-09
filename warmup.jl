# https://www.youtube.com/watch?v=m2DvmHusyk4

1 + 1

# import Pluto

# session = Pluto.ServerSession()

# path = tempname()
# original = joinpath(pathof(Pluto) |> dirname |> dirname, "sample", "Tower of Hanoi.jl")
# # so that we don't overwrite the file:
# Pluto.readwrite(original, path)

# @info "Loading sample notebook"
# nb = Pluto.load_notebook(Pluto.tamepath(path));
# session.notebooks[nb.notebook_id] = nb;

# @info "Running sample notebook"
# Pluto.update_save_run!(session, nb, nb.cells; run_async=false, prerender_text=true)

# nice! we ran the notebook, so we already precompiled a lot
#= 
@info "Starting HTTP server"
# next, we'll run the HTTP server which needs a bit of nasty code
t = @async Pluto.run(40404; session=session)

sleep(3)
download("http://localhost:40404/")

# lets leave the server running lol

# this is async because it blocks for some reason
# @async Base.throwto(t, InterruptException())
# sleep(2) # i am pulling these numbers out of thin air =#