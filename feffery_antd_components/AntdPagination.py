# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdPagination(Component):
    """An AntdPagination component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- defaultCurrent (number; default 1)
- defaultPageSize (number; default 10)
- current (number; optional)
- disabled (boolean; optional)
- hideOnSinglePage (boolean; optional)
- pageSize (number; optional)
- pageSizeOptions (list of numbers; optional)
- showQuickJumper (boolean; optional)
- showSizeChanger (boolean; optional)
- showTotalPrefix (string; optional)
- showTotalSuffix (string; optional)
- simple (boolean; optional)
- size (string; optional)
- total (number; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, defaultCurrent=Component.UNDEFINED, defaultPageSize=Component.UNDEFINED, current=Component.UNDEFINED, disabled=Component.UNDEFINED, hideOnSinglePage=Component.UNDEFINED, pageSize=Component.UNDEFINED, pageSizeOptions=Component.UNDEFINED, showQuickJumper=Component.UNDEFINED, showSizeChanger=Component.UNDEFINED, showTotalPrefix=Component.UNDEFINED, showTotalSuffix=Component.UNDEFINED, simple=Component.UNDEFINED, size=Component.UNDEFINED, total=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'defaultCurrent', 'defaultPageSize', 'current', 'disabled', 'hideOnSinglePage', 'pageSize', 'pageSizeOptions', 'showQuickJumper', 'showSizeChanger', 'showTotalPrefix', 'showTotalSuffix', 'simple', 'size', 'total', 'loading_state']
        self._type = 'AntdPagination'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'defaultCurrent', 'defaultPageSize', 'current', 'disabled', 'hideOnSinglePage', 'pageSize', 'pageSizeOptions', 'showQuickJumper', 'showSizeChanger', 'showTotalPrefix', 'showTotalSuffix', 'simple', 'size', 'total', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdPagination, self).__init__(**args)
