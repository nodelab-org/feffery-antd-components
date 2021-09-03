# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdcheckbox

"""
    feffery_antdcheckbox(;kwargs...)

An AntdCheckbox component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `disabled` (Bool; optional)
- `label` (String; optional)
- `checked` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdcheckbox(; kwargs...)
        available_props = Symbol[:id, :className, :style, :disabled, :label, :checked, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdcheckbox", "AntdCheckbox", "feffery_antd_components", available_props, wild_props; kwargs...)
end

