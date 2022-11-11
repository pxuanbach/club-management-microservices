import React, { Suspense } from "react";
import { BrowserRouter } from 'react-router-dom';

import Navbar from "./components/Navbar";
import ContainerRoutes from "./routers";
import "./App.css"
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Suspense fallback={<span>Loading...</span>}>
          <Navbar/>
          <ContainerRoutes/>
        </Suspense>
      </BrowserRouter>
    </div>
  );
}

export default App;
