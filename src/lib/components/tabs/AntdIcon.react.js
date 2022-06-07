import { ApartmentOutlined, NodeIndexOutlined } from '@ant-design/icons';
import React, { } from 'react';
import PropTypes from 'prop-types';

// https://ant.design/components/tabs-cn/
export default function AntdIcon(props) {

    const {
        id,
        icon,
        ...otherProps
    } = props;

    return Function("<"+icon+" id="+id+" />")();
    
}

//
AntdIcon.propTypes = {
    // id
    id: PropTypes.string.isRequired,

    // icon to display. Currently must be 'schema' or 'data'
    icon: PropTypes.string.isRequired, 
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 
AntdIcon.defaultProps = {
    icon: "ApartmentOutlined"
}