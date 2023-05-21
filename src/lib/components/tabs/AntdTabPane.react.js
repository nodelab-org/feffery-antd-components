import React, { } from 'react';
import PropTypes from 'prop-types';
import 'antd/dist/antd.css';

const parseChildrenToArray = children => {
    if (
        children && !Array.isArray(children)
    ) {
        return [children];
    }
    return children;
};

// https://ant.design/components/tabs-cn/
export default function AntdTabPane (props) {

    const {
        id,
        // key,
        children,
        className,
        icon,
        style,
        tabTitle,
        disabled,
        // closable,
        loading_state
        // ...otherProps
    } = props;

    return (
        <div id={id}
            children={parseChildrenToArray(children)}
            className={className}
            icon={icon}
            style={style}
            tab={tabTitle}
            disabled={disabled}
            // closable={closable} 
            data-dash-is-loading={
                (
                    loading_state && loading_state.is_loading
                ) || undefined
            }
            >
        </div>
    );
    
}

//
AntdTabPane.propTypes = {
    // id
    id: PropTypes.oneOfType(
        [
            PropTypes.string,
            PropTypes.object
        ]
    ).isRequired,

    /**
     * The content of the tab - will only be displayed if this tab is selected
     */
    children: PropTypes.node,

    // css
    className: PropTypes.string,

    // icon to display. Currently must be 'schema' or 'data'
    icon: PropTypes.string, 

    // inline CSS styles for pane
    style: PropTypes.object,

    // title of tab displayed in tab bar
    tabTitle: PropTypes.string,

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
    tabTitle:"New Tab"
}