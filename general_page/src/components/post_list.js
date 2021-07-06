import React, { useEffect, useState } from "react";
import { render } from "react-dom";
import { Post } from "./post";
import {csrf_token} from "../vars";

function PostList() {
    const [state, setState] = useState({
        data: [],
        loaded: false,
        next: null,
        previous: '',
        count: 0,
    })

    useEffect(() => {
        fetch("general_page_api/v1/posts/")
            .then(response => {
                if (response.status > 400)
                    setState({placeholder: "Something went wrong!"})

                return response.json();
            })
            .then(data => setState(() => {
                return {
                    data: data.results,
                    loaded: true,
                    next: data.next,
                    previous: data.previous,
                    count: data.count
                }
            }))
    }, [])

    return (
        <div>
            <div className="container" >
                {state.data.map(post => {
                    return (
                        <Post post={post} />
                    );
                })}
            </div>
            {state.next
                ? <ul className="pagination justify-content-center">
                    <li className="page-item cursor-pointer mt-5">
                        <div className="page-link" onClick={() =>
                            fetch(state.next, {
                                method: 'GET',
                                headers: {'X-CSRFToken': csrf_token},
                            }).then(response => response.json()).then(data => {
                                setState(() => {
                                    return {
                                        data: state.data.concat(data.results),
                                        loaded: true,
                                        next: data.next,
                                        previous: data.previous,
                                        count: data.count
                                    }
                                })
                            })
                        }>Next 10 post</div>
                    </li>
                </ul>
                : null
            }
        </div>
    );
}


export default PostList;

const container = document.getElementById("post_list");
render(<PostList />, container);
