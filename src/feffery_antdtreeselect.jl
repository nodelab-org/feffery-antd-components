# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtreeselect

"""
    feffery_antdtreeselect(;kwargs...)

An AntdTreeSelect component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `treeData` (optional)
- `allowClear` (Bool; optional)
- `bordered` (Bool; optional)
- `listHeight` (Real; optional)
- `placeholder` (String; optional)
- `value` (String | Real | Array of String | Reals; optional)
- `defaultValue` (String | Real | Array of String | Reals; optional)
- `maxTagCount` (Real; optional)
- `multiple` (Bool; optional)
- `size` (String; optional)
- `treeCheckable` (Bool; optional)
- `treeCheckStrictly` (Bool; optional)
- `treeDefaultExpandAll` (Bool; optional)
- `treeDefaultExpandedKeys` (Array of Strings; optional)
- `treeExpandedKeys` (Array of Strings; optional)
- `virtual` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdtreeselect(; kwargs...)
        available_props = Symbol[:id, :className, :style, :treeData, :allowClear, :bordered, :listHeight, :placeholder, :value, :defaultValue, :maxTagCount, :multiple, :size, :treeCheckable, :treeCheckStrictly, :treeDefaultExpandAll, :treeDefaultExpandedKeys, :treeExpandedKeys, :virtual, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdtreeselect", "AntdTreeSelect", "feffery_antd_components", available_props, wild_props; kwargs...)
end

