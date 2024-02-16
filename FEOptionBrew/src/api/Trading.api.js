import { ALPACA_API_KEY, ALPACA_API_SECRET } from "@env";

const BASE_URL = "https://paper-api.alpaca.markets";
const API_KEY = ALPACA_API_KEY;

/* -------- TRADING -------- */
/* Trading requires the Broker API Key + User ID
- Pass in the current users ID to 
*/

// Place an Order
export const placeOrder = async () => {
  const ordersURL = `${BASE_URL}/v2/orders`;

  try {
    const response = await fetch(ordersURL, {
      method: "POST",
      headers: {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        side: "buy",
        type: "market",
        time_in_force: "day",
      }),
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
