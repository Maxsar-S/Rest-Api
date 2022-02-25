import React from 'react'
import {Link} from 'react-router-dom'


class SearchArticle extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            search_name: "",
            article: {},
        }
    }


    handlerOnChange(event) {
        console.log(event.target);
        this.setState({
            [event.target.name]: event.target.value
        })
    }


    handlerOnSubmit(event) {
        event.preventDefault();
        this.setState((state) => {
            return {
                article: this.props.articleSearch(this.state.search_name)
            }
        })

    }


    ArticleItem({item}) {
        return (
            <tr>
                <td>
                    {item.id}
                </td>
                <td>
                    {item.name}
                </td>
                <td>
                    <Link to={`user/${item.author.id}`}>
                        {item.author.first_name} {item.author.last_name}
                    </Link>
                </td>
            </tr>
        )
    }


    render() {

        let search_article = Object.values(this.state.article)
        return (
            <div>
                <form onSubmit={(event) => this.handlerOnSubmit(event)}>
                    <input type="text" name="search_name"
                           onChange={(event) => this.handlerOnChange(event)}/>
                    <input type="submit" name="search_name"/>
                </form>

                <table>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>NAME</th>
                        <th>AUTHOR</th>
                    </tr>
                    </thead>
                    <tbody>
                    {search_article.map((article) => <this.ArticleItem item={article}/>)}
                    </tbody>
                </table>
            </div>
        )
    }


}

export default SearchArticle