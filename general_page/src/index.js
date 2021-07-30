import React from 'react'
import ReactDOM from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import { rootReducer, initialState } from './reducer'
import GeneralPage from "./layouts/GeneralPage";

const store = createStore(rootReducer, initialState)

ReactDOM.render(
    <Provider store={store}>
        <GeneralPage />
    </Provider>,
    document.getElementById('general_page')
)
