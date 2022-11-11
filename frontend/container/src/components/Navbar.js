import React, { useState, useEffect, useContext } from 'react'
import { Link } from 'react-router-dom'
import './Navbar.css'
import { UserContext } from '../UserContext'
import SignedOutMenu from './SignOutMenu';
import SignedInMenu from './SignInMenu';
import logo_web from "../assets/logoweb.png";

const Navbar = () => {
    // const socket = useContext(SocketContext)
    const { user, setUser } = useContext(UserContext);

    const logout = async () => {
        try {
            // const res = await axiosInstance.get('/logout', { withCredentials: true });
            // const data = res.data;
            // console.log('logout data', data);
            localStorage.clear()
            setUser(null);
            // socket.emit('leave-rooms')
        } catch (error) {
            console.log(error)
        }
    }

    const menu = user
        ? <SignedInMenu logout={logout}/>
        : <SignedOutMenu/>

    return (
        <nav>
            <div className="nav-wrapper">
                <Link to="/" className="brand-logo">
                    <img src={logo_web} className="logo-web" />
                </Link>
                {menu}
            </div>
        </nav>
    )
}

export default Navbar 