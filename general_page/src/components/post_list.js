import React, { Component } from 'react';
import { render } from "react-dom";
import { Post } from "./post";

class PostList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("general_page_api/v1/posts/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <div className="container" >
        {this.state.data.map(post => {
          return (
            <Post post={post} />
          );
        })}
      </div>
    );
  }
}


export default PostList;

const container = document.getElementById("post_list");
render(<PostList />, container);
