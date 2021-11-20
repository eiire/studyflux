import React, { useState } from 'react'
import { connect } from 'react-redux'
import Loader from '../components/Loader'
import { Link } from "react-router-dom";
import fetch from "../components/functions/fetchWithTimeOut";
import {setAuth, setUser} from "../actions";
import { csrf_token } from '../components/vars'

const Wrapper = props => {
    const [state, setState] = useState({
        navbar_open: false,
    })

    const logout = () => {
        fetch('logout_api/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrf_token
            },
        })
            .then(response => response.json())
            .then(response => {
                if (!response.error) {
                    props.setUser({})
                    props.setAuth(false)
                }
            })
    }

    const navbarClick = () => {
        setState(prev => ({...prev, navbar_open: state.navbar_open ? false : true}))
    }

    return (
        <>
            <header className="page-header">
                <Link className='logo' push to="/"> StudyFlux </Link>
                <div className="meta">
                    <div style={{color: 'white', tabSize: '10px'}}>
                        TEST
                    </div>
                </div>
                <div id="test_account" className="account">
                    {props.auth
                        ? <>
                            <a className='login' href={`/users/@${props.user.username}/`}> {props.user.username} </a>
                            <Link className='logout' push to="/" onClick={logout}> Log Out </Link>
                        </>
                        : <>
                            <Link className='login' push to="signin"> Log In </Link>
                            <Link className='signup' push to="signup"> Sign Up </Link>
                        </>
                    }
                </div>
            </header>
            <div className={state.navbar_open ? 'my_navbar my_navbar_responsive' : 'my_navbar'} id="my_navbar">
                <div className="active">
                    {props.auth
                        ? <a href={`/users/@${props.user.username}/`}> Home </a>
                        : <Link className='signup' push to="signup"> Home </Link>
                    }
                    {state.navbar_open ? <div className="icon icon_responsive" onClick={navbarClick}>☰</div> : null}
                </div>
                {props.auth
                    ? <a href={`/users/@${props.user.username}/blog`} style={state.navbar_open ? {'display':'flex'} : {'display':'none'}}> Your blog </a>
                    : <Link className='signup' push to="signup" style={state.navbar_open ? {'display':'flex'} : {'display':'none'}}> Your blog </Link>
                }
                {!state.navbar_open ? <div className="icon" onClick={navbarClick}>☰</div> : null}
            </div>
            <main>
                <div className="container">
                    <div className="row">
                        <div className="col-12 col-lg order-last order-lg-first">
                            {props.component}
                        </div>
                    </div>
                </div>
            </main>
            {props.loading && <Loader />}
        </>
    )
}

const mapStateToProps = store => {
    return {
        loading: store.loading,
        trancheHide: store.trancheHide,
        loanHide: store.loanHide,
        auth: store.auth,
        user: store.user,
    }
}

const mapDispatchToProps = dispatch => {
    return {
        setUser: user => dispatch(setUser(user)),
        setAuth: auth => dispatch(setAuth(auth)),
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Wrapper)
