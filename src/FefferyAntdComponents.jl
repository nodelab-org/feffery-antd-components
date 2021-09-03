
module FefferyAntdComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1rc1"

include("feffery_antdalert.jl")
include("feffery_antdanchor.jl")
include("feffery_antdbutton.jl")
include("feffery_antdcascader.jl")
include("feffery_antdcheckbox.jl")
include("feffery_antdcheckboxgroup.jl")
include("feffery_antdcollapse.jl")
include("feffery_antddatepicker.jl")
include("feffery_antddaterangepicker.jl")
include("feffery_antddivider.jl")
include("feffery_antddrawer.jl")
include("feffery_antdempty.jl")
include("feffery_antdinput.jl")
include("feffery_antdmenu.jl")
include("feffery_antdmessage.jl")
include("feffery_antdmodal.jl")
include("feffery_antdnotification.jl")
include("feffery_antdpagination.jl")
include("feffery_antdpopover.jl")
include("feffery_antdradiogroup.jl")
include("feffery_antdresult.jl")
include("feffery_antdselect.jl")
include("feffery_antdskeleton.jl")
include("feffery_antdslider.jl")
include("feffery_antdspace.jl")
include("feffery_antdspin.jl")
include("feffery_antdsteps.jl")
include("feffery_antdswitch.jl")
include("feffery_antdtable.jl")
include("feffery_antdtag.jl")
include("feffery_antdtooltip.jl")
include("feffery_antdtransfer.jl")
include("feffery_antdtree.jl")
include("feffery_antdtreeselect.jl")
include("feffery_antdupload.jl")
include("feffery_antdcol.jl")
include("feffery_antdrow.jl")
include("feffery_antdcontent.jl")
include("feffery_antdfooter.jl")
include("feffery_antdheader.jl")
include("feffery_antdlayout.jl")
include("feffery_antdsider.jl")
include("feffery_antdtabpane.jl")
include("feffery_antdtabs.jl")
include("feffery_antdparagraph.jl")
include("feffery_antdtext.jl")
include("feffery_antdtitle.jl")
include("feffery_antdtypography.jl")

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
