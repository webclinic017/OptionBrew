import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./Account.css";

/**
 * A component representing a user account page where user details are displayed and can be logged out.
 * It fetches user data from a backend upon mounting using an API call and handles user logout.
 *
 * @component
 * @example
 * return (
 *   <Account />
 * )
 */
const Account = () => {
  /** State to hold the user details */
  const [userDetails, setUserDetails] = useState({
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
  });

  /** State to hold any error messages */
  const [errorMessage, setErrorMessage] = useState("");

  /** Navigation hook from react-router-dom for redirection */
  const navigate = useNavigate();

  useEffect(() => {
    /**
     * Fetches user details from the server and updates state accordingly.
     * It uses the axios library to make the HTTP request.
     */
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
  }, []); // Empty dependency array means this effect will only run once after the component mounts.

  /**
   * Handles the user logout by removing the session token and navigating to the login page.
   */
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
