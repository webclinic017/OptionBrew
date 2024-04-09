import "./App.css";
import React from "react"; // Ensure React is in scope when using JSX.
import Home from "./pages/Home/Home";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import ProtectedRoute from "./util/ProtecedRoute";
import Account from "./pages/Account/Account";
import SignUp from "./pages/SignUp/SignUp";
import Login from "./pages/Login/Login";

function App() {
  return (
    <BrowserRouter>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login />} />

          {/* PROTECTED ROUTES */}
          <Route element={<ProtectedRoute />}>
            <Route path="/account" element={<Account />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
