import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";
import axios from "axios";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";
import { format } from "date-fns";

const Home = () => {
  const navigate = useNavigate();
  const [stockData, setStockData] = useState([]);

  const fetchStockData = async () => {
    const endpoint = "http://127.0.0.1:8000/market-data/aapl/live/"; // Endpoint for live data

    try {
      const response = await axios.get(endpoint);
      console.log("Received data:", response.data); // Check the data structure
      const validData = response.data.map((data) => ({
        ...data,
        timestamp: new Date(data.t).getTime(),
      }));
      setStockData(validData);
    } catch (error) {
      console.error("Failed to fetch stock data:", error);
    }
  };

  useEffect(() => {
    fetchStockData();
    const interval = setInterval(fetchStockData, 60000);
    return () => clearInterval(interval);
  }, []);

  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleSignUpClick = () => {
    navigate("/sign-up");
  };
  console.log("Final stock data for chart:", stockData);

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
          <span className="highlighted-word">Alpaca API</span>, we provide a
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
        {stockData.length > 0 ? (
          <div>
            <h2>Stock Data Loaded</h2> {/* Debugging text */}
            <LineChart width={400} height={400} data={stockData}>
              <Line type="monotone" dataKey="c" stroke="#8884d8" />
              <CartesianGrid stroke="#ccc" />
              <XAxis
                dataKey="timestamp"
                tickFormatter={(tick) => {
                  try {
                    // Display both date and time
                    return format(new Date(tick), "yyyy-MM-dd HH:mm:ss");
                  } catch (error) {
                    console.error("Error formatting tick:", tick, error);
                    return "";
                  }
                }}
              />

              <YAxis />
              <Tooltip
                formatter={(value, name, props) => {
                  if (name === "c") {
                    return [`${value.toFixed(2)}`, "Close Price"];
                  }
                  return value;
                }}
                labelFormatter={(label) =>
                  format(new Date(label), "yyyy-MM-dd HH:mm:ss")
                }
              />
            </LineChart>
          </div>
        ) : (
          <p>Loading stock data...</p>
        )}
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
