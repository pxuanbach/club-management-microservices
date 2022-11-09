import React, { useState, useEffect, useContext } from 'react'
import './App.css';
import { Box, Modal, Alert, Snackbar } from '@mui/material';  
import ClubItem from './ClubItem';
import AddClub from './modal/AddClub';

const style = {
  position: 'absolute',
  top: '45%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 700,
  bgcolor: 'background.paper',
  border: 'none',
  boxShadow: 24,
  p: 4,
};

function App() {

  const [showFormAddClub, setShowFormAddClub] = useState(false);
  return (
    <div>
      <Modal
        open={showFormAddClub}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        onClose={() => {
          setShowFormAddClub(false);
        }}
      >
        <Box sx={style}>
          <AddClub
            // setShowFormAdd={setShowFormAddClub}
            // clubs={clubs}
            // setClubs={setClubs}
            // showSnackbar={showSnackbar}
          />
        </Box>
      </Modal>
      <div className='div-header'>
        <div className='div-search'>
          <input
            // value={search}
            type="text"
            placeholder="Tìm kiếm câu lạc bộ"
            // onChange={handleChangeSearch}
            // onKeyPress={event => event.key === 'Enter' ? handleSearch(event) : null}
          />
          <i class="fa-solid fa-magnifying-glass"></i>
        </div>
      </div>
      <div className='div-body'>
        <div className='header-body'>
          <div className='header-title'> Câu lạc bộ của bạn</div>
          
            <div className='div-btnadd'>
              <button onClick={() => setShowFormAddClub(true)} className='btnAdd' >Tạo câu lạc bộ</button>
              <i class="fa-solid fa-plus"></i>
            </div>
        </div>
        <div className='div-card-team'>
          <ClubItem/>
        </div>

      </div>
    </div>

  );
}

export default App;
