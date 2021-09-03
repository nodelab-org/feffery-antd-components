# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTable(Component):
    """An AntdTable component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- columns (dict; optional): columns has the following type: list of dicts containing keys 'title', 'dataIndex', 'renderOptions', 'fixed', 'editable', 'align', 'width', 'ellipsis', 'sorter', 'render'.
Those keys have the following types:
  - title (string; required)
  - dataIndex (string; required)
  - renderOptions (dict; optional): renderOptions has the following type: dict containing keys 'renderType', 'renderLinkText'.
Those keys have the following types:
  - renderType (string; optional)
  - renderLinkText (string; optional)
  - fixed (string; optional)
  - editable (boolean; optional)
  - align (string; optional)
  - width (number | string; optional)
  - ellipsis (boolean | number | string | dict | list; optional)
  - sorter (boolean | number | string | dict | list; optional)
  - render (boolean | number | string | dict | list; optional)
- data (list of dicts; optional)
- sortOptions (dict; default {
    sortDataIndexes: []
}): sortOptions has the following type: dict containing keys 'sortDataIndexes', 'multiple'.
Those keys have the following types:
  - sortDataIndexes (list of strings; optional)
  - multiple (boolean; optional)
- filterOptions (dict; optional)
- pagination (dict; optional): pagination has the following type: boolean | dict containing keys 'position', 'pageSize', 'current', 'pageSizeOptions', 'showQuickJumper', 'showTotalPrefix', 'showTotalSuffix', 'total'.
Those keys have the following types:
  - position (string; optional)
  - pageSize (number; optional)
  - current (number; optional)
  - pageSizeOptions (list of numbers; optional)
  - showQuickJumper (boolean; optional)
  - showTotalPrefix (string; optional)
  - showTotalSuffix (string; optional)
  - total (number; optional)
- autoIgnorePagination (boolean; default False)
- bordered (boolean; default False)
- maxHeight (number; optional)
- currentData (list; optional)
- recentlyChangedRow (dict; optional)
- sorter (dict; optional): sorter has the following type: dict containing keys 'columns', 'orders'.
Those keys have the following types:
  - columns (list of strings; optional)
  - orders (list of strings; optional)
- filter (dict; optional)
- mode (string; default 'client-side')
- popupContainerId (string; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, columns=Component.UNDEFINED, data=Component.UNDEFINED, sortOptions=Component.UNDEFINED, filterOptions=Component.UNDEFINED, pagination=Component.UNDEFINED, autoIgnorePagination=Component.UNDEFINED, bordered=Component.UNDEFINED, maxHeight=Component.UNDEFINED, currentData=Component.UNDEFINED, recentlyChangedRow=Component.UNDEFINED, sorter=Component.UNDEFINED, filter=Component.UNDEFINED, mode=Component.UNDEFINED, popupContainerId=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'columns', 'data', 'sortOptions', 'filterOptions', 'pagination', 'autoIgnorePagination', 'bordered', 'maxHeight', 'currentData', 'recentlyChangedRow', 'sorter', 'filter', 'mode', 'popupContainerId', 'loading_state']
        self._type = 'AntdTable'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'columns', 'data', 'sortOptions', 'filterOptions', 'pagination', 'autoIgnorePagination', 'bordered', 'maxHeight', 'currentData', 'recentlyChangedRow', 'sorter', 'filter', 'mode', 'popupContainerId', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTable, self).__init__(**args)
