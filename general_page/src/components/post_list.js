import React, { useState} from 'react';
import { render } from "react-dom";
import { Post } from "./post";

function PostList() {
    const [state, setState] = useState({
        data: [],
        loaded: false
    })

    fetch("general_page_api/v1/posts/")
        .then(response => {
          if (response.status > 400)
              setState({ placeholder: "Something went wrong!" })

          return response.json();
        })
        .then(data => setState({
            data,
            loaded: true
        }));

    return (
        <div className="container" >
            {state.data.map(post => {
                return (
                    <Post post={post} />
                );
            })}
        </div>
    );
}


export default PostList;

const container = document.getElementById("post_list");
render(<PostList />, container);
