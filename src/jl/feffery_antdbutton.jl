# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdbutton

"""
    feffery_antdbutton(;kwargs...)
    feffery_antdbutton(children::Any;kwargs...)
    feffery_antdbutton(children_maker::Function;kwargs...)


An AntdButton component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `block` (Bool; optional)
- `className` (String; optional)
- `danger` (Bool; optional)
- `disabled` (Bool; optional)
- `href` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `nClicks` (Real; optional)
- `shape` (String; optional)
- `size` (String; optional)
- `style` (Dict; optional)
- `target` (String; optional)
- `type` (String; optional)
"""
function feffery_antdbutton(; kwargs...)
        available_props = Symbol[:children, :id, :block, :className, :danger, :disabled, :href, :loading_state, :nClicks, :shape, :size, :style, :target, :type]
        wild_props = Symbol[]
        return Component("feffery_antdbutton", "AntdButton", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdbutton(children::Any; kwargs...) = feffery_antdbutton(;kwargs..., children = children)
feffery_antdbutton(children_maker::Function; kwargs...) = feffery_antdbutton(children_maker(); kwargs...)

