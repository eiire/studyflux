export const initialState = {
    api: {
        url: ''
    },
    auth: false,
    user: {},
    signup_stage: 'registration',
    loading: false,
    csrf_token: ''
}

export function rootReducer(state = initialState, action) {
    switch (action.type) {
        case 'SET_AUTH':
            return {...state, auth: action.payload}
        case 'SET_LOADING':
            return {...state, loading: action.payload}
        case 'SET_USER':
            return {...state, user: action.payload}
        case 'SET_SIGNUP_STAGE':
            return {...state, signup_stage: action.payload}
        default:
            return state
    }
}
