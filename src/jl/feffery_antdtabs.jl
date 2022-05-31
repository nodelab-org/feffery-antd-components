# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtabs

"""
    feffery_antdtabs(;kwargs...)
    feffery_antdtabs(children::Any;kwargs...)
    feffery_antdtabs(children_maker::Function;kwargs...)


An AntdTabs component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): tab children, i.e. contents
- `id` (String; optional)
- `activeKey` (String; optional)
- `animated` (Bool; optional): whether to animate change of tab
- `className` (String; optional)
- `defaultActiveKey` (String; optional)
- `disabled` (Bool; optional)
- `forceRender` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `nClicksAdd` (Real; optional): number of times add button has been clicked
- `nClicksRemove` (Real; optional): number of times add button has been clicked
- `nTabClicks` (Real; optional): number of times add button has been clicked
- `size` (String; optional)
- `style` (Dict; optional): new tab to add on click
- `tabPosition` (String; optional)
- `targetKey` (String; optional)
"""
function feffery_antdtabs(; kwargs...)
        available_props = Symbol[:children, :id, :activeKey, :animated, :className, :defaultActiveKey, :disabled, :forceRender, :loading_state, :nClicksAdd, :nClicksRemove, :nTabClicks, :size, :style, :tabPosition, :targetKey]
        wild_props = Symbol[]
        return Component("feffery_antdtabs", "AntdTabs", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdtabs(children::Any; kwargs...) = feffery_antdtabs(;kwargs..., children = children)
feffery_antdtabs(children_maker::Function; kwargs...) = feffery_antdtabs(children_maker(); kwargs...)

