# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdswitch

"""
    feffery_antdswitch(;kwargs...)

An AntdSwitch component.

Keyword arguments:
- `id` (String; optional)
- `checked` (Bool; optional)
- `checkedChildren` (String; optional)
- `className` (String; optional)
- `disabled` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `size` (String; optional)
- `style` (Dict; optional)
- `unCheckedChildren` (String; optional)
"""
function feffery_antdswitch(; kwargs...)
        available_props = Symbol[:id, :checked, :checkedChildren, :className, :disabled, :loading_state, :size, :style, :unCheckedChildren]
        wild_props = Symbol[]
        return Component("feffery_antdswitch", "AntdSwitch", "feffery_antd_components", available_props, wild_props; kwargs...)
end

