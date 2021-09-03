# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSlider(Component):
    """An AntdSlider component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- defaultValue (number | list of numbers; optional)
- disabled (boolean; default False)
- range (boolean; default False)
- min (number; default 0)
- max (number; default 100)
- step (number; default 1)
- value (number | list of numbers; optional)
- marks (dict; optional)
- tooltipVisible (boolean; optional)
- tooltipPrefix (string; default '')
- tooltipSuffix (string; default '')
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, defaultValue=Component.UNDEFINED, disabled=Component.UNDEFINED, range=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, step=Component.UNDEFINED, value=Component.UNDEFINED, marks=Component.UNDEFINED, tooltipVisible=Component.UNDEFINED, tooltipPrefix=Component.UNDEFINED, tooltipSuffix=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'defaultValue', 'disabled', 'range', 'min', 'max', 'step', 'value', 'marks', 'tooltipVisible', 'tooltipPrefix', 'tooltipSuffix', 'loading_state']
        self._type = 'AntdSlider'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'defaultValue', 'disabled', 'range', 'min', 'max', 'step', 'value', 'marks', 'tooltipVisible', 'tooltipPrefix', 'tooltipSuffix', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdSlider, self).__init__(**args)
