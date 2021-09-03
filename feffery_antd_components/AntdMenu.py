# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdMenu(Component):
    """An AntdMenu component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- menuItems (list; optional)
- mode (string; default 'vertical')
- theme (string; default 'light')
- currentKey (string; optional)
- defaultOpenKeys (list of strings; optional)
- defaultSelectedKey (string; optional)
- renderCollapsedButton (boolean; default False)
- loading_state (dict; optional): loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, menuItems=Component.UNDEFINED, mode=Component.UNDEFINED, theme=Component.UNDEFINED, currentKey=Component.UNDEFINED, defaultOpenKeys=Component.UNDEFINED, defaultSelectedKey=Component.UNDEFINED, renderCollapsedButton=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'menuItems', 'mode', 'theme', 'currentKey', 'defaultOpenKeys', 'defaultSelectedKey', 'renderCollapsedButton', 'loading_state']
        self._type = 'AntdMenu'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'menuItems', 'mode', 'theme', 'currentKey', 'defaultOpenKeys', 'defaultSelectedKey', 'renderCollapsedButton', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdMenu, self).__init__(**args)
