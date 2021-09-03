# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdupload

"""
    feffery_antdupload(;kwargs...)
    feffery_antdupload(children::Any;kwargs...)
    feffery_antdupload(children_maker::Function;kwargs...)


An AntdUpload component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `apiUrl` (String; optional)
- `buttonContent` (String; optional)
- `className` (String; optional)
- `fileListMaxLength` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function feffery_antdupload(; kwargs...)
        available_props = Symbol[:children, :id, :apiUrl, :buttonContent, :className, :fileListMaxLength, :loading_state, :style]
        wild_props = Symbol[]
        return Component("feffery_antdupload", "AntdUpload", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdupload(children::Any; kwargs...) = feffery_antdupload(;kwargs..., children = children)
feffery_antdupload(children_maker::Function; kwargs...) = feffery_antdupload(children_maker(); kwargs...)

