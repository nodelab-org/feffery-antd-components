# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtext

"""
    feffery_antdtext(;kwargs...)
    feffery_antdtext(children::Any;kwargs...)
    feffery_antdtext(children_maker::Function;kwargs...)


An AntdText component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `code` (Bool; optional)
- `copyable` (Bool; optional)
- `strikethrough` (Bool; optional)
- `disabled` (Bool; optional)
- `mark` (Bool; optional)
- `strong` (Bool; optional)
- `italic` (Bool; optional)
- `underline` (Bool; optional)
- `keyboard` (Bool; optional)
- `type` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdtext(; kwargs...)
        available_props = Symbol[:children, :id, :className, :style, :code, :copyable, :strikethrough, :disabled, :mark, :strong, :italic, :underline, :keyboard, :type, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdtext", "AntdText", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdtext(children::Any; kwargs...) = feffery_antdtext(;kwargs..., children = children)
feffery_antdtext(children_maker::Function; kwargs...) = feffery_antdtext(children_maker(); kwargs...)

