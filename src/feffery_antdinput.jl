# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdinput

"""
    feffery_antdinput(;kwargs...)

An AntdInput component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `mode` (String; optional)
- `placeholder` (String; optional)
- `size` (String; optional)
- `addonBefore` (String; optional)
- `addonAfter` (String; optional)
- `allowClear` (Bool; optional)
- `bordered` (Bool; optional)
- `defaultValue` (String; optional)
- `disabled` (Bool; optional)
- `maxLength` (Real; optional)
- `value` (String; optional)
- `showCount` (Bool; optional)
- `nSubmit` (Real; optional)
- `nClicksSearch` (Real; optional)
"""
function feffery_antdinput(; kwargs...)
        available_props = Symbol[:id, :className, :style, :loading_state, :mode, :placeholder, :size, :addonBefore, :addonAfter, :allowClear, :bordered, :defaultValue, :disabled, :maxLength, :value, :showCount, :nSubmit, :nClicksSearch]
        wild_props = Symbol[]
        return Component("feffery_antdinput", "AntdInput", "feffery_antd_components", available_props, wild_props; kwargs...)
end

