import React, { useState, useEffect } from "react";
import { Tabs } from 'antd';
// import { isNil, none } from 'ramda';
import 'antd/dist/antd.css';
import PropTypes from "prop-types";

// coerce children to array if not already
const parseChildrenToArray = (children) => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};
// Drag & Drop node
// const TabNode = (prps) => {
//     const { connectDragSource, connectDropTarget, children } = prps;
//     return (
//         connectDragSource(connectDropTarget(children))
//     )
// };


// const cardTarget = {

//     drop(props, monitor) {

//         const dragKey = monitor.getItem().index;
//         const hoverKey = props.index;
    
//         if (dragKey === hoverKey) {
//             return;
//         }
    
//         props.moveTabNode(dragKey, hoverKey);
//         monitor.getItem().index = hoverKey;

//     },

// };


// const cardSource = {

//     beginDrag(props) {

//         return {
//             id: props.id,
//             index: props.index,
//         };
//     },

// };


// const WrapTabNode = DropTarget('DND_NODE', cardTarget, connect => ({

//     connectDropTarget: connect.dropTarget(),

// }))(

//     DragSource('DND_NODE', cardSource, (connect, monitor) => ({

//     connectDragSource: connect.dragSource(),
//     isDragging: monitor.isDragging(),

//     }))(TabNode),

// );


export default function AntdTabs (props) {
    
    const children = parseChildrenToArray(props.children)
    const [tabsDisabled, setTabsDisabled] = useState(props.disabled)

    let activeKey = props.activeKey
        ? props.activeKey
        : props.defaultActiveKey;
    
    useEffect(() => {

        setTabsDisabled((_dsbld) => props.disabled === true || props.disabled === "true")

    }, [props.disabled])

    const onChange = aKey => {

        if (!tabsDisabled) {

            console.log("onChange callback fired")
            props.setProps({ 
                "activeKey" : aKey,
            })

        }

    };

    const onEdit = (targetKey, action) => {
        
        if (!tabsDisabled) {

            console.log("onEdit callback fired")

            if (action === "remove") {
    
                props.setProps({
                    "nClicksRemove": props.nClicksRemove + 1,
                    // "trigger": "remove",
                    "targetKey":targetKey})

                
            } else if (action === "add") {
    
                props.setProps({
                    "nClicksAdd": props.nClicksAdd + 1,
                    // "trigger": "add"
                });

            }

        }

    }

    const onTabClick = (key, event) => {
        
        // executed when active tab is clicked

        if (key === props.activeKey && !tabsDisabled) {
            
            console.log("increment nTabClicks!")

            props.setProps({
                "nTabClicks": props.nTabClicks + 1,
                // "trigger": "add"
            });

        }

    }
  
    return (
        // <DndProvider backend={HTML5Backend}>
            <Tabs 
                id={props.id}
                animated={props.animated}
                // renderTabBar={renderTabBar} 
                className={props.className}
                style={props.style}
                defaultActiveKey={props.defaultActiveKey}
                activeKey={activeKey}
                size={props.size}
                tabPosition={props.tabPosition}
                type={"editable-card"}
                hideAdd={false}
                onChange={onChange}
                onEdit={onEdit}
                onTabClick={onTabClick}
                data-dash-is-loading={
                    (props.loading_state && props.loading_state.is_loading) || undefined
                }>
                {children}
            </Tabs>
        // </DndProvider>
    );
    
}

AntdTabs.propTypes = {
    
    /**
     * whether to animate change of tab
     */
    animated: PropTypes.bool,

    // key. readonly
    activeKey: PropTypes.string,
    
    /**
     * tab children, i.e. contents
     */
    children: PropTypes.node,
    
    // css className
    className: PropTypes.string,
    
    // default active key
    defaultActiveKey: PropTypes.string,
    
    disabled: PropTypes.bool,

    forceRender: PropTypes.bool,

    // component id
    id: PropTypes.string,
    
    /**
     * number of times add button has been clicked
     */
    nClicksAdd: PropTypes.number,
    
    /**
     * number of times add button has been clicked
     */
    nClicksRemove: PropTypes.number,

    /**
     * number of times add button has been clicked
     */
    nTabClicks: PropTypes.number,

    /**
     * new tab to add on click
     */
    // newTab: PropTypes.node,

    // previousActiveKey: PropTypes.string,

    // css inline styles
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

    // 'small'、'default' 'large'
    size: PropTypes.string,

    // 'top'、'left'、'right', 'bottom'
    tabPosition: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    targetKey: PropTypes.string
    // latestDeletePane: PropTypes.string,

};

AntdTabs.defaultProps = {
    animated: false,
    activeKey:"0",  
    forceRender: false,
    defaultActiveKey:"0",  
    disabled: false,
    nClicksAdd:0,
    nClicksRemove:0,
    nTabClicks:0,
    size:"small"
};



