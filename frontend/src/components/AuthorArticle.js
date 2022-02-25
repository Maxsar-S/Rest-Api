import React from 'react'
import {useParams} from 'react-router-dom'

const ArticleItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.author.first_name} {item.author.last_name}
            </td>
        </tr>
    )
}


const AuthorArticleList = ({articles}) => {


    let {id} = useParams();
    let filteredArticles = articles.filter((article) => article.author.id === +id)
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>AUTHOR</th>
                </tr>
            </thead>
            <tbody>
            {filteredArticles.map((article) => <ArticleItem item={article}/>)}
            </tbody>
        </table>
    )
}

export default AuthorArticleList