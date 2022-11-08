import React from 'react';
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

  const columns = [
    { field: 'id', headerName: 'ID', headerAlign: 'center',align: 'center',flex: 0.5,disableColumnMenu: true, },
    { field: 'img_url', headerName: 'Hình đại diện',  flex: 0.6 },
    { field: 'name', headerName: 'Tên câu lạc bộ',  flex: 1.3 },
    {
      field: 'leader',
      headerName: "Trưởng câu lạc bộ",
      flex: 1,
    },
    {
      field: 'treasurer',
      headerName: "Thủ quỹ",
      flex: 1,
    },
    { field: 'members_num', headerName: "Thành viên", type: 'number', flex: 0.5 },
    { field: 'fund', headerName: 'Quỹ (VND)', type: 'number', flex: 0.8 },
    {
      field: 'btn-update',
      headerName: '',
      align: 'center',
      flex: 0.4,
      disableColumnMenu: true,
      sortable: false,
      renderCell: (value) => {
        return (
          <Tooltip title="Cập nhật" placement="right-start">
            <Button style={{ color: '#1B264D' }}><i class="fa-solid fa-pen-to-square" style={{ fontSize: 20 }}></i></Button>
          </Tooltip>
        )
      }
    },
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
    {
      field: 'btn-delete',
      headerName: '',
      align: 'center',
      flex: 0.4,
      disableColumnMenu: true,
      sortable: false,
      renderCell: (value) => {
        return (
          <Tooltip title="Xóa" placement="right-start">
            <Button style={{ color: '#1B264D' }}>
              <ClearIcon />
            </Button>
          </Tooltip>
        )
      }
    }
  ];
  
  const rows = [
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
    { id: 1, img_url: '', name: 'Jon', leader: 'dat', treasurer:'bach',members_num: 10,fund: 1000 },
  ];
  
  return (
    <div className="container">
      <div className='mng__header'>
        <h2>Quản lý các câu lạc bộ</h2>
        <div className='header__stack'>
          <div className='stack-left'>
            <CustomTextField
              id="search-field"
              label="Tìm kiếm (Tên Câu lạc bộ)"
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
              // onClick={handleOpenAdd}
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
