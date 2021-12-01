# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtabpane

"""
    feffery_antdtabpane(;kwargs...)
    feffery_antdtabpane(children::Any;kwargs...)
    feffery_antdtabpane(children_maker::Function;kwargs...)


An AntdTabPane component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; required)
- `className` (String; optional)
- `icon` (String; optional)
- `style` (Dict; optional)
- `tabTitle` (String; optional)
- `disabled` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdtabpane(; kwargs...)
        available_props = Symbol[:children, :id, :className, :icon, :style, :tabTitle, :disabled, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdtabpane", "AntdTabPane", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdtabpane(children::Any; kwargs...) = feffery_antdtabpane(;kwargs..., children = children)
feffery_antdtabpane(children_maker::Function; kwargs...) = feffery_antdtabpane(children_maker(); kwargs...)

