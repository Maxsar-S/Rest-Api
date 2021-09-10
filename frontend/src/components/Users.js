import React from "react";
import {Link} from 'react-router-dom'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`user/${user.id}`}>
                    {user.username}
                </Link>
            </td>
            <td>
                <Link to={`user/${user.id}`}>
                    {user.first_name}
                </Link>
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Username</th>
                <th>First_Name</th>
                <th>Last_Name</th>
                <th>Email</th>
            </tr>
            </thead>
            <tbody>
            {users.map((user) => <UserItem user={user}/>)}
            </tbody>
        </table>
    )
}

export default UserList;