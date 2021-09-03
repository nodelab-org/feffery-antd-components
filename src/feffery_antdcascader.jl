# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdcascader

"""
    feffery_antdcascader(;kwargs...)

An AntdCascader component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `options` (optional)
- `disabled` (Bool; optional)
- `changeOnSelect` (Bool; optional)
- `size` (String; optional)
- `bordered` (Bool; optional)
- `placeholder` (String; optional)
- `defaultValue` (Array of Strings; optional)
- `value` (Array of Strings; optional)
- `expandTrigger` (String; optional)
- `popupPlacement` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdcascader(; kwargs...)
        available_props = Symbol[:id, :className, :style, :options, :disabled, :changeOnSelect, :size, :bordered, :placeholder, :defaultValue, :value, :expandTrigger, :popupPlacement, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdcascader", "AntdCascader", "feffery_antd_components", available_props, wild_props; kwargs...)
end

