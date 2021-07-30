import React, { useEffect, useState } from "react";
import Post from "./Post";
import { csrf_token } from "../vars";
import { connect } from 'react-redux'
import { setLoading } from "../../actions";
import fetch from '../functions/fetchWithTimeout'
import '../../styles/general_page.css'

function PostList({setLoading}) {
    const [state, setState] = useState({
        data: [],
        loaded: false,
        next: null,
        previous: '',
        count: 0,
    })

    useEffect(() => {
        setLoading(true)

        fetch('general_page_api/v1/posts/')
            .then(response => {
                if (response.status > 400)
                    setState({placeholder: 'Something went wrong!'})

                return response.json();
            })
            .then(data => setState(() => {
                setLoading(false)

                return {
                    data: data.results,
                    loaded: true,
                    next: data.next,
                    previous: data.previous,
                    count: data.count
                }
            }))
            .catch(err => {
                setLoading(false)
                setState((prev) => ({...prev, placeholder: 'Timeout expired'}))
            })
    }, [])

    return (
        <React.Fragment>
            {state.data.map(post => {
                return (
                    <Post key={post.id} post={post} />
                );
            })}

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
        </React.Fragment>
    );
}

const mapStateToProps = store => {
    return {
        //
    }
}

const mapDispatchToProps = dispatch => {
    return {
        setLoading: loading => dispatch(setLoading(loading)),
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PostList)
