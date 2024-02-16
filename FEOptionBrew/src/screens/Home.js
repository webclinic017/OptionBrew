import React, { useState } from "react";
import { SafeAreaView, View, Text, Button } from "react-native";
import { placeOrder } from "../api/Trading.api";

const Home = () => {
  const [orderResponse, setOrderResponse] = useState(null);
  const [error, setError] = useState("");

  const handlePlaceOrder = async () => {
    try {
      const response = await placeOrder();
      setOrderResponse(response);
      setError(""); // Reset error state in case of previous error
    } catch (error) {
      console.error(error);
      setError(error.message);
    }
  };

  return (
    <SafeAreaView>
      <View>
        <Text>Hello World</Text>
        <Button title="Place Order" onPress={handlePlaceOrder} />
        {orderResponse && (
          <Text>Order Placed: {JSON.stringify(orderResponse)}</Text>
        )}
        {error && <Text>Error: {error}</Text>}
      </View>
    </SafeAreaView>
  );
};

export default Home;
