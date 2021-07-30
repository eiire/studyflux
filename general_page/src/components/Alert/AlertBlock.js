import React from 'react'

const AlertBlock = props => {
    return (
        <div className={'alert alert-' + props.type + (props.className ? ' ' + props.className : '')}>{props.message}</div>
    );
}

export default AlertBlock