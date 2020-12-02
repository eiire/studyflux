import React, {useState} from 'react';
import {csrf_token} from '../vars'

export function Like({post}) {
    const [is_fan, setIs_fan] = useState(post.is_fan)

    return (
        <div className="like">
            {is_fan
                ? <div onClick={() =>
                    fetch('http://127.0.0.1:8000/like_api/v1/posts/' + post.id + '/unlike/', {
                        method: 'POST',
                        headers: {'X-CSRFToken': csrf_token},
                    }).then((response) => response.ok ? setIs_fan(false) : setIs_fan(true))
                }> - </div>
                : <div onClick={() =>
                    fetch('http://127.0.0.1:8000/like_api/v1/posts/' + post.id + '/like/', {
                        method: 'POST',
                        headers: {'X-CSRFToken': csrf_token},
                    }).then((response) => response.ok ? setIs_fan(true) : setIs_fan(false))
                }> + </div>
            }
        </div>
    )
}
