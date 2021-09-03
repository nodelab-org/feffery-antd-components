# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtransfer

"""
    feffery_antdtransfer(;kwargs...)

An AntdTransfer component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `dataSource` (optional): . dataSource has the following type: Array of lists containing elements 'key', 'title'.
Those elements have the following types:
  - `key` (String | Real; optional)
  - `title` (String; optional)s
- `height` (String; optional)
- `pagination` (optional): . pagination has the following type: Bool | lists containing elements 'pageSize'.
Those elements have the following types:
  - `pageSize` (Real; optional)
- `operations` (Array; optional)
- `showSearch` (Bool; optional)
- `showSelectAll` (Bool; optional)
- `titles` (Array; optional)
- `targetKeys` (Array; optional)
- `moveDirection` (String; optional)
- `moveKeys` (Array; optional)
"""
function feffery_antdtransfer(; kwargs...)
        available_props = Symbol[:id, :className, :style, :dataSource, :height, :pagination, :operations, :showSearch, :showSelectAll, :titles, :targetKeys, :moveDirection, :moveKeys]
        wild_props = Symbol[]
        return Component("feffery_antdtransfer", "AntdTransfer", "feffery_antd_components", available_props, wild_props; kwargs...)
end

