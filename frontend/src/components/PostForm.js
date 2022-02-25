import React from "react";



class PostForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            author: 0,
            article:0,
            text:"",
        }
    }


    handlerOnChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handlerOnSubmit(event) {
        event.preventDefault();
        this.props.postCreate(this.state.name, this.state.author, this.state.article, this.state.text);
    }


    render() {
        return (
            <form onSubmit={(event) => this.handlerOnSubmit(event)}>
                <input type="text" name="name"
                        value={this.state.name}
                        onChange={(event) => this.handlerOnChange(event)}/>
                <select name="author"
                        onChange={(event) => this.handlerOnChange(event)}>
                {this.props.users.map((user) => (
                        <option value={user.id} key={user.id}>
                            {user.first_name} {user.last_name}
                        </option>
                ))}
                </select>
                <select name="article"
                        onChange={(event) => this.handlerOnChange(event)}>
                {this.props.articles.map((article) => (
                        <option value={article.id} key={article.id}>
                            {article.name}
                        </option>
                ))}
                </select>
                <input type="text" name="text"
                        value={this.state.text}
                        onChange={(event) => this.handlerOnChange(event)}/>
                <input type="submit" name="create"/>
            </form>
        )
    }

}


export default PostForm