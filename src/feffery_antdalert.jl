# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdalert

"""
    feffery_antdalert(;kwargs...)

An AntdAlert component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `message` (String | Array of Strings; optional)
- `type` (String; optional)
- `description` (String; optional)
- `banner` (Bool; optional)
- `showIcon` (Bool; optional)
- `closable` (Bool; optional)
- `renderLoopText` (Bool; optional)
"""
function feffery_antdalert(; kwargs...)
        available_props = Symbol[:id, :className, :style, :loading_state, :message, :type, :description, :banner, :showIcon, :closable, :renderLoopText]
        wild_props = Symbol[]
        return Component("feffery_antdalert", "AntdAlert", "feffery_antd_components", available_props, wild_props; kwargs...)
end

