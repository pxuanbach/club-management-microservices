import React, { useContext } from 'react'
import Tooltip from '@mui/material/Tooltip'
import { Link } from 'react-router-dom'
import Avatar from '@mui/material/Avatar';
import { UserContext } from '../UserContext'

const SignedInMenu = ({ logout, pathName }) => {
    const { user } = useContext(UserContext);

    return (
        <div className='nav-menu'>
            <div className='list-btn'>
                <Tooltip title="Lịch hoạt động" placement="right-start">
                    <Link to="/scheduler">
                        <i class="fa-solid fa-calendar-days"></i>
                    </Link>
                </Tooltip>
                <Tooltip title="Câu lạc bộ của tôi" placement="right-start">
                    <Link
                        className={pathName === 'clubs' ? 'selected' : ''}
                        to="/clubs">
                        <i class="fa-solid fa-users"></i>
                    </Link>
                </Tooltip>
                <Tooltip title="Tin nhắn" placement="right-start">
                    <Link

                        to="/message">
                        <i class="fa-solid fa-comment-dots"></i>
                    </Link>
                </Tooltip>

                {user.username.includes('admin') ?
                    <>
                        <Tooltip title="Quản lý các câu lạc bộ" placement="right-start">
                            <Link

                                to="/club-admin">
                                <i class="fa-solid fa-users-gear"></i>
                            </Link>
                        </Tooltip>
                        <Tooltip title="Quản lý tài khoản" placement="right-start">
                            <Link

                                to='/user-admin'>
                                <i class="fa-solid fa-user-gear"></i>
                            </Link>
                        </Tooltip>
                    </> : null}
            </div>
            <div className='avatar-logout'>
                <Tooltip title="Thông tin cá nhân" placement="right-start">
                    <Link to="/info">
                        <Avatar src={user.img_url} />
                    </Link>
                </Tooltip>
                <Tooltip title="Đăng xuất" placement='right-start'>
                    <a onClick={logout} href="/login">
                        <i class="fa-solid fa-right-from-bracket"></i>
                    </a>
                </Tooltip>
            </div>
        </div>
    )
}

export default SignedInMenu