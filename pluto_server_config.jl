(
    # Julia Compiler options:
    # This makes Julia's precompilation less optimized for repeated package loads, and more optimized for single package loads. Precompilation will be faster, package loads will be slower. But in total, startup times will be faster, see https://discourse.julialang.org/t/first-pluto-notebook-launches-are-slower-on-julia-1-9-beta-3/93429/
    pkgimages="no",
    # This makes Julia compile faster, and run slightly slower.
    optimize=1,

    # Pluto security options:
    # Disable authentication – jupyter/binder already does its own auth, no need to add more.
    require_secret_for_open_links=false,
    require_secret_for_access=false,
    # Disable the warning message about running code from unknown sources when exiting Safe Preview mode (https://github.com/fonsp/Pluto.jl/pull/2563)
    warn_about_untrusted_code=false,

    # Pluto misc options:
    # Don't try to start Firefox when the server launches
    launch_browser=false,
    # Don't show the "a newer version of Pluto is available" message
    dismiss_update_notification=true,
    # Don't show the file picker at the top of the notebook (because all files stored on binder will be lost). Instead, just show a big download button so users can store the .jl file locally.
    show_file_system=false,
)
