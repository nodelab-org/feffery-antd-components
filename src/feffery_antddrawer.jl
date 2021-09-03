# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antddrawer

"""
    feffery_antddrawer(;kwargs...)
    feffery_antddrawer(children::Any;kwargs...)
    feffery_antddrawer(children_maker::Function;kwargs...)


An AntdDrawer component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `visible` (Bool; optional)
- `title` (String; optional)
- `placement` (String; optional)
- `closable` (Bool; optional)
- `forceRender` (Bool; optional)
- `destroyOnClose` (Bool; optional)
- `containerId` (String; optional)
- `height` (Real; optional)
- `mask` (Bool; optional)
- `maskClosable` (Bool; optional)
- `width` (Real; optional)
- `zIndex` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antddrawer(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style, :visible, :title, :placement, :closable, :forceRender, :destroyOnClose, :containerId, :height, :mask, :maskClosable, :width, :zIndex, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antddrawer", "AntdDrawer", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antddrawer(children::Any; kwargs...) = feffery_antddrawer(;kwargs..., children = children)
feffery_antddrawer(children_maker::Function; kwargs...) = feffery_antddrawer(children_maker(); kwargs...)

