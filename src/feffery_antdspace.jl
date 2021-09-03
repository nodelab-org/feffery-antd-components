# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdspace

"""
    feffery_antdspace(;kwargs...)
    feffery_antdspace(children::Any;kwargs...)
    feffery_antdspace(children_maker::Function;kwargs...)


An AntdSpace component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `align` (String; optional)
- `direction` (String; optional)
- `size` (String | Real; optional)
- `addSplitLine` (Bool; optional)
- `wrap` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdspace(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style, :align, :direction, :size, :addSplitLine, :wrap, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdspace", "AntdSpace", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdspace(children::Any; kwargs...) = feffery_antdspace(;kwargs..., children = children)
feffery_antdspace(children_maker::Function; kwargs...) = feffery_antdspace(children_maker(); kwargs...)

