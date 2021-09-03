# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDateRangePicker(Component):
    """An AntdDateRangePicker component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- picker (string; default 'date')
- showTime (boolean; default False)
- placeholderStart (string; optional)
- placeholderEnd (string; optional)
- disabledStart (boolean; optional)
- disabledEnd (boolean; optional)
- selectedStartDate (string; optional)
- selectedEndDate (string; optional)
- bordered (boolean; default True)
- defaultPickerValue (dict; optional): defaultPickerValue has the following type: dict containing keys 'value', 'format'.
Those keys have the following types:
  - value (string; optional)
  - format (string; optional)
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, picker=Component.UNDEFINED, showTime=Component.UNDEFINED, placeholderStart=Component.UNDEFINED, placeholderEnd=Component.UNDEFINED, disabledStart=Component.UNDEFINED, disabledEnd=Component.UNDEFINED, selectedStartDate=Component.UNDEFINED, selectedEndDate=Component.UNDEFINED, bordered=Component.UNDEFINED, defaultPickerValue=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'picker', 'showTime', 'placeholderStart', 'placeholderEnd', 'disabledStart', 'disabledEnd', 'selectedStartDate', 'selectedEndDate', 'bordered', 'defaultPickerValue', 'loading_state']
        self._type = 'AntdDateRangePicker'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'picker', 'showTime', 'placeholderStart', 'placeholderEnd', 'disabledStart', 'disabledEnd', 'selectedStartDate', 'selectedEndDate', 'bordered', 'defaultPickerValue', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdDateRangePicker, self).__init__(**args)
