# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdslider

"""
    feffery_antdslider(;kwargs...)

An AntdSlider component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `defaultValue` (Real | Array of Reals; optional)
- `disabled` (Bool; optional)
- `range` (Bool; optional)
- `min` (Real; optional)
- `max` (Real; optional)
- `step` (Real; optional)
- `value` (Real | Array of Reals; optional)
- `marks` (Dict; optional)
- `tooltipVisible` (Bool; optional)
- `tooltipPrefix` (String; optional)
- `tooltipSuffix` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdslider(; kwargs...)
        available_props = Symbol[:id, :className, :style, :defaultValue, :disabled, :range, :min, :max, :step, :value, :marks, :tooltipVisible, :tooltipPrefix, :tooltipSuffix, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdslider", "AntdSlider", "feffery_antd_components", available_props, wild_props; kwargs...)
end

