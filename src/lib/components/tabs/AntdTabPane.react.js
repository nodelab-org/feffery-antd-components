import React, { Component } from 'react';
import PropTypes from 'prop-types';
import 'antd/dist/antd.css';

const parseChildrenToArray = children => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};

// https://ant.design/components/tabs-cn/
export default class AntdTabPane extends Component {
    render() {
        const {
            id,
            children,
            className,
            style,
            tab,
            key,
            disabled,
            // closable,
            setProps,
            loading_state
        } = this.props;

        return (
            <div id={id}
                className={className}
                style={style}
                tab={tab}
                key={key}
                disabled={disabled}
                // closable={closable}
                children={parseChildrenToArray(children)}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }>
            </div>
        );
    }
}

//
AntdTabPane.propTypes = {
    // id
    id: PropTypes.string,

    /**
     * The content of the tab - will only be displayed if this tab is selected
     */
    children: PropTypes.node,

    // css
    className: PropTypes.string,

    // 
    style: PropTypes.object,

    // 
    tab: PropTypes.string,

    // 
    key: PropTypes.string,

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
}