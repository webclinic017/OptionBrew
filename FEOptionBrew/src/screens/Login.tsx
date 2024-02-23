import React, { useState } from "react";
import { View, StyleSheet, Text, TouchableOpacity } from "react-native";
import { Input, Button } from "react-native-elements";
import { AppDarkTheme } from "../styles/Theme"; // Adjust the path as needed

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <View style={styles.container}>
      <Input
        placeholder="Enter your email"
        inputStyle={{ color: AppDarkTheme.colors.text }}
        placeholderTextColor="#ccc"
        inputContainerStyle={{
          borderBottomColor: AppDarkTheme.colors.secondary,
        }}
      />
      <Input
        placeholder="Enter your password"
        secureTextEntry={true}
        inputStyle={{ color: AppDarkTheme.colors.text }}
        placeholderTextColor="#ccc"
        inputContainerStyle={{
          borderBottomColor: AppDarkTheme.colors.secondary,
        }}
      />
      <TouchableOpacity>
        <Text style={styles.forgotPasswordText}>Forgot Password?</Text>
      </TouchableOpacity>
      <Button
        title="Log in"
        buttonStyle={{ backgroundColor: AppDarkTheme.colors.primary }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    backgroundColor: AppDarkTheme.colors.background,
    padding: 20,
  },
  forgotPasswordText: {
    color: AppDarkTheme.colors.secondary,
    textAlign: "right",
  },
});

export default Login;
