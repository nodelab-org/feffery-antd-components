import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Upload, message, Button, ConfigProvider } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import zhCN from 'antd/lib/locale/zh_CN';
import 'antd/dist/antd.css';

// 定义文件上传部件AntdUpload，api参数参考https://ant.design/components/upload-cn/
const AntdUpload = (props) => {

    // 取得必要属性或参数
    let {
        id,
        children,
        className,
        style,
        apiUrl,
        fileListMaxLength,
        buttonContent,
        loading_state
    } = props;

    const [fileList, updateFileList] = useState([]);

    const uploadProps = {
        name: 'file',
        action: apiUrl,
        headers: {
            // authorization: 'authorization-text',
        },
        onChange(info) {

            if (info.file.status !== 'uploading') {
                console.log(info);
            }
            if (info.file.status === 'done') {
                console.log('上传成功：')
                console.log(info);
                message.success(`${info.file.name} 上传成功！`);
            } else if (info.file.status === 'error') {
                console.log('上传失败：')
                console.log(info);
                message.error(`${info.file.name} 上传失败！`);
            }

            // 基于fileListMaxLength参数设置，对fileList状态进行更新
            updateFileList(info.fileList.slice(-fileListMaxLength))
        },
    };


    // 返回定制化的前端部件
    return (
        <ConfigProvider locale={zhCN}>
            <Upload {...uploadProps}
                fileList={fileList}>
                <Button icon={<UploadOutlined />}>{buttonContent ? buttonContent : "点击上传文件"}</Button>
            </Upload>
        </ConfigProvider>

    );
}

// 定义参数或属性
AntdUpload.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 内嵌文字的文本内容
    children: PropTypes.node,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置文件上传服务的接口url
    apiUrl: PropTypes.string,

    // 设置已上传文件列表的最大显示长度，默认为3
    fileListMaxLength: PropTypes.number,

    // 按钮模式下设置按钮内的文字内容
    buttonContent: PropTypes.string,

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
AntdUpload.defaultProps = {
    fileListMaxLength: 3
}

export default AntdUpload;
