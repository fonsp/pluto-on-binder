import Pluto

@assert haskey(ENV, "JSP_PORT")

Pluto.run(
    host="0.0.0.0",
    port=parse(Int64, get(ENV, "JSP_PORT", nothing)),

    pkgimages="no",

    require_secret_for_open_links=false,
    require_secret_for_access=false,
    warn_about_untrusted_code=false,

    launch_browser=false,
    dismiss_update_notification=true,
    show_file_system=false,
)