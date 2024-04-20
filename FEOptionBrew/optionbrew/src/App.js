import "./App.css";
import React from "react"; // Ensure React is in scope when using JSX.
import Home from "./pages/Home/Home";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import ProtectedRoute from "./util/ProtecedRoute";
import Account from "./pages/Account/Account";
import SignUp from "./pages/SignUp/SignUp";
import Login from "./pages/Login/Login";
import Navbar from "./components/Navbar/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sign-up" element={<SignUp />} />
        <Route path="/login" element={<Login />} />

        {/* PROTECTED ROUTES */}
        <Route element={<ProtectedRoute />}>
          <Route path="/account" element={<Account />} />
          <Route path="/dashboard" element={<Account />} />
          <Route path="/market" element={<Account />} />
          <Route path="/watchlist" element={<Account />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
