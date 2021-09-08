import './App.css';
import React from "react";
import UserList from "./components/Users";
import ArticleList from "./components/Articles";
import AuthorArticleList from './components/AuthorArticle'
import PostList from "./components/Posts";
import axios from 'axios';
import {BrowserRouter, Route, Link, Switch, Redirect} from "react-router-dom";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

const API_ROOT = 'http://127.0.0.1:8000/api'
const get_url = (url_name) => `${API_ROOT}${url_name}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'articles': [],
            'posts': [],
        }
    }

    componentDidMount() {
        axios.all(
            [
                axios.get(get_url('users')),
                axios.get(get_url('articles')),
                axios.get(get_url('posts')),
            ]

        )
            .then(axios.spread((users, articles, posts)=>{
                this.setState(
                    {
                        'users': users.data.results,
                        'articles': articles.data.results,
                        'posts': posts.data.results
                    }
                )
            }))
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/articles'>Articles</Link>
                            </li>
                            <li>
                                <Link to='/posts'>Posts</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/articles' component={() => <ArticleList articles={this.state.articles}/>}/>
                        <Route path='/posts' component={() => <PostList posts={this.state.posts}/>}/>
                        <Route path='/user/:id' component={() => <AuthorArticleList articles={this.state.articles}/>}/>
                        <Redirect from='/users' to='/'/>
                        <Route component={{NotFound404}}/>
                    </Switch>
                </BrowserRouter>
            </div>

        )
    }
}


export default App;
