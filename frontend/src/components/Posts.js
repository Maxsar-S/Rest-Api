import React from 'react'


const PostItem = ({post}) => {
    return (
        <tr>
            <td>{post.id}</td>
            <td>{post.name}</td>
            <td>{post.article}</td>
            <td>{post.text}</td>
            <td>{post.author.first_name}</td>
            <td>{post.created_at}</td>
            <td>{post.updated_at}</td>
        </tr>
    )
}


const PostList = ({posts}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>ARTICLE</th>
                <th>TEXT</th>
                <th>AUHTOR</th>
                <th>CREATED</th>
                <th>UPDATED</th>
            </tr>
            </thead>
            <tbody>
            {posts.map((post) => <PostItem key={post.id} post={post}/>)}
            </tbody>
        </table>
    )
}


export default PostList