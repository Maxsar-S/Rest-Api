import React from 'react'
import {Link} from "react-router-dom";


const ArticleItem = ({article}) => {
    return (
        <tr>
            <td>{article.id}</td>
            <td>
                <Link to={`article/${article.id}`}>
                {article.name}
                </Link>
            </td>
            <td>
                <Link to={`user/${article.author.id}`}>
                    {article.author.first_name} {article.author.last_name}
                </Link>
            </td>
        </tr>
    )
}


const ArticleList = ({articles}) => {
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
            {articles.map((article) => <ArticleItem key={article.id} article={article}/>)}
            </tbody>
        </table>
    )
}


export default ArticleList

