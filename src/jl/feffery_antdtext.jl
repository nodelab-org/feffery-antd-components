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
- `code` (Bool; optional)
- `copyable` (Bool; optional)
- `disabled` (Bool; optional)
- `italic` (Bool; optional)
- `keyboard` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `mark` (Bool; optional)
- `strikethrough` (Bool; optional)
- `strong` (Bool; optional)
- `style` (Dict; optional)
- `type` (String; optional)
- `underline` (Bool; optional)
"""
function feffery_antdtext(; kwargs...)
        available_props = Symbol[:children, :id, :className, :code, :copyable, :disabled, :italic, :keyboard, :loading_state, :mark, :strikethrough, :strong, :style, :type, :underline]
        wild_props = Symbol[]
        return Component("feffery_antdtext", "AntdText", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdtext(children::Any; kwargs...) = feffery_antdtext(;kwargs..., children = children)
feffery_antdtext(children_maker::Function; kwargs...) = feffery_antdtext(children_maker(); kwargs...)

