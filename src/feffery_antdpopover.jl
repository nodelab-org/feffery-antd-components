# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdpopover

"""
    feffery_antdpopover(;kwargs...)
    feffery_antdpopover(children::Any;kwargs...)
    feffery_antdpopover(children_maker::Function;kwargs...)


An AntdPopover component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `title` (String; optional)
- `content` (a list of or a singular dash component, string or number; optional)
- `placement` (String; optional)
- `color` (String; optional)
- `mouseEnterDelay` (Real; optional)
- `mouseLeaveDelay` (Real; optional)
- `overlayClassName` (String; optional)
- `overlayStyle` (Dict; optional)
- `overlayInnerStyle` (Dict; optional)
- `trigger` (String | Array of Strings; optional)
- `contentChildrenIndexes` (Array of Reals; optional)
- `containerId` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdpopover(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style, :title, :content, :placement, :color, :mouseEnterDelay, :mouseLeaveDelay, :overlayClassName, :overlayStyle, :overlayInnerStyle, :trigger, :contentChildrenIndexes, :containerId, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdpopover", "AntdPopover", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdpopover(children::Any; kwargs...) = feffery_antdpopover(;kwargs..., children = children)
feffery_antdpopover(children_maker::Function; kwargs...) = feffery_antdpopover(children_maker(); kwargs...)

