import React, { Component } from 'react';
import { render } from "react-dom";

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
            <div className="row">
              <div className="col-md-7" >
                <a href={post.url}>
                  <div className="img_container">
                    <img src={post.image} alt={post.image.split('/').pop()} />
                  </div>
                </a>
              </div>
              <div className="col-md-5">
                <h3 href={post.url_post}> {post.title} </h3>
                <small>
                  <p className="card-text"> {
                    (new Date(post.created_on)).toLocaleDateString().split('/').join(' ')
                  } |&nbsp;
                    Categories:&nbsp;
                    {post.topics.map(topic => {
                      return (
                        <a href={topic.url}>
                          {topic.title}
                        </a>
                      )
                    })}
                  </p>
                </small>
                <p> {post.header} </p>
                <a className="btn btn-primary" href={post.url}> View post </a>
              </div>
            </div>
          );
        })}
      </div>
    );
  }
}


export default PostList;

const container = document.getElementById("post_list");
render(<PostList />, container);
