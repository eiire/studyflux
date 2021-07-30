import React from 'react'
import Wrapper from '../layouts/Wrapper'
import PostList from "../components/Feed/PostList";

export default function Home () {
    return (
        <Wrapper component={<PostList />} />
    )
}
