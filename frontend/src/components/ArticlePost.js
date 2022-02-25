import React from 'react'
import {useParams} from 'react-router-dom'

const PostItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.article.name}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.author.first_name} {item.author.last_name}
            </td>
        </tr>
    )
}


const ArticlePostList = ({posts}) => {


    let {id} = useParams();
    let filteredPosts = posts.filter((post) => post.id === +id)
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>ARTICLE</th>
                    <th>TEXT</th>
                    <th>AUTHOR</th>
                </tr>
            </thead>
            <tbody>
            {filteredPosts.map((post) => <PostItem item={post}/>)}
            </tbody>
        </table>
    )
}

export default ArticlePostList