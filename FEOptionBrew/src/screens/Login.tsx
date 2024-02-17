import React, { useState } from "react";
import { View, StyleSheet } from "react-native";
import { Button, TextInput, Text } from "react-native-paper";
import { LoginScreenNavigationProp } from "../util/NavigationTypes";

type Props = {
  navigation: LoginScreenNavigationProp;
};

const Login: React.FC<Props> = ({ navigation }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isPasswordSecure, setIsPasswordSecure] = useState(true);

  const togglePasswordVisibility = () => {
    setIsPasswordSecure((prev) => !prev);
  };

  const handleLogin = () => {
    console.log(username, password);
  };

  return (
    <View style={styles.container}>
      <TextInput
        label="Username"
        value={username}
        onChangeText={setUsername}
        mode="outlined"
        style={styles.input}
      />
      <TextInput
        label="Password"
        mode="outlined"
        secureTextEntry={isPasswordSecure}
        value={password}
        onChangeText={setPassword}
        style={styles.input}
        right={
          <TextInput.Icon
            icon={isPasswordSecure ? "eye" : "eye-off"}
            onPress={togglePasswordVisibility}
          />
        }
      />
      <Button
        onPress={() => navigation.navigate("ForgotPassword")}
        uppercase={false}
        style={styles.forgotPassword}
      >
        Forgot Password?
      </Button>
      <Button mode="contained" onPress={handleLogin} style={styles.button}>
        Login
      </Button>
      <View style={styles.signupContainer}>
        <Text style={styles.signUpText}>Don't have an account? </Text>
        <Button onPress={() => navigation.navigate("SignUp")} uppercase={false}>
          Sign Up
        </Button>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: "center",
  },
  input: {
    marginBottom: 10,
  },
  button: {
    marginTop: 10,
  },
  forgotPassword: {
    marginLeft: 235,
  },
  signupContainer: {
    flexDirection: "row",
    justifyContent: "center",
    marginTop: 20,
  },
  signUp: {
    fontSize: 15,
  },
  signUpText: {
    marginTop: 10,
    fontSize: 15,
  },
});

export default Login;
