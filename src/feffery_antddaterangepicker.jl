# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antddaterangepicker

"""
    feffery_antddaterangepicker(;kwargs...)

An AntdDateRangePicker component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `picker` (String; optional)
- `showTime` (Bool; optional)
- `placeholderStart` (String; optional)
- `placeholderEnd` (String; optional)
- `disabledStart` (Bool; optional)
- `disabledEnd` (Bool; optional)
- `selectedStartDate` (String; optional)
- `selectedEndDate` (String; optional)
- `bordered` (Bool; optional)
- `defaultPickerValue` (optional): . defaultPickerValue has the following type: lists containing elements 'value', 'format'.
Those elements have the following types:
  - `value` (String; optional)
  - `format` (String; optional)
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antddaterangepicker(; kwargs...)
        available_props = Symbol[:id, :className, :style, :picker, :showTime, :placeholderStart, :placeholderEnd, :disabledStart, :disabledEnd, :selectedStartDate, :selectedEndDate, :bordered, :defaultPickerValue, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antddaterangepicker", "AntdDateRangePicker", "feffery_antd_components", available_props, wild_props; kwargs...)
end

