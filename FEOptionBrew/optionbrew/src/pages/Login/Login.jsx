import React from "react";
import { useState, useRef } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

const server = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const requestSent = useRef(false);

  localStorage.removeItem("token");

  const navigate = useNavigate();

  const handleSubmit = () => {};

  return (
    <div className="login-form-container">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Email</label>
          <input
            className="username-form"
            type="email"
            id="username"
            name="username"
            placeholder="Enter your email"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            className="password-form"
            type="password"
            id="password"
            name="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="forgot-password">
          <Link to="/reset-password">Forgot password?</Link>
        </div>
        <button type="submit">Login</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <div className="sign-up">
          <span>Don't have an account? </span>
          <Link to="/sign-up">Sign Up</Link>
        </div>
        {/* <div className="guest-user" onClick={handleGuestUser}>
          <span> or </span>
          <span className="guest-text">Continue as a guest</span>
        </div> */}
      </form>
    </div>
  );
};

export default Login;
