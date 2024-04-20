import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { format } from "date-fns";
import "./Home.css";
import CustomTooltip from "../../util/CustomToolTip";
import isMarketOpen from "../../util/MarketTiming";

const Home = () => {
  const navigate = useNavigate();
  const [stockData, setStockData] = useState([]);
  const [isDataLive, setIsDataLive] = useState(false);
  const [timeSpan, setTimeSpan] = useState("LIVE"); // Default to 'Live'
  const [ticker, setTicker] = useState("TSLA"); // Set default ticker symbol to 'TSLA'

  const getDateFormat = (span) => {
    switch (span) {
      case "LIVE":
        return "HH:mm"; // Hours and minutes for live data
      case "1M":
        return "MMM dd"; // Month and day for monthly data
      case "6M":
      case "YTD":
        return "MMM yyyy"; // Month and year for longer spans
      default:
        return "yyyy-MM-dd"; // Default to full date
    }
  };

  const calculateTicks = (data, span) => {
    let tickInterval;
    switch (span) {
      case "LIVE":
        tickInterval = 5 * 60 * 1000; // One tick every five minutes for live data
        break;
      case "1M":
        tickInterval = 3 * 24 * 60 * 60 * 1000; // One tick every three days
        break;
      case "6M":
        tickInterval = 30 * 24 * 60 * 60 * 1000; // One tick every month
        break;
      case "YTD":
        tickInterval = 2 * 30 * 24 * 60 * 60 * 1000; // One tick every two months
        break;
      default:
        tickInterval = 30 * 24 * 60 * 60 * 1000; // Default to one tick every month
    }
    const firstTick = data[0].timestamp;
    const lastTick = data[data.length - 1].timestamp;
    let ticks = [];
    for (let t = firstTick; t <= lastTick; t += tickInterval) {
      ticks.push(t);
    }
    return ticks;
  };

  const getTickCount = (span) => {
    switch (span) {
      case "LIVE":
        return 12; // More ticks for a live view
      case "1M":
        return 10;
      case "6M":
        return 12;
      case "YTD":
        return 6;
      default:
        return 10;
    }
  };

  const handleTimeSpanChange = (span) => {
    setTimeSpan(span);
    fetchStockData(span);
  };

  const fetchLiveData = async () => {
    const endpoint = `http://127.0.0.1:8000/market-data/${ticker}/live-data/`;
    try {
      const response = await axios.get(endpoint);
      const newData = response.data.map((data) => ({
        ...data,
        timestamp: new Date(data.timestamp).getTime(),
      }));
      setStockData(newData);
    } catch (error) {
      console.error("Failed to fetch live stock data:", error);
    }
  };

  const fetchStockData = async (span) => {
    let endpoint;
    if (span === "LIVE") {
      endpoint = `http://127.0.0.1:8000/market-data/${ticker}/live/`;
    } else {
      endpoint = `http://127.0.0.1:8000/market-data/${ticker}/historical/${span}/`;
    }

    console.log(`Fetching data from: ${endpoint}`); // Debugging log
    try {
      const response = await axios.get(endpoint);
      console.log(`Response from ${endpoint}:`, response.data); // Log the full response data
      const newData = response.data.map((data) => ({
        ...data,
        timestamp: new Date(data.t).getTime(),
      }));

      if (span === "LIVE") {
        setStockData((currentData) => [...currentData, ...newData]);
      } else {
        setStockData(newData);
      }
    } catch (error) {
      console.error("Failed to fetch stock data:", error);
    }
  };

  useEffect(() => {
    if (timeSpan === "LIVE") {
      const fetchInterval = isMarketOpen()
        ? setInterval(fetchLiveData, 5000)
        : null;
      setIsDataLive(!!fetchInterval); // Only set to true if interval is set

      // Fetch initial data if market is open
      if (fetchInterval) {
        fetchLiveData();
      }

      return () => clearInterval(fetchInterval);
    } else {
      setIsDataLive(false);
      fetchStockData(timeSpan); // Fetch historical data once

      return () => {}; // No cleanup needed for historical data fetch
    }
  }, [timeSpan, ticker]); // Removed isMarketOpen from dependencies

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
          <a className="alpaca-link" href="https://alpaca.markets/">
            Alpaca API
          </a>
          , we provide a seamless and dynamic platform to enhance your trading
          potential.
        </p>
        <div className="header-buttons">
          <button className="btn login-btn" onClick={() => navigate("/login")}>
            Login
          </button>
          <button
            className="btn signup-btn"
            onClick={() => navigate("/sign-up")}
          >
            Sign Up
          </button>
        </div>
      </div>
      <div className="stocks-graph-placeholder">
        <h2 className="tsla-label">${ticker}</h2>
        <div className="time-span-buttons">
          {["LIVE", "1M", "6M", "YTD"].map((span) => (
            <button
              key={span}
              className={`btn time-btn ${timeSpan === span ? "active" : ""}`}
              onClick={() => handleTimeSpanChange(span)}
            >
              {span}
            </button>
          ))}
        </div>
        {stockData.length > 0 ? (
          <ResponsiveContainer width="100%" height={400}>
            <LineChart
              data={stockData}
              margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
            >
              <Line
                type="monotone"
                dataKey="c"
                stroke="#82ca9d"
                strokeWidth={2}
                dot={{
                  stroke: "#82ca9d",
                  strokeWidth: 2,
                  fill: "#ffffff",
                  r: 3,
                }}
                activeDot={{
                  stroke: "green",
                  strokeWidth: 2,
                  fill: "white",
                  r: 7,
                }}
              />
              <XAxis
                dataKey="timestamp"
                tickFormatter={(unixTime) =>
                  format(new Date(unixTime), getDateFormat(timeSpan))
                }
                ticks={calculateTicks(stockData, timeSpan)}
                scale="time"
                type="number"
                domain={["dataMin", "dataMax"]}
                tick={{ fill: "#ccc", fontSize: 12 }}
                stroke="#ccc"
              />
              <YAxis
                tick={{ fill: "#ccc", fontSize: 12 }}
                stroke="#ccc"
                domain={[
                  (dataMin) => Math.floor(dataMin * 0.95),
                  (dataMax) => Math.ceil(dataMax * 1.05),
                ]}
              />
              <Tooltip content={<CustomTooltip />} />
            </LineChart>
          </ResponsiveContainer>
        ) : (
          <p>Loading stock data...</p>
        )}
      </div>
      <footer className="option-brew-footer">
        © 2024 Option Brew All Rights Reserved.
      </footer>
    </div>
  );
};

export default Home;
