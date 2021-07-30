import React, { useState } from "react";
import { connect } from 'react-redux'
import { Redirect } from 'react-router-dom'
import Registration from "../components/Auth/RegistrationForm";
import Wrapper from "../layouts/Wrapper";
import ConfirmForm from "../components/Auth/ConfirmForm";
import '../styles/login_style.css'

function SignUp({signup_stage}) {
    let component;

    switch (signup_stage) {
        case 'registration':
            component = <Registration />
            break
        case 'confirm':
            component = <ConfirmForm />
            break
        default:
            component = <Redirect to='/' />
    }

    return <Wrapper component={component} />

}

const mapStateToProps = store => {
    return {
        signup_stage: store.signup_stage
    }
}

const mapDispatchToProps = dispatch => {
    return {
        //
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(SignUp)
