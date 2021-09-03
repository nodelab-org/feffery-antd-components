# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdempty

"""
    feffery_antdempty(;kwargs...)

An AntdEmpty component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `description` (String; optional)
- `image` (String; optional)
- `imageStyle` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdempty(; kwargs...)
        available_props = Symbol[:id, :className, :style, :description, :image, :imageStyle, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdempty", "AntdEmpty", "feffery_antd_components", available_props, wild_props; kwargs...)
end

