import React from 'react'


const ArticleItem = ({article}) => {
    return (
        <tr>
            <td>{article.id}</td>
            <td>{article.name}</td>
            <td>{article.authors}</td>
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
                <th>AUHTORS</th>
            </tr>
            </thead>
            <tbody>
            {articles.map((article) => <ArticleItem key={article.id} article={article}/>)}
            </tbody>
        </table>
    )
}


export default ArticleList

