# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSteps(Component):
    """An AntdSteps component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- current (number; default 0)
- direction (string; default 'horizontal')
- labelPlacement (string; optional)
- progressDot (boolean; default False)
- size (string; default 'default')
- status (string; default 'process')
- type (string; optional)
- steps (dict; optional): steps has the following type: list of dicts containing keys 'title', 'subTitle', 'description'.
Those keys have the following types:
  - title (string; required)
  - subTitle (string; optional)
  - description (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, loading_state=Component.UNDEFINED, current=Component.UNDEFINED, direction=Component.UNDEFINED, labelPlacement=Component.UNDEFINED, progressDot=Component.UNDEFINED, size=Component.UNDEFINED, status=Component.UNDEFINED, type=Component.UNDEFINED, steps=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'loading_state', 'current', 'direction', 'labelPlacement', 'progressDot', 'size', 'status', 'type', 'steps']
        self._type = 'AntdSteps'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'loading_state', 'current', 'direction', 'labelPlacement', 'progressDot', 'size', 'status', 'type', 'steps']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdSteps, self).__init__(**args)
