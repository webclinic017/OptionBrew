import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./Account.css";

const Account = () => {
  const [userDetails, setUserDetails] = useState({
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
  });
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserDetails = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/users/me", {
          headers: {
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        });

        setUserDetails({
          firstName: response.data.first_name,
          lastName: response.data.last_name,
          email: response.data.email,
          phone: response.data.phone_number, // Adjust these keys based on your UserSerializer
        });
      } catch (error) {
        console.error("Error fetching user data:", error);
        setErrorMessage("Failed to fetch user data.");
      }
    };

    fetchUserDetails();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token"); // Clear session token
    navigate("/"); // Navigate to login page
  };

  return (
    <div className="account-container">
      <h1>My Account</h1>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      <div className="profile-info">
        <p>
          <strong>First Name:</strong> {userDetails.firstName}
        </p>
        <p>
          <strong>Last Name:</strong> {userDetails.lastName}
        </p>
        <p>
          <strong>Email:</strong> {userDetails.email}
        </p>
        <p>
          <strong>Phone:</strong> {userDetails.phone}
        </p>
      </div>
      <button onClick={handleLogout} className="logout-button">
        Logout
      </button>
    </div>
  );
};

export default Account;
