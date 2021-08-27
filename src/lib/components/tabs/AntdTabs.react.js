import React, {useState} from "react";
import { Tabs } from 'antd';

import { isNil, omit } from 'ramda';
import 'antd/dist/antd.css';
import { DndProvider, DragSource, DropTarget } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import PropTypes from "prop-types";
import { triggerFocus } from "antd/lib/input/Input";


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


const renderTabPanes = (tabPanes) => {

    return tabPanes.map((tp) => {
    
        let childProps = resolveChildProps(tp) 

        const {
            id,
            className,
            style,
            tab,
            key,
            disabled,
            closable,
            loading_state,
            setProps,
            persistence,
            persistence_type,
            persisted_props,
            children,
            ...otherProps
        } = childProps;

            
        return (
            <TabPane
                id={id}
                className={className}
                style={style}
                tab={tab}
                key={key}
                disabled={disabled}
                closable={tabPanes.length > 1? true : false}
                loading_state={loading_state}>
                {/* {...otherProps} */}
                {tp}
            </TabPane>
        );
    // })
    });
}

// Drag & Drop node
function TabNode (props) {
    const { connectDragSource, connectDropTarget, children } = props;
    return (
        connectDragSource(connectDropTarget(children))
    )
}

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

export default function AntdTabs (props) {

    const [tabPanes, setTabPanes] = useState([])
    const [order, setOrder] = useState([])


    const moveTabNode = (dragKey, hoverKey) => {
        
        if (tabPanes) {

            setOrder((ordr) => {
      
                const newOrder = ordr.slice();
       
                tabPanes.forEach((tp) => {
                if (newOrder.indexOf(tp.key) === -1) {
                    newOrder.push(tp.key);
                }
                });
    
                const dragIndex = newOrder.indexOf(dragKey);
                const hoverIndex = newOrder.indexOf(hoverKey);
    
                newOrder.splice(dragIndex, 1);
                newOrder.splice(hoverIndex, 0, dragKey);

                return newOrder
    
            });
        }
    };

    const renderTabBar = (props, DefaultTabBar) => (
        <DefaultTabBar {...props}>
        {node => (
            <WrapTabNode key={node.key} index={node.key} moveTabNode={moveTabNode}>
            {node}
            </WrapTabNode>
        )}
        </DefaultTabBar>
    );

    const remove = targetKey => {

        let newActiveKey = props.activeKey;
        let lastIndex;
        
        console.log("remove fired")

        setTabPanes((tps)=>{

            console.log("setTabPanes fired")

            console.log("targetKey")
            console.log(targetKey)

            console.log("old tabPanes")
            console.log(tps)

            tps.forEach((tp, i) => {
                if (tp.key === targetKey) {
                    lastIndex = i - 1;
                }
            });

            const newTabPanes = tps.filter(tp => tp.key !== targetKey);
            
            console.log("newTabPanes")
            console.log(newTabPanes)

            if (newTabPanes.length && newActiveKey === String(targetKey)) {

                if (lastIndex >= 0) {

                    newActiveKey = newTabPanes[lastIndex].key;

                } else {

                    newActiveKey = newTabPanes[0].key;

                }
            }
            
            props.setProps({"activeKey":newActiveKey})
            
            // console.log(childrenArray)
            // props.setProps({"children":childrenArray})
            return newTabPanes

        })
        // props.setProps({"activeKey":newActiveKey})
        
    };  

    const onChange = activeKey => {

        props.setProps({ activeKey: activeKey })
        props.setProps({"children":[]})

    };

    
    const onEdit = (targetKey, action) => {

        if (action === "remove") {

            remove(targetKey);
        }

        // props.setProps({ latestDeletePane: targetKey })
        // props.setProps({children:childrenArray})
    };
    

    if (props.children) {

        const child = Array.isArray(props.children)
            ? props.children[0] 
            : props.children 

        if (!tabPanes.map((tp) => {return tp.key}).includes(child.key)) {

            setTabPanes((tps) => {

                tps.push(child)
                return tps
    
            });
    
            setOrder((ordr) => {
    
                ordr.push(child.key)
                return ordr
    
            })

        }

    }

    // if (tabPanes.length>1){

    //     setTabPanes((tabPanes) => {

    //         return tabPanes.sort((a, b) => {

    //             const orderA = order.indexOf(a.key);
    //             const orderB = order.indexOf(b.key);

    //             if (orderA !== -1 && orderB !== -1) {
    //                 return orderA - orderB;
    //             }
    //             if (orderA !== -1) {
    //                 return -1;
    //             }
    //             if (orderB !== -1) {
    //                 return 1;
    //             }

    //             const ia = tabPanes.indexOf(a);
    //             const ib = tabPanes.indexOf(b);

    //             return ia - ib;

    //         });

    //     })

    // }
    let tabPanesRender = renderTabPanes(tabPanes)
    
    if (tabPanesRender.length>1) {
        
        tabPanesRender = tabPanesRender.sort((a, b) => {

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
    
        })

    }
    
    return (
        <DndProvider backend={HTML5Backend}>
            <Tabs 
                id={props.id}
                renderTabBar={renderTabBar} 
                className={props.className}
                style={props.style}
                defaultActiveKey={props.defaultActiveKey}
                activeKey={props.activeKey}
                size={props.size}
                tabPosition={props.tabPosition}
                type={"editable-card"}
                hideAdd={true}
                onChange={onChange}
                onEdit={onEdit}
                data-dash-is-loading={
                    (props.loading_state && props.loading_state.is_loading) || undefined
                }>
                {tabPanesRender}
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
    // children: PropTypes.node,
    /**
     * New tab to add 
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

    // key. readonly
    activeKey: PropTypes.string,

    // key
    // latestDeletePane: PropTypes.string,

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
    defaultActiveKey:"0",  
};



