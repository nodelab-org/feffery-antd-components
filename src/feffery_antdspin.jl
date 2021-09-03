# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdspin

"""
    feffery_antdspin(;kwargs...)
    feffery_antdspin(children::Any;kwargs...)
    feffery_antdspin(children_maker::Function;kwargs...)


An AntdSpin component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `spinning` (Bool; optional)
- `size` (String; optional)
- `delay` (Real; optional)
- `text` (String; optional)
- `excludeProps` (Array of Strings; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdspin(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style, :spinning, :size, :delay, :text, :excludeProps, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdspin", "AntdSpin", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdspin(children::Any; kwargs...) = feffery_antdspin(;kwargs..., children = children)
feffery_antdspin(children_maker::Function; kwargs...) = feffery_antdspin(children_maker(); kwargs...)

