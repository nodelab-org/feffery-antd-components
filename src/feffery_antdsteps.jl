# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdsteps

"""
    feffery_antdsteps(;kwargs...)

An AntdSteps component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `current` (Real; optional)
- `direction` (String; optional)
- `labelPlacement` (String; optional)
- `progressDot` (Bool; optional)
- `size` (String; optional)
- `status` (String; optional)
- `type` (String; optional)
- `steps` (optional): . steps has the following type: Array of lists containing elements 'title', 'subTitle', 'description'.
Those elements have the following types:
  - `title` (String; required)
  - `subTitle` (String; optional)
  - `description` (String; optional)s
"""
function feffery_antdsteps(; kwargs...)
        available_props = Symbol[:id, :className, :style, :loading_state, :current, :direction, :labelPlacement, :progressDot, :size, :status, :type, :steps]
        wild_props = Symbol[]
        return Component("feffery_antdsteps", "AntdSteps", "feffery_antd_components", available_props, wild_props; kwargs...)
end

