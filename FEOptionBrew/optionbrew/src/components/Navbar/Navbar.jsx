import React from "react";
import { Link, useNavigate, NavLink } from "react-router-dom";
import { Axios } from "axios";
import "./Navbar.css";
import logoImport from "../../assets/Logo.png";

const Navbar = () => {
  // Navigation hook for redirecting
  const navigate = useNavigate();

  // Logo
  const logo = logoImport;

  const handleLogoClick = () => {
    navigate("/");
  };

  return (
    <nav>
      <div className="navbar">
        <div className="nav-container">
          <div className="navbar-logo" onClick={handleLogoClick}>
            <img src={logo} alt="Option Brew Logo" className="logo" />{" "}
          </div>
          <h1 className="optionBrew-Name" onClick={handleLogoClick}>
            Option <span className="highlighted-word">Brew</span>
          </h1>
          <div className="quick-links">
            <NavLink
              to="/dashboard"
              className={({ isActive }) =>
                isActive ? "quick-link active-link" : "quick-link"
              }
            >
              Dashboard
            </NavLink>
            <NavLink
              to="/market"
              className={({ isActive }) =>
                isActive ? "quick-link active-link" : "quick-link"
              }
            >
              Market
            </NavLink>
            <NavLink
              to="/watchlist"
              className={({ isActive }) =>
                isActive ? "quick-link active-link" : "quick-link"
              }
            >
              Watchlist
            </NavLink>
            <NavLink
              to="/account"
              className={({ isActive }) =>
                isActive ? "quick-link active-link" : "quick-link"
              }
            >
              Account
            </NavLink>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
