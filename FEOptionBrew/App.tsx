import React from "react";
import { NavigationContainer, DefaultTheme } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import Login from "./src/screens/Login";
import SignUp from "./src/screens/SignUp";
import Tabs from "./src/components/Tabs";
import ForgotPassword from "./src/screens/ForgotPassword";
import Home from "./src/screens/Home";
import { AppDarkTheme } from "./src/styles/Theme";

const Stack = createStackNavigator();

const MyTheme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    background: AppDarkTheme.colors.background,
    text: AppDarkTheme.colors.text,
  },
  dark: true, // Indicate that this is a dark theme
};

export default function App() {
  return (
    <NavigationContainer theme={MyTheme}>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="Login" component={Login} />
        <Stack.Screen name="SignUp" component={SignUp} />
        <Stack.Screen name="ForgotPassword" component={ForgotPassword} />
        <Stack.Screen name="Tabs" component={Tabs} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
