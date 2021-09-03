# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antddatepicker

"""
    feffery_antddatepicker(;kwargs...)

An AntdDatePicker component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `picker` (String; optional)
- `selectedDate` (String; optional)
- `showTime` (Bool; optional)
- `allowClear` (Bool; optional)
- `defaultPickerValue` (optional): . defaultPickerValue has the following type: lists containing elements 'value', 'format'.
Those elements have the following types:
  - `value` (String; optional)
  - `format` (String; optional)
- `placeholder` (String; optional)
- `bordered` (Bool; optional)
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antddatepicker(; kwargs...)
        available_props = Symbol[:id, :className, :style, :picker, :selectedDate, :showTime, :allowClear, :defaultPickerValue, :placeholder, :bordered, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antddatepicker", "AntdDatePicker", "feffery_antd_components", available_props, wild_props; kwargs...)
end

