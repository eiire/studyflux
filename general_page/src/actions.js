export function setUser(user) {
    return {
        type: 'SET_USER',
        payload: user
    }
}

export function setAuth(auth) {
    return {
        type: 'SET_AUTH',
        payload: auth
    }
}

export function setLoading(loading) {
    return {
        type: 'SET_LOADING',
        payload: loading
    }
}

export function setSignUpStage(signup_stage) {
    return {
        type: 'SET_SIGNUP_STAGE',
        payload: signup_stage
    }
}

export function setCsrfToken(csrf_token) {
    return {
        type: 'CSRF_TOKEN',
        payload: csrf_token
    }
}
