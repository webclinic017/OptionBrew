import { ALPACA_API_KEY, ALPACA_API_SECRET } from "@env";

const BASE_URL = "https://broker-api.sandbox.alpaca.markets";
const API_KEY = ALPACA_API_KEY;
const API_SECRET = ALPACA_API_SECRET;

/* -------- BROKER -------- */

// Fetch Account Activities
export const fetchAccountActivities = async () => {
  const activitiesURL = `${BASE_URL}/v1/accounts/activities?page_size=100`;

  try {
    const response = await fetch(activitiesURL, {
      method: "GET",
      headers: {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET,
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    return await response.json();
  } catch (error) {
    console.error("There was an error!", error);
    throw error; // Throw error to handle it where the function is called
  }
};
