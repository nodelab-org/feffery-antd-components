# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtitle

"""
    feffery_antdtitle(;kwargs...)
    feffery_antdtitle(children::Any;kwargs...)
    feffery_antdtitle(children_maker::Function;kwargs...)


An AntdTitle component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `code` (Bool; optional)
- `copyable` (Bool; optional)
- `disabled` (Bool; optional)
- `italic` (Bool; optional)
- `keyboard` (Bool; optional)
- `level` (Real; optional)
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
function feffery_antdtitle(; kwargs...)
        available_props = Symbol[:children, :id, :className, :code, :copyable, :disabled, :italic, :keyboard, :level, :loading_state, :mark, :strikethrough, :strong, :style, :type, :underline]
        wild_props = Symbol[]
        return Component("feffery_antdtitle", "AntdTitle", "feffery_antd_components", available_props, wild_props; kwargs...)
end

feffery_antdtitle(children::Any; kwargs...) = feffery_antdtitle(;kwargs..., children = children)
feffery_antdtitle(children_maker::Function; kwargs...) = feffery_antdtitle(children_maker(); kwargs...)

