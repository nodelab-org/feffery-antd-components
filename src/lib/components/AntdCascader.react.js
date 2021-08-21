import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Cascader, ConfigProvider } from 'antd';
import zhCN from 'antd/lib/locale/zh_CN';
import 'antd/dist/antd.css';

// 定义级联选择部件AntdCascader，api参数参考https://ant.design/components/cascader-cn/
export default class AntdCascader extends Component {

    constructor(props) {
        super(props)
        if (!props.value) {
            props.setProps({ value: props.defaultValue })
        }

    }

    render() {
        // 取得必要属性或参数
        let {
            id,
            style,
            className,
            options,
            setProps,
            loading_state
        } = this.props;

        // 返回定制化的前端部件
        return (
            <ConfigProvider locale={zhCN}>
                <Cascader
                    id={id}
                    className={className}
                    style={{ ...{ width: '100%' }, ...style }}
                    options={options}
                    data-dash-is-loading={
                        (loading_state && loading_state.is_loading) || undefined
                    }
                    getPopupContainer={(triggerNode) => triggerNode.parentNode}
                />
            </ConfigProvider>
        );
    }
}

// 定义递归PropTypes
const PropOptionNodeShape = {
    // 选项对应的值
    value: PropTypes.string.isRequired,

    // 选项对应显示的文字标题
    label: PropTypes.string.isRequired

};

const PropOptionNode = PropTypes.shape(PropOptionNodeShape);
PropOptionNodeShape.children = PropTypes.arrayOf(PropOptionNode);
const optionDataPropTypes = PropTypes.arrayOf(PropOptionNode);

// 定义参数或属性
AntdCascader.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 组织选项层级结构对应的json数据
    options: optionDataPropTypes.isRequired,

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

// 设置默认参数
AntdCascader.defaultProps = {}
