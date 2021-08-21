import React, { Component } from 'react';
import PropTypes from 'prop-types';
import TextLoop from 'react-text-loop'
import { Alert } from 'antd';
import 'antd/dist/antd.css';

// 定义警告提示部件AntdAlert，api参数参考https://ant.design/components/alert-cn/
export default class AntdAlert extends Component {
    render() {
        // 取得必要属性或参数
        let {
            id,
            className,
            style,
            message,
            type,
            description,
            banner,
            showIcon,
            closable,
            renderLoopText,
            setProps
        } = this.props;

        if (renderLoopText && Array.isArray(message)) {
            return (
                <Alert id={id}
                    className={className}
                    style={style}
                    message={
                        <TextLoop mask>
                            {message.map(item => <div>{item}</div>)}
                        </TextLoop>
                    }
                    type={type}
                    description={description}
                    banner={banner}
                    showIcon={showIcon}
                    closable={closable}>
                </Alert>
            );
        }

        return (
            <Alert id={id}
                className={className}
                style={style}
                message={message}
                type={type}
                description={description}
                banner={banner}
                showIcon={showIcon}
                closable={closable}>
            </Alert>
        );
    }
}

// 定义参数或属性
AntdAlert.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

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

    // 设置显示的文字信息
    message: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.arrayOf(PropTypes.string)
    ]),

    // 设置提示类型，可选的有'success'、'info'、'warning'和'error'四种
    type: PropTypes.string,

    // 设置警告提示的辅助性文字介绍
    description: PropTypes.string,

    // 设置是否开启顶部公告模式，默认为false
    banner: PropTypes.bool,

    // 设置是否显示辅助图标，默认为false（banner=true时默认为true）
    showIcon: PropTypes.bool,

    // 设置警告提示是否有关闭按钮，默认为false
    closable: PropTypes.bool,

    // 设置是否启动轮播文字模式，默认为false
    renderLoopText: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

// 设置默认参数
AntdAlert.defaultProps = {
    closable: false,
    renderLoopText: false
}
