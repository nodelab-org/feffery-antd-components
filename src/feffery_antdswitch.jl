# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdswitch

"""
    feffery_antdswitch(;kwargs...)

An AntdSwitch component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `disabled` (Bool; optional)
- `checked` (Bool; optional)
- `checkedChildren` (String; optional)
- `unCheckedChildren` (String; optional)
- `size` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdswitch(; kwargs...)
        available_props = Symbol[:id, :className, :style, :disabled, :checked, :checkedChildren, :unCheckedChildren, :size, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdswitch", "AntdSwitch", "feffery_antd_components", available_props, wild_props; kwargs...)
end

