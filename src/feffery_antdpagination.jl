# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdpagination

"""
    feffery_antdpagination(;kwargs...)

An AntdPagination component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `defaultCurrent` (Real; optional)
- `defaultPageSize` (Real; optional)
- `current` (Real; optional)
- `disabled` (Bool; optional)
- `hideOnSinglePage` (Bool; optional)
- `pageSize` (Real; optional)
- `pageSizeOptions` (Array of Reals; optional)
- `showQuickJumper` (Bool; optional)
- `showSizeChanger` (Bool; optional)
- `showTotalPrefix` (String; optional)
- `showTotalSuffix` (String; optional)
- `simple` (Bool; optional)
- `size` (String; optional)
- `total` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdpagination(; kwargs...)
        available_props = Symbol[:id, :className, :style, :defaultCurrent, :defaultPageSize, :current, :disabled, :hideOnSinglePage, :pageSize, :pageSizeOptions, :showQuickJumper, :showSizeChanger, :showTotalPrefix, :showTotalSuffix, :simple, :size, :total, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdpagination", "AntdPagination", "feffery_antd_components", available_props, wild_props; kwargs...)
end

