import React from "react";



class ArticleForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            author: 0,
        }
    }


    handlerOnChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handlerOnSubmit(event) {
        event.preventDefault();
        this.props.articleCreate(this.state.name, this.state.author);
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
                <input type="submit" name="create"/>
            </form>

        )
    }

}


export default ArticleForm