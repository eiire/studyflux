import React from 'react';

const AlertText = props => {
    return (
        <div className={'text-small text-' + props.type + (props.className ? ' ' + props.className : '')}>{props.message}</div>
    );
}

export default AlertText;