# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdcheckboxgroup

"""
    feffery_antdcheckboxgroup(;kwargs...)

An AntdCheckboxGroup component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `disabled` (Bool; optional)
- `title` (String; optional)
- `options` (optional): . options has the following type: Array of lists containing elements 'label', 'value', 'disabled'.
Those elements have the following types:
  - `label` (String; optional)
  - `value` (String; optional)
  - `disabled` (Bool; optional)s
- `value` (Array of Strings; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdcheckboxgroup(; kwargs...)
        available_props = Symbol[:id, :className, :style, :disabled, :title, :options, :value, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdcheckboxgroup", "AntdCheckboxGroup", "feffery_antd_components", available_props, wild_props; kwargs...)
end

