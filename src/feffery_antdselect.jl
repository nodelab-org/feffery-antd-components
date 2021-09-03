# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdselect

"""
    feffery_antdselect(;kwargs...)

An AntdSelect component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `options` (optional): . options has the following type: Array of lists containing elements 'label', 'value', 'disabled'.
Those elements have the following types:
  - `label` (String | Real; required)
  - `value` (String | Real; required)
  - `disabled` (Bool; optional) | lists containing elements 'group', 'options'.
Those elements have the following types:
  - `group` (String; required)
  - `options` (optional): . options has the following type: Array of lists containing elements 'label', 'value', 'disabled'.
Those elements have the following types:
  - `label` (String | Real; required)
  - `value` (String | Real; required)
  - `disabled` (Bool; optional)ss
- `allowClear` (Bool; optional)
- `mode` (String; optional)
- `placeholder` (String; optional)
- `value` (String | Real | Array of String | Reals; optional)
- `defaultValue` (String | Real | Array of String | Reals; optional)
- `maxTagCount` (Real; optional)
- `listHeight` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdselect(; kwargs...)
        available_props = Symbol[:id, :className, :style, :options, :allowClear, :mode, :placeholder, :value, :defaultValue, :maxTagCount, :listHeight, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdselect", "AntdSelect", "feffery_antd_components", available_props, wild_props; kwargs...)
end

