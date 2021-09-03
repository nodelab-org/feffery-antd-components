# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antddivider

"""
    feffery_antddivider(;kwargs...)
    feffery_antddivider(children::Any;kwargs...)
    feffery_antddivider(children_maker::Function;kwargs...)


An AntdDivider component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `innerTextOrientation` (String; optional)
- `isDashed` (Bool; optional)
- `direction` (String; optional)
- `lineColor` (String; optional)
- `fontStyle` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antddivider(; kwargs...)
        available_props = Symbol[:children, :id, :className, :innerTextOrientation, :isDashed, :direction, :lineColor, :fontStyle, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antddivider", "AntdDivider", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antddivider(children::Any; kwargs...) = feffery_antddivider(;kwargs..., children = children)
feffery_antddivider(children_maker::Function; kwargs...) = feffery_antddivider(children_maker(); kwargs...)

