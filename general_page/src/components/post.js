import React, {useState} from 'react';

export function Post({post}) {
    const csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').attr('value')
    const [is_fan, setIs_fan] = useState(post.is_fan)

    return post.image === null
        ? <div className="col">
            <h3 href={post.url_post}> {post.title} </h3>

            <small>
                <p className="card-text">
                    {(new Date(post.created_on)).toLocaleDateString().split('/').join(' ')}
                    |&nbsp;Categories:&nbsp;

                    {post.topics.map(topic => {
                      return <a href={topic.url}> {topic.title} </a>;
                    })}
                </p>
            </small>

            <div className="like"> Like:
                { is_fan
                    ? <div onClick={() =>
                        fetch('http://127.0.0.1:8000/like_api/v1/posts/'+ post.id + '/unlike/', {
                            method: 'POST',
                            headers: {'X-CSRFToken': csrfmiddlewaretoken},
                        }).then((data) => setIs_fan(false))
                    }> - </div>
                    : <div onClick={() =>
                        fetch('http://127.0.0.1:8000/like_api/v1/posts/'+ post.id + '/unlike/', {
                            method: 'POST',
                            headers: {'X-CSRFToken': csrfmiddlewaretoken},
                        }).then((data) => setIs_fan(true))
                    }> + </div>
                }
            </div>

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
                    <p className="card-text">
                        { (new Date(post.created_on)).toLocaleDateString().split('/').join(' ') }
                        |&nbsp;Categories:&nbsp;

                        {post.topics.map(topic => {
                            return <a href={topic.url}> {topic.title} </a>;
                        })}
                    </p>
                </small>

                <div className="like"> Like:
                    { is_fan
                        ? <div onClick={() =>
                            fetch('http://127.0.0.1:8000/like_api/v1/posts/'+ post.id + '/unlike/', {
                                method: 'POST',
                                headers: {'X-CSRFToken': csrfmiddlewaretoken},
                            }).then((data) => setIs_fan(false))
                        }> - </div>
                        : <div onClick={() =>
                            fetch('http://127.0.0.1:8000/like_api/v1/posts/'+ post.id + '/unlike/', {
                                method: 'POST',
                                headers: {'X-CSRFToken': csrfmiddlewaretoken},
                            }).then((data) => setIs_fan(true))
                        }> + </div>
                    }
                </div>

                <p> {post.header} </p>
                <a className="btn btn-primary" href={post.url}> View post </a>
            </div>
        </div>;
}
