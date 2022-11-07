import React from 'react';
import { Link } from 'react-router-dom';
import Tooltip from '@mui/material/Tooltip'
import logo_web from "../assets/logoweb.png";
import Avatar from '@mui/material/Avatar';
import "./Navbar"
const Header = (pathName) => (
  <div className='nav-menu'>
            <div className='list-btn'>
                <Tooltip title="Lịch hoạt động" placement="right-start">
                    <Link
                        className={pathName === 'scheduler' ? 'selected' : ''}
                        to="/">
                        <i class="fa-solid fa-calendar-days"></i>
                    </Link>
                </Tooltip>
                <Tooltip title="Câu lạc bộ của tôi" placement="right-start">
                    <Link
                        className={pathName === 'clubs' ? 'selected' : ''}
                        to="/club-admin">
                        <i class="fa-solid fa-users"></i>
                    </Link>
                </Tooltip>
                <Tooltip title="Tin nhắn" placement="right-start">
                    <Link
                        className={pathName === 'message' ? 'selected' : ''}
                        to="/user-admin">
                        <i class="fa-solid fa-comment-dots"></i>
                    </Link>
                </Tooltip>
{/* 
                {user.username.includes('admin') ?
                    <> */}
                        <Tooltip title="Quản lý các câu lạc bộ" placement="right-start">
                            <Link
                                className={pathName === 'mng-club' ? 'selected' : ''}
                                to="/mng-club">
                                <i class="fa-solid fa-users-gear"></i>
                            </Link>
                        </Tooltip>
                        <Tooltip title="Quản lý tài khoản" placement="right-start">
                            <Link
                                className={pathName === 'mng-account' ? 'selected' : ''}
                                to='/mng-account'>
                                <i class="fa-solid fa-user-gear"></i>
                            </Link>
                        </Tooltip>
                    {/* </> : null} */}
            </div>
            <div className='list-btn'>
                {/* <div className='list-btn'> */}
                <Tooltip title="Thông báo" placement='right-start'>
                    <Link
                        className={pathName === 'notification' ? 'selected' : ''}
                        to="/notification">
                        <i class="fa-solid fa-bell"></i>
                    </Link>
                </Tooltip>
                {/* </div> */}
                <Tooltip title="Thông tin cá nhân" placement="right-start">
                    <Link className={pathName === 'info' ? 'selected' : ''} to="/info">
                        <Avatar />
                    </Link>
                </Tooltip>
                <Tooltip title="Đăng xuất" placement='right-start'>
                    <a href="/login">
                        <i class="fa-solid fa-right-from-bracket"></i>
                    </a>
                </Tooltip>
            </div>

        </div>

);

export default Header;