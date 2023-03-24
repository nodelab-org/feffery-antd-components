import React, { useState, useEffect } from "react";
import { Tabs } from 'antd';

import { isNil } from 'ramda';
import 'antd/dist/antd.css';
// import { DndProvider, DragSource, DropTarget } from 'react-dnd';
// import { HTML5Backend } from 'react-dnd-html5-backend';
import PropTypes from "prop-types";
// import { triggerFocus } from "antd/lib/input/Input";
import { ApartmentOutlined, NodeIndexOutlined } from '@ant-design/icons';

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


const renderTabPane = (child, n_tabs, forceRender) => {
    
    const childProps = resolveChildProps(child) 

    const {
        children,
        className,
        id,
        tabTitle,
        icon,
        style,
        // key,
        disabled,
        closable,
        loading_state,
        persisted_props,
        persistence,
        persistence_type,
        setProps
        // ...otherProps
    } = childProps;
    
    // const styledTabTitle = <pre style={tabTitleStyle}>{tabTitle}</pre>

    return (
        <TabPane
            className={className}
            closable={n_tabs > 1? true : false}
            // closable={true}
            disabled={disabled}
            forceRender={forceRender}
            id={id}
            key={id}
            loading_state={loading_state}
            style={style}
            // tab={tabTitle}>
            tab={icon === "schema"
                ? <span> <ApartmentOutlined /> {tabTitle}</span>
                : icon === "data"
                    ? <span> <NodeIndexOutlined /> {tabTitle}</span>
                    : tabTitle
            }>
            {child}
        </TabPane>
    )

}


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
    // const [order, setOrder] = useState(children.map(child=>child.key))
    let tabPanesRender = children 
        ? children.map((tp, index) => renderTabPane(
            tp,
            children.length,
            // props.tabLength,
            props.forceRender
            ))
        : []
    let activeKey = props.activeKey
        ? props.activeKey
        : props.defaultActiveKey;
    
    useEffect(() => {

        setTabsDisabled((dsbld) => props.disabled === true || props.disabled === "true")

    }, [props.disabled])

    // console.log("tabPanesRender initialised")
    // console.log(tabPanesRender)

    // const moveTabNode = (dragKey, hoverKey) => {
        
    //     if (order && order.length) {

    //         setOrder((o) => {

    //             const newOrder = o.slice();

    //             props.children.forEach((tp) => {
    //             if (newOrder.indexOf(tp.key) === -1) {
    //                 newOrder.push(tp.key);
    //             }
    //             });
    
    //             const dragIndex = newOrder.indexOf(dragKey);
    //             const hoverIndex = newOrder.indexOf(hoverKey);
    
    //             newOrder.splice(dragIndex, 1);
    //             newOrder.splice(hoverIndex, 0, dragKey);

    //             return newOrder
    
    //         });

    //         console.log("order after moveTabNode setOrder")
    //         console.log(order)
    //     }
    // };

    {/* <WrapTabNode key={node.key} index={node.key} moveTabNode={moveTabNode}> */}
    // const renderTabBar = (prps, DefaultTabBar) => (
    //     <DefaultTabBar {...prps}>
    //     {node => (
    //         node
    //     )}
    //     </DefaultTabBar>
    // );

    const onChange = aKey => {

        if (!tabsDisabled) {

            console.log("onChange callback fired")
            props.setProps({ 
                // "previousActiveKey" : props.activeKey,
                "activeKey" : aKey,
                // "trigger" : "change"
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
                
                // let lastIndex;
    
                // tabPanesRender.forEach((tp, i) => {
                    
                //     if (tp.key === props.targetKey) {
    
                //         lastIndex = i - 1;
                    
                //     }
    
                // }); 
    
                // props.setProps({"activeKey" : lastIndex})
                
            } else if (action === "add") {
    
                props.setProps({
                    "nClicksAdd": props.nClicksAdd + 1,
                    // "trigger": "add"
                });
                // props.setProps({"activeKey" : lastIndex})
    
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
    // if (tabPanesRender && tabPanesRender.length && tabPanesRender.length < order.length) {
        
    //     // child removed
    //     console.log("child removed")

    // let lastIndex;

    // tabPanesRender.forEach((tp, i) => {
        
    //     if (tp.key === props.targetKey) {

    //         lastIndex = i - 1;
        
    //     }

    // }); 

        // setOrder((ordr) => {ordr.filter((key) => key !== props.targetKey)});

        // console.log("order after child removed setOrder")
        // console.log(order)

    //     if (tabPanesRender.length && activeKey === String(props.targetKey)) {

    //         if (lastIndex >= 0) {
    
    //             activeKey = tabPanesRender[lastIndex].key;
    
    //         } else {
    
    //             activeKey = tabPanesRender[0].key;
    
    //         }
    //     }
    // }

    // if (tabPanesRender && order && tabPanesRender.length && tabPanesRender.length > order.length) {
        
    //     // child added 
    //     console.log("children added")

    //     const newTabPanes = tabPanesRender.slice(order.length,tabPanesRender.length)

    //     console.log("newTabPanes")
    //     console.log(newTabPanes)

    //     setOrder((ordr) => {

    //         newTabPanes.map((newTp)=>ordr.push(newTp.key))
    //         return ordr

    //     })
        

    //     console.log("order after child added setOrder")
    //     console.log(order)

    //     activeKey = newTabPanes[newTabPanes.length-1].key
    // }


    // if (order && tabPanesRender && tabPanesRender.length>1){

    //     tabPanesRender = tabPanesRender.sort((a, b) => {

    //         const orderA = order.indexOf(a.key);
    //         const orderB = order.indexOf(b.key);

    //         if (orderA !== -1 && orderB !== -1) {
    //             return orderA - orderB;
    //         }
    //         if (orderA !== -1) {
    //             return -1;
    //         }
    //         if (orderB !== -1) {
    //             return 1;
    //         }

    //         const ia = tabPanesRender.indexOf(a);
    //         const ib = tabPanesRender.indexOf(b);

    //         return ia - ib;

    //     })

    // }

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
                {tabPanesRender}
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

    targetKey: PropTypes.string,
    // latestDeletePane: PropTypes.string,


    /**
     * Used to make it easy in Dash application to detect whether nClicksAadd, nClicksRemove or changing active tab caused component to update
     */
    // trigger: PropTypes.string

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



