import React, { Suspense } from "react";
import { BrowserRouter } from 'react-router-dom';

import Header from "./components/Header";
import ContainerRoutes from "./routers";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Suspense fallback={<span>Loading...</span>}>
          <Header></Header>
          <ContainerRoutes/>
        </Suspense>
      </BrowserRouter>
    </div>
  );
}

export default App;
