import React, { useEffect, useState } from 'react';
import { Like } from "./Like";
import { connect } from "react-redux";

function Post({post, auth}) {
    const [state, setState] = useState({
        img: true,
    });

     useEffect(() => {
        fetch(post.image)
            .then(response => {
                if (response.status > 400)
                    setState({img: false})

                return response.json();
            })
    }, [])

    return (
         <div className="row">
            <div className="col-md-7" >
                <a href={state.img ? post.image : '/static/img/noimg.jpg'}>
                    <div className="img_container"> <img src={state.img ? post.image : '/static/img/noimg.jpg'} /> </div>
                </a>
            </div>

            <div className="col-md-5">
                <div className="row d-flex justify-content-between align-items-center mt-5 mb-5">
                    <div className="col-auto">
                        <h3 href={post.url_post}> {post.title} </h3>
                    </div>
                    <div className="col-auto">
                        <span class="text-lighten"> is an article written by </span> <a href={post.user_url}> {post.username} </a>
                    </div>
                </div>
                <small>
                    <p className="card-text">
                        { (new Date(post.created_on)).toLocaleDateString().split('/').join(' ') }
                        |&nbsp;Categories:&nbsp;

                        {post.topics.map(topic => {
                            return <a href={topic.url}> {topic.title} </a>;
                        })}
                    </p>
                </small>

               <p> {post.header} </p>
               <div class="row d-flex justify-content-between align-items-center mt-5">
                   <div class="col-auto">
                       <a className="btn btn-primary" href={post.url}> View post </a>
                   </div>
                   <div className="col-auto">
                       {auth ? <Like post={post}/> : undefined}
                   </div>
               </div>
            </div>
        </div>
    )
}

const mapStateToProps = store => {
    return {
        auth: store.auth
    }
}

export default connect(
    mapStateToProps,
)(Post)
