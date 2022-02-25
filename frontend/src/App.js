import './App.css';
import React from "react";

import UserList from "./components/Users";
import ArticleList from "./components/Articles";
import AuthorArticleList from './components/AuthorArticle';
import ArticleForm from './components/ArticleForm';
import PostForm from "./components/PostForm";
import PostList from "./components/Posts";
import ArticlePostList from "./components/ArticlePost";
import SearchArticle from "./components/SeacrhBar";

import axios from 'axios';
import {BrowserRouter, Route, Link, Switch, Redirect} from "react-router-dom";
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

const DOMAIN = 'http://127.0.0.1:8000/api'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'articles': [],
            'article': {},
            'posts': [],
            'search_articles': {}
        }
    }

    logout() {
        this.setToken('');
    }

    getToken(username, password) {
        axios.post(
            'http://127.0.0.1:8000/api-token-auth/',
            {username: username, password: password}
        ).then(response => {
            this.setToken(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    getTokenFromStorage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.loadData())
    }

    setToken(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.loadData())
    }


    loadData() {
        if (!this.isAuthenticated()) {
            return;
        }
        const headers = this.getHeaders()
        axios.get(get_url('/users/'), {headers})
            .then(response => {
                this.setState({users: response.data.results})
            })
            .catch(error => console.log(error))

        axios.get(get_url('/articles/'), {headers})
            .then(response => {
                this.setState({articles: response.data.results})
            })
            .catch(error => {
                console.log(error)
                this.setState({articles: []})
            })
        axios.get(get_url('/posts/'), {headers})
            .then(response => {
                this.setState({posts: response.data.results})
            })
            .catch(error => {
                console.log(error)
                this.setState({posts: []})
            })
    }


    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.isAuthenticated()) {
            headers['Authorization'] = `Token ${this.state.token}`;
        }
        return headers
    }


    isAuthenticated() {
        return this.state.token !== '';
    }


    componentDidMount() {
        this.getTokenFromStorage();
    }


    articleDelete(id) {
        const headers = this.getHeaders();
        axios
            .delete(get_url(`/articles/${id}/`), {headers})
            .then(result => {
                this.setState({
                    articles: this.state.articles.filter((item) => item.item.id !== id)
                })
            })
            .catch(error => console.log(error))
    }


    articleCreate(name, author) {
        const headers = this.getHeaders();
        axios
            .post(get_url('/articles/'),
                {name: name, author: author},
                {headers})
            .then(result => {
                const newArticle = result.data;
                this.setState({
                    articles: [...this.state.articles, newArticle]
                })
            })
            .catch(error => console.log(error))
    }


    articleSearch(search_name) {
        return (this.state.articles.filter((item) => item.name.includes(search_name)))
    }


    postDelete(id) {
        const headers = this.getHeaders();
        axios
            .delete(get_url(`/posts/${id}/`), {headers})
            .then(result => {
                this.setState({
                    articles: this.state.posts.filter((item) => item.item.id !== id)
                })
            })
            .catch(error => console.log(error))
    }


    postCreate(name, author, article, text) {
        const headers = this.getHeaders();
        axios
            .post(get_url('/posts/'),
                {name: name, author: author, article: article, text: text},
                {headers})
            .then(result => {
                const newPost = result.data;
                this.setState({
                    posts: [...this.state.posts, newPost]
                })
            })
            .catch(error => console.log(error))
    }


    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to={'/'}>Users</Link>
                            </li>
                            <li>
                                <Link to={'/articles'}>Articles</Link>
                            </li>
                            <li>
                                <Link to={'/posts'}>Posts</Link>
                            </li>
                            <li>
                                {this.isAuthenticated() ?
                                    <button onClick={() => this.logout()}>
                                        Logout
                                    </button> :
                                    <Link to={'/login'}>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path={'/'} component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path={'/articles'}>
                            <ArticleList articles={this.state.articles} articleDelete={(id) =>
                                this.articleDelete(id)}/>
                        </Route>
                        <Route exact path={'/articles/create'} component={() => <ArticleForm
                            articleCreate={(name, author) =>
                                this.articleCreate(name, author)} users={this.state.users}/>
                        }/>
                        <Route path={'/user/:id'} component={() =>
                            <AuthorArticleList articles={this.state.articles}/>}/>
                        <Route exact path={'/articles/search'} component={() =>
                            <SearchArticle articleSearch={(search_name) => this.articleSearch(search_name)}/>}/>

                        <Route path={'/posts'} component={() =>
                            <PostList posts={this.state.posts} postDelete={(id) =>
                                this.postDelete(id)}/>}/>

                        <Route exact path={'/posts/create'} component={() => <PostForm
                            postCreate={(name, author, article, text) =>
                                this.postCreate(name, author, article, text)} users={this.state.users}
                            articles={this.state.articles}/>
                        }/>

                        <Route path={'/article/:id'} component={() =>
                            <ArticlePostList posts={this.state.posts}/>}/>

                        <Route path={'/login/'}>
                            <LoginForm getToken={(username, password) => this.getToken(username, password)}/>
                        </Route>
                        <Redirect from='/users' to='/'/>
                        <Route component={{NotFound404}}/>
                    </Switch>
                </BrowserRouter>
            </div>

        )
    }
}


export default App;
