import React, { Suspense, useState, useEffect } from "react";
import { BrowserRouter } from 'react-router-dom';
import axiosInstance from "./AxiosInstance";
import { UserContext } from "./UserContext";
import Navbar from "./components/Navbar";
import ContainerRoutes from "./routers";
import "./App.css"

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const verifyUser = async () => {
      try {
        const token = localStorage.getItem("token")
        const res = await axiosInstance.post('/auth/verify-token', 
        token,
        { 
          headers: { 
            'Content-Type': 'application/json', 
            'Accept': 'application/json'
          },
        });
        const data = res.data;
        //console.log(data)
        setUser(data);
      } catch (error) {
        console.log(error)
      }
    }
    verifyUser();
  }, [])

  return (
    <div className="App">
      <UserContext.Provider value={{ user, setUser }}>
        <BrowserRouter>
          <Suspense fallback={<span>Loading...</span>}>
            <Navbar />
            <ContainerRoutes />
          </Suspense>
        </BrowserRouter>
      </UserContext.Provider>
    </div>
  );
}

export default App;
