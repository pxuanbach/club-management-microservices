import React from 'react';
import { NavLink } from 'react-router-dom';
import logo_web from "../assets/logoweb.png";
import Avatar from '@mui/material/Avatar';
const Header = () => (
  <div style={{width: "50px",position: "relative", height: "105vh", backgroundColor:"#1B264D"}}>
    <div style={{}}>
        <div style={{}}>
          <NavLink
            style={{
              textDecoration: "none",
              fontWeight: "bold",
              color: "#282c34",
              fontSize: 20
            }}
            to="/"
          >
             <img src={logo_web} style={{width:"45px", marginTop: "5px" }}/>
          </NavLink>
        </div>
        <div style={{ }}>
          <NavLink
            style={{
              display:"flex",
              justifyContent:"center",
              alignItems:"center",
              textDecoration: "none",
              fontWeight: "bold",
              color: "#282c34",
              fontSize: 20
            }}
            to="/user-admin"
          >
            <Avatar />
          </NavLink>
        </div>
        <div style={{}}>
          <NavLink
            style={{
              textDecoration: "none",
              fontWeight: "bold",
              color: "white",
              fontSize: 20
            }}
            to="/club-admin"
          >
            <div>
            <i class="fa-solid fa-users" style={{color:"white"}}></i>
            club
            </div>
          </NavLink>
        </div>
      </div>
  </div>
);

export default Header;