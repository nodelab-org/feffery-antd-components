# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtabs

"""
    feffery_antdtabs(;kwargs...)
    feffery_antdtabs(children::Any;kwargs...)
    feffery_antdtabs(children_maker::Function;kwargs...)


An AntdTabs component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `activeKey` (String; optional)
- `className` (String; optional)
- `defaultActiveKey` (String; optional)
- `latestDeletePane` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `size` (String; optional)
- `style` (Dict; optional)
- `tabPosition` (String; optional)
"""
function feffery_antdtabs(; kwargs...)
        available_props = Symbol[:children, :id, :activeKey, :className, :defaultActiveKey, :latestDeletePane, :loading_state, :size, :style, :tabPosition]
        wild_props = Symbol[]
        return Component("feffery_antdtabs", "AntdTabs", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdtabs(children::Any; kwargs...) = feffery_antdtabs(;kwargs..., children = children)
feffery_antdtabs(children_maker::Function; kwargs...) = feffery_antdtabs(children_maker(); kwargs...)

