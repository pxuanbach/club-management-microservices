import React, { useEffect, useState } from 'react'
import Avatar from '@mui/material/Avatar';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import axiosInstance from '../AxiosInstance';
import './FindMember.css'


const FindMember = ({
    title,
    memberSelected,
    setMemberSelected,
    errorText,
    setErrorText
}) => {
    const [openAutoComplete, setOpenAutoComplete] = useState(false);
    const [users, setUsers] = useState([])

    const handleSearchMembers = async event => {
        event.preventDefault();
        if (event.target.value.trim()) {
            const res = await axiosInstance.get(`/users?search=${event.target.value.trim()}`)

            const data = res.data;
            //console.log(data)
            if (data) {
                setUsers(data)
            }
        } else {
            setUsers([])
        }
    }

    return (
        <div className='add-member'>
            <Autocomplete id='search-members'
                fullWidth
                open={openAutoComplete}
                onOpen={() => {
                    setOpenAutoComplete(true);
                }}
                onClose={() => {
                    setOpenAutoComplete(false);
                }}
                onChange={(event, value) => {
                    setMemberSelected(value)
                }}
                noOptionsText='Không tìm thấy'
                options={users}
                getOptionLabel={(option) => option.username}
                renderInput={(params) => (
                    <TextField {...params}
                        onChange={handleSearchMembers}
                        id="add-members"
                        variant="outlined"
                        label={title}
                        size="small"
                        error={errorText}
                        helperText={errorText}
                    />
                )}
            />
            {/* <div className='member-selected'>
                <Avatar />
                <div className='selected-info'>
                    <span>Nguyễn Tiến Đạt</span>
                    <span>abc@gmail.com</span>
                </div>
            </div> */}
        </div>
    )
}

export default FindMember