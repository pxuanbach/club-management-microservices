import React, { lazy } from 'react';
import { Routes, Route } from 'react-router-dom';
import MicroFrontend from "./components/MicroFrontend";
import NotFound from "./components/NotFound";
import Login from "./components/pages/Login";

const userAdminHost = process.env.REACT_APP_USER_ADMIN_HOST;
const clubAdminHost = process.env.REACT_APP_CLUB_ADMIN_HOST;
const myClubHost = process.env.REACT_APP_MY_CLUB_HOST;

const Main = () => {
    return (
        <div>
            <h1>abc</h1>
        </div>
       
    )
}

const UserAdmin = ({ history }) => (
    <MicroFrontend history={history} host={userAdminHost} name="UserAdmin" />
);

const ClubAdmin = ({ history }) => (
    <MicroFrontend history={history} host={clubAdminHost} name="ClubAdmin" />
);

const MyClub = ({history}) => (
    <MicroFrontend history={history} host={myClubHost} name="MyClub" />
);

const ContainerRoutes = () => {
    return (
        <Routes>
            <Route exact path="/" element={<Main/>}/>
            <Route path="/login" element={<Login/>} />
            <Route path="/user-admin" element={<UserAdmin/>} />
            <Route path="/club-admin" element={<ClubAdmin/>} /> 
            <Route path="/my-club" element={<MyClub/>} />
            <Route path="*" element={<NotFound/>} />
        </Routes>
    )
};

export default ContainerRoutes;