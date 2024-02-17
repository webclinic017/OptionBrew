import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { Provider as PaperProvider } from "react-native-paper";
import Login from "./src/screens/Login";
import SignUp from "./src/screens/SignUp";
import Tabs from "./src/components/Tabs";
import ForgotPassword from "./src/screens/ForgotPassword";

const Stack = createStackNavigator();

export default function App() {
  return (
    <PaperProvider theme={themes}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Login">
          <Stack.Screen name="Login" component={Login} />
          <Stack.Screen name="SignUp" component={SignUp} />
          <Stack.Screen name="ForgotPassword" component={ForgotPassword} />
          <Stack.Screen name="Tabs" component={Tabs} />
        </Stack.Navigator>
      </NavigationContainer>
    </PaperProvider>
  );
}

const themes = {
  colors: {
    primary: "rgb(0, 95, 175)",
    onPrimary: "rgb(255, 255, 255)",
    primaryContainer: "rgb(212, 227, 255)",
    onPrimaryContainer: "rgb(0, 28, 58)",
    secondary: "rgb(0, 99, 154)",
    onSecondary: "rgb(255, 255, 255)",
    secondaryContainer: "rgb(206, 229, 255)",
    onSecondaryContainer: "rgb(0, 29, 50)",
    tertiary: "rgb(0, 103, 131)",
    onTertiary: "rgb(255, 255, 255)",
    tertiaryContainer: "rgb(188, 233, 255)",
    onTertiaryContainer: "rgb(0, 31, 42)",
    error: "rgb(186, 26, 26)",
    onError: "rgb(255, 255, 255)",
    errorContainer: "rgb(255, 218, 214)",
    onErrorContainer: "rgb(65, 0, 2)",
    background: "rgb(253, 252, 255)",
    onBackground: "rgb(26, 28, 30)",
    surface: "rgb(253, 252, 255)",
    onSurface: "rgb(26, 28, 30)",
    surfaceVariant: "rgb(224, 226, 236)",
    onSurfaceVariant: "rgb(67, 71, 78)",
    outline: "rgb(116, 119, 127)",
    outlineVariant: "rgb(195, 198, 207)",
    shadow: "rgb(0, 0, 0)",
    scrim: "rgb(0, 0, 0)",
    inverseSurface: "rgb(47, 48, 51)",
    inverseOnSurface: "rgb(241, 240, 244)",
    inversePrimary: "rgb(165, 200, 255)",
    elevation: {
      level0: "transparent",
      level1: "rgb(240, 244, 251)",
      level2: "rgb(233, 239, 249)",
      level3: "rgb(225, 235, 246)",
      level4: "rgb(223, 233, 245)",
      level5: "rgb(218, 230, 244)",
    },
    surfaceDisabled: "rgba(26, 28, 30, 0.12)",
    onSurfaceDisabled: "rgba(26, 28, 30, 0.38)",
    backdrop: "rgba(45, 49, 56, 0.4)",
  },
};
