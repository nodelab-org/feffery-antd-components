import React, {useEffect, useState} from "react";
import { Tabs } from 'antd';
import { isNil, omit } from 'ramda';
import 'antd/dist/antd.css';
import { DndProvider, DragSource, DropTarget } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import PropTypes from "prop-types";

const { TabPane } = Tabs;

// coerce children to array if not already
const parseChildrenToArray = (children) => {
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

// Drag & Drop node
function TabNode (props) {
    const { connectDragSource, connectDropTarget, children } = props;
    return (
        connectDragSource(connectDropTarget(children))
    )
}

export default function AntdTabs (props) {

    const [order,setOrder] = useState([])

    // feffery
    let {
        id,
        children,
        className,
        style,
        defaultActiveKey,
        activeKey,
        size,
        tabPosition,
        type,
        setProps,
        loading_state
    } = props;

    children = parseChildrenToArray(children)

    const tabPanes = children.map(
        (child) => {
            let childProps = resolveChildProps(child)

            const {
                id,
                className,
                style,
                tab,
                disabled,
                // closable,
                loading_state,
                ...otherProps
            } = childProps;

            return (
                <TabPane
                    id={id}
                    className={className}
                    style={style}
                    tab={tab}
                    disabled={disabled}
                    // closable={closable}
                    loading_state={loading_state}
                    {...omit(
                        ['setProps', 'persistence', 'persistence_type', 'persisted_props'],
                        otherProps
                    )}>
                    {child}
                </TabPane>
            );
        }
    )

    const orderTabPanes = tabPanes.slice().sort((a, b) => {
        const orderA = order.indexOf(a.key);
        const orderB = order.indexOf(b.key);

        if (orderA !== -1 && orderB !== -1) {
        return orderA - orderB;
        }
        if (orderA !== -1) {
        return -1;
        }
        if (orderB !== -1) {
        return 1;
        }

        const ia = tabPanes.indexOf(a);
        const ib = tabPanes.indexOf(b);

        return ia - ib;
    });

    const moveTabNode = (dragKey, hoverKey) => {
        setOrder((order) => {
            const newOrder = order.slice();
    
            children.forEach((child) => {
            if (newOrder.indexOf(child.key === -1)) {
                newOrder.push(child.key);
            }
            });
    
            const dragIndex = newOrder.indexOf(dragKey);
            const hoverIndex = newOrder.indexOf(hoverKey);
    
            newOrder.splice(dragIndex, 1);
            newOrder.splice(hoverIndex, 0, dragKey);
            return newOrder
        })
    };

    const cardTarget = {

        drop(props, monitor) {

            const dragKey = monitor.getItem().index;
            const hoverKey = props.index;
        
            if (dragKey === hoverKey) {
                return;
            }
        
            props.moveTabNode(dragKey, hoverKey);
            monitor.getItem().index = hoverKey;

        },

    };
  
    const cardSource = {

        beginDrag(props) {

            return {
                id: props.id,
                index: props.index,
            };
        },

    };

    const WrapTabNode = DropTarget('DND_NODE', cardTarget, connect => ({
        connectDropTarget: connect.dropTarget(),
    }))(
        DragSource('DND_NODE', cardSource, (connect, monitor) => ({
        connectDragSource: connect.dragSource(),
        isDragging: monitor.isDragging(),
        }))(TabNode),
    );
  
    const renderTabBar = (props, DefaultTabBar) => (
        <DefaultTabBar {...props}>
        {node => (
            <WrapTabNode key={node.key} index={node.key} moveTabNode={moveTabNode}>
            {node}
            </WrapTabNode>
        )}
        </DefaultTabBar>
    );

    const onChange = e => {
        setProps({ activeKey: e })
    }

    const onEdit = (targetKey, action) => {

        // console.log({ targetKey, action })
        setProps({ latestDeletePane: targetKey })
    }

    return (
        <DndProvider backend={HTML5Backend}>
            <Tabs id={id}
                renderTabBar={renderTabBar} 
                className={className}
                style={style}
                defaultActiveKey={defaultActiveKey}
                activeKey={activeKey}
                size={size}
                tabPosition={tabPosition}
                type={type}
                hideAdd={true}
                onChange={onChange}
                onEdit={onEdit}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }>
                {orderTabPanes}
            </Tabs>
        </DndProvider>
    );

}

AntdTabs.propTypes = {
    // id
    id: PropTypes.string,

    /**
     * The content of the tab - will only be displayed if this tab is selected
     */
    children: PropTypes.node,

    // css className
    className: PropTypes.string,

    // css inline styles
    style: PropTypes.object,

    // key
    defaultActiveKey: PropTypes.string,

    // 'top'、'left'、'right', 'bottom'
    tabPosition: PropTypes.string,

    // 'small'、'default' 'large'
    size: PropTypes.string,

    // 'line'、'card' 'editable-card' 'line'
    type: PropTypes.string,

    // key
    activeKey: PropTypes.string,

    // key
    latestDeletePane: PropTypes.string,

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

AntdTabs.defaultProps = {

};



