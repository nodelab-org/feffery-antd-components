# AUTO GENERATED FILE - DO NOT EDIT

export feffery_antdtree

"""
    feffery_antdtree(;kwargs...)

An AntdTree component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `style` (Dict; optional)
- `treeData` (optional)
- `showIcon` (Bool; optional)
- `checkable` (Bool; optional)
- `defaultExpandAll` (Bool; optional)
- `defaultExpandedKeys` (Array of Strings; optional)
- `defaultExpandParent` (Bool; optional)
- `multiple` (Bool; optional)
- `selectable` (Bool; optional)
- `showLine` (optional): . showLine has the following type: Bool | lists containing elements 'showLeafIcon'.
Those elements have the following types:
  - `showLeafIcon` (Bool; optional)
- `selectedKeys` (Array; optional)
- `checkedKeys` (Array; optional)
- `height` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function feffery_antdtree(; kwargs...)
        available_props = Symbol[:id, :className, :style, :treeData, :showIcon, :checkable, :defaultExpandAll, :defaultExpandedKeys, :defaultExpandParent, :multiple, :selectable, :showLine, :selectedKeys, :checkedKeys, :height, :loading_state]
        wild_props = Symbol[]
        return Component("feffery_antdtree", "AntdTree", "feffery_antd_components", available_props, wild_props; kwargs...)
end

