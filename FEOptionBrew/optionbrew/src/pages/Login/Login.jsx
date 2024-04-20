import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import "./Login.css";

const Login = () => {
  const [email, setEmail] = useState(""); // Changed variable name for clarity
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/login/", {
        email: email, // Updated to use email instead of username for clarity
        password: password,
      });
      localStorage.setItem("token", response.data.token); // Store the token in local storage
      console.log("Login successful", response.data);
      navigate("/dashboard"); // Redirect to a dashboard or home page after login
    } catch (err) {
      if (err.response) {
        setError("Failed to log in: " + err.response.data.error); // More specific error based on backend response
      } else {
        setError(
          "Failed to log in. Please check your credentials and try again."
        );
      }
      console.error(err);
    }
  };

  return (
    <div className="login-container">
      <h2>Log into Your Account</h2>
      <form onSubmit={handleSubmit} className="login-form">
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p className="login-error">{error}</p>}
        <button type="submit" className="login-btn-page">
          Login
        </button>
        <div className="login-links">
          <Link to="/sign-up">Don't have an account? Sign Up</Link>
        </div>
      </form>
    </div>
  );
};

export default Login;
