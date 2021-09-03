# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdcol

"""
    feffery_antdcol(;kwargs...)
    feffery_antdcol(children::Any;kwargs...)
    feffery_antdcol(children_maker::Function;kwargs...)


An AntdCol component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `flex` (String | Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `offset` (Real; optional)
- `order` (Real; optional)
- `pull` (Real; optional)
- `push` (Real; optional)
- `span` (Real; optional)
- `style` (Dict; optional)
"""
function feffery_antdcol(; kwargs...)
        available_props = Symbol[:children, :id, :className, :flex, :loading_state, :offset, :order, :pull, :push, :span, :style]
        wild_props = Symbol[]
        return Component("feffery_antdcol", "AntdCol", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdcol(children::Any; kwargs...) = feffery_antdcol(;kwargs..., children = children)
feffery_antdcol(children_maker::Function; kwargs...) = feffery_antdcol(children_maker(); kwargs...)

