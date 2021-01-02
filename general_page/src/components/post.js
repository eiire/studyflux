import React from 'react';
import {Like} from "./like";
import {is_auth} from '../vars'

export function Post({post}) {
    return post.image === null
        ? <div className="col">
            <h3 href={post.url_post}> {post.title} </h3>

            <small>
                <h5 className="card-text text-right">
                    <a href={post.user_url} style={{color:'#af6800'}}> {post.username} </a>
                </h5>

                <p className="card-text">
                    {(new Date(post.created_on)).toLocaleDateString().split('/').join(' ')}
                    |&nbsp;Categories:&nbsp;

                    {post.topics.map(topic => {
                      return <a href={topic.url}> {topic.title} </a>;
                    })}
                </p>
            </small>

            {is_auth ? <Like post={post}/> : undefined}

            <p> {post.header} </p>
            <a className="btn btn-primary" href={post.url}> View post </a>
        </div>
        : <div className="row">
            <div className="col-md-7" >
                <a href={post.url}>
                    <div className="img_container"> <img src={post.image} alt={post.image.split('/').pop()} /> </div>
                </a>
            </div>

            <div className="col-md-5">
                <h3 href={post.url_post}> {post.title} </h3>

                <small>
                    <h5 className="card-text text-right">
                        <a href={post.user_url}> {post.username} </a>
                    </h5>

                    <p className="card-text">
                        { (new Date(post.created_on)).toLocaleDateString().split('/').join(' ') }
                        |&nbsp;Categories:&nbsp;

                        {post.topics.map(topic => {
                            return <a href={topic.url}> {topic.title} </a>;
                        })}
                    </p>
                </small>

                {is_auth ? <Like post={post}/> : undefined}

                <p> {post.header} </p>
                <a className="btn btn-primary" href={post.url}> View post </a>
            </div>
        </div>;
}
