# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdmodal

"""
    feffery_antdmodal(;kwargs...)
    feffery_antdmodal(children::Any;kwargs...)
    feffery_antdmodal(children_maker::Function;kwargs...)


An AntdModal component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional)
- `cancelCounts` (Real; optional)
- `cancelText` (String; optional)
- `centered` (Bool; optional)
- `className` (String; optional)
- `closable` (Bool; optional)
- `closeCounts` (Real; optional)
- `keyboard` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `mask` (Bool; optional)
- `maskClosable` (Bool; optional)
- `okCounts` (Real; optional)
- `okText` (String; optional)
- `renderFooter` (Bool; optional)
- `style` (Dict; optional)
- `title` (String; optional)
- `visible` (Bool; optional)
- `width` (Real; optional)
"""
function feffery_antdmodal(; kwargs...)
        available_props = Symbol[:children, :id, :cancelCounts, :cancelText, :centered, :className, :closable, :closeCounts, :keyboard, :loading_state, :mask, :maskClosable, :okCounts, :okText, :renderFooter, :style, :title, :visible, :width]
        wild_props = Symbol[]
        return Component("feffery_antdmodal", "AntdModal", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdmodal(children::Any; kwargs...) = feffery_antdmodal(;kwargs..., children = children)
feffery_antdmodal(children_maker::Function; kwargs...) = feffery_antdmodal(children_maker(); kwargs...)

