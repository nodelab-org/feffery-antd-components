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
- `className` (String; optional)
- `style` (Dict; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `title` (String; optional)
- `visible` (Bool; optional)
- `okText` (String; optional)
- `cancelText` (String; optional)
- `renderFooter` (Bool; optional)
- `width` (Real; optional)
- `centered` (Bool; optional)
- `keyboard` (Bool; optional)
- `closable` (Bool; optional)
- `mask` (Bool; optional)
- `maskClosable` (Bool; optional)
- `okCounts` (Real; optional)
- `cancelCounts` (Real; optional)
- `closeCounts` (Real; optional)
"""
function feffery_antdmodal(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style, :loading_state, :title, :visible, :okText, :cancelText, :renderFooter, :width, :centered, :keyboard, :closable, :mask, :maskClosable, :okCounts, :cancelCounts, :closeCounts]
        wild_props = Symbol[]
        return Component("feffery_antdmodal", "AntdModal", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdmodal(children::Any; kwargs...) = feffery_antdmodal(;kwargs..., children = children)
feffery_antdmodal(children_maker::Function; kwargs...) = feffery_antdmodal(children_maker(); kwargs...)

