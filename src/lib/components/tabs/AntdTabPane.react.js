import React, { } from 'react';
import PropTypes from 'prop-types';
import 'antd/dist/antd.css';

const { Tabs } = antd;
const { TabPane } = Tabs;

const parseChildrenToArray = children => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};

const resolveChildProps = (child) => {
    // This may need to change in the future if https://github.com/plotly/dash-renderer/issues/84 is addressed
    if (
        // disabled is a defaultProp (so it's always set)
        // meaning that if it's not set on child.props, the actual
        // props we want are lying a bit deeper - which means they
        // are coming from Dash
        isNil(child.props.disabled) &&
        child.props._dashprivate_layout &&
        child.props._dashprivate_layout.props
    ) {
        // props are coming from Dash
        return child.props._dashprivate_layout.props;
    } else {
        // else props are coming from React (e.g. Demo.js, or Tabs.test.js)
        return child.props;
    }
};


// https://ant.design/components/tabs-cn/
export default function AntdTabPane (props) {

    const resolvedProps = resolveChildProps(props) 

    const {
        id,
        children,
        className,
        style,
        tab,
        disabled,
        loading_state,
        ...otherProps
    } = resolvedProps;

    return (
        <TabPane
            className={className}
            closable={true}
            disabled={disabled}
            forceRender={forceRender}
            id={id}
            key={id}
            loading_state={loading_state}
            style={style}
            tab={tab}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {parseChildrenToArray(children)}
        </TabPane>
    )
}

//
AntdTabPane.propTypes = {
    // id
    id: PropTypes.string.isRequired,

    /**
     * The content of the tab - will only be displayed if this tab is selected
     */
    children: PropTypes.node,

    // css
    className: PropTypes.string,

    // inline CSS styles for pane
    style: PropTypes.object,

    // title of tab displayed in tab bar
    tab: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),

    // inline  CSS styles for tab title. Useful for fixing width to avoid problems with flexbox when changint tabTitle after render
    // tabTitleStyle: PropTypes.object,
    // 
    // key: PropTypes.string,

    // 
    disabled: PropTypes.bool,

    // default true
    // closable: PropTypes.bool,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 
AntdTabPane.defaultProps = {
    className:"antd-tabpane",
    disabled:false,
    style:{},
    tab:"New Tab"
}