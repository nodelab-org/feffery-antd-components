# AUTO GENERATED FILE - DO NOT EDIT

export 'feffery'_antdparagraph

"""
    'feffery'_antdparagraph(;kwargs...)
    'feffery'_antdparagraph(children::Any;kwargs...)
    'feffery'_antdparagraph(children_maker::Function;kwargs...)


An AntdParagraph component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `code` (Bool; optional)
- `copyable` (Bool; optional)
- `disabled` (Bool; optional)
- `ellipsis` (optional): . ellipsis has the following type: Bool | lists containing elements 'rows', 'expandable', 'symbol', 'tooltip'.
Those elements have the following types:
  - `rows` (Real; optional)
  - `expandable` (Bool; optional)
  - `symbol` (String; optional)
  - `tooltip` (Bool; optional)
- `italic` (Bool; optional)
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
function 'feffery'_antdparagraph(; kwargs...)
        available_props = Symbol[:children, :id, :className, :code, :copyable, :disabled, :ellipsis, :italic, :loading_state, :mark, :strikethrough, :strong, :style, :type, :underline]
        wild_props = Symbol[]
        return Component("'feffery'_antdparagraph", "AntdParagraph", "feffery_antd_components", available_props, wild_props; kwargs...)
end

'feffery'_antdparagraph(children::Any; kwargs...) = 'feffery'_antdparagraph(;kwargs..., children = children)
'feffery'_antdparagraph(children_maker::Function; kwargs...) = 'feffery'_antdparagraph(children_maker(); kwargs...)

