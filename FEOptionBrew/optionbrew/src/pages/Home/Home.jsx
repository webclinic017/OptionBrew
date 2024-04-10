import React from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const Home = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleSignUpClick = () => {
    navigate("/sign-up");
  };

  return (
    <div className="option-brew-home">
      <div className="text-and-login-container">
        <h1>
          <span className="highlighted-word">Transform</span> Your Portfolio
          with Option Brew
        </h1>
        <p>
          Step into the forefront of financial innovation with Option Brew.
          Leveraging the cutting-edge{" "}
          <span className="highlighted-word"> Alpaca API</span>, we provide a
          seamless and dynamic platform to enhance your trading potential.
        </p>
        <div className="header-buttons">
          <button className="btn login-btn" onClick={handleLoginClick}>
            Login
          </button>
          <button className="btn signup-btn" onClick={handleSignUpClick}>
            Sign Up
          </button>
        </div>
      </div>
      <div className="stocks-graph-placeholder">
        <p>FAANG stocks + graphs</p>
      </div>
      <footer className="option-brew-footer">
        © 2024 Option Brew All Rights Reserved. |{" "}
        <a href="/terms-of-service">Terms of Service</a> |{" "}
        <a href="/privacy-policy">Privacy Policy</a>
      </footer>
    </div>
  );
};

export default Home;
