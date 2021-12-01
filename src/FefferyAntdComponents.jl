
module FefferyAntdComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1rc1"

include("feffery_antdtabpane.jl")
include("feffery_antdtabs.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_antd_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_antd_components.min.js",
    external_url = "https://unpkg.com/feffery_antd_components@0.0.1rc1/feffery_antd_components/feffery_antd_components.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_antd_components.min.js.map",
    external_url = "https://unpkg.com/feffery_antd_components@0.0.1rc1/feffery_antd_components/feffery_antd_components.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
