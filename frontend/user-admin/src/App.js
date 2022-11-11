import React, { useState, useEffect, useContext } from 'react'
import { DataGrid } from '@mui/x-data-grid';
import {
  Avatar, TextField, Button, Tooltip, Box,
  Modal, Alert, Snackbar, Popover
} from '@mui/material';
import { styled } from '@mui/material/styles';
import ClearIcon from '@mui/icons-material/Clear';
import SearchIcon from '@mui/icons-material/Search';
import RefreshIcon from '@mui/icons-material/Refresh';
import "./App.css"
import AddAccount from './modal/AddAccount';
const CustomTextField = styled(TextField)({
  '& label.Mui-focused': {
    color: '#1B264D',
  },
  '& .MuiInput-underline:after': {
    borderBottomColor: '#1B264D',
  },
});
const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 750,
  bgcolor: 'background.paper',
  border: 'none',
  boxShadow: 24,
  p: 3,
};
function App() {

  const [openModalAdd, setOpenModalAdd] = useState(false);

  const handleOpenAdd = () => setOpenModalAdd(true);
  const handleCloseAdd = () => setOpenModalAdd(false);

  const columns = [
    { field: 'id', headerName: 'ID', headerAlign: 'center',align: 'center',flex: 0.5,disableColumnMenu: true, },
    { field: 'img_url', headerName: 'Hình đại diện',  flex: 0.6 },
    { field: 'username', headerName: 'Tài khoản',  flex: 0.7 },
    { field: 'name', headerName: 'Tên người dùng', flex: 1.5 },
    { field: 'email', headerName: 'Email', flex: 1.5 },
    { field: 'groups_num', headerName: 'Số nhóm tham gia', type: 'number', flex: 0.8, sortable: false },
    {
      field: 'btn-block',
      headerName: '',
      align: 'center',
      flex: 0.4,
      disableColumnMenu: true,
      sortable: false,
      renderCell: (value) => {
        return (
          <Tooltip title={value.row.isblocked ? "Gỡ chặn" : "Chặn"} placement="right-start">
            <Button style={{ color: '#1B264D' }}>
              <i class={value.row.isblocked ? "fa-solid fa-lock" : "fa-solid fa-lock-open"}
                style={{ fontSize: 20 }}></i>
            </Button>
          </Tooltip>
        )
      }
    },
  ];
  
  const rows = [
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
    { id: 1, img_url: '', username: 'Jon', name: 'dat', email:'abc@gmail.com',groups_num: 10},
  ];
  
  return (
    <div className="container">
      <Modal
        open={openModalAdd}
        onClose={handleCloseAdd}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <AddAccount
            handleClose={handleCloseAdd}
            // users={users}
            // setUsers={setUsers}
            // showSnackbar={showSnackbar}
          />
        </Box>
      </Modal>
      <div className='mng__header'>
        <h2>Quản lý tài khoản</h2>
        <div className='header__stack'>
          <div className='stack-left'>
            <CustomTextField
              id="search-field"
              label="Tìm kiếm (Tài khoản, tên, email)"
              variant="standard"
              // value={search}
              // onChange={handleChangeSearchField}
              size='small'
              // onKeyPress={event => event.key === 'Enter' ? handleSearch(event) : null}
            />

            <Tooltip title='Tìm kiếm' placement='right-start'>
              <Button
                className='btn-search'
                variant="text"
                disableElevation
                >
                <SearchIcon sx={{ color: '#1B264D' }} />
              </Button>
            </Tooltip>
            <Tooltip title='Làm mới' placement='right-start'>
              <Button sx={{ borderColor: '#1B264D' }}
                className='btn-refresh'
                variant="outlined"
                disableElevation
                >
                <RefreshIcon sx={{ color: '#1B264D' }} />
              </Button>
            </Tooltip>
          </div>

          <div className='stack-right'>
            <Button
              style={{ background: '#1B264D' }}
              variant="contained"
              disableElevation
              startIcon={<i class="fa-solid fa-plus"></i>}
              onClick={handleOpenAdd}
              >
              Thêm tài khoản mới
            </Button>
            {/* <Button
              style={{ background: '#1B264D' }}
              variant="contained"
              disableElevation
              startIcon={<i class="fa-solid fa-file-import"></i>}>
              <span>Nhập file</span>
            </Button> */}
            <Button
              // onClick={handleExportUsers}
              style={{ background: '#1B264D' }}
              variant="contained"
              disableElevation
              startIcon={<i class="fa-solid fa-file-export"></i>}>
              <span>Xuất file</span>
            </Button>
          </div>
        </div>
      </div>
      <div className='mng__body'>
        <DataGrid
          // getRowId={(r) => r._id}
          rows={rows}
          columns={columns}
          autoHeight
          pageSize={7}
        />
      </div>
    </div>
  );
}

export default App;
