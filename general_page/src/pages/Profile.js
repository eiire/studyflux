import React from 'react'
import Wrapper from '../layouts/Wrapper'
import UserProfile from '../components/User/UserProfile'

function Profile () {
    return (
        <Wrapper component={<UserProfile />} />
    )
}

export default Profile
