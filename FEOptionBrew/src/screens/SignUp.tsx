import React, { useState } from "react";
import { View, StyleSheet } from "react-native";
import { Button, TextInput, Text } from "react-native-paper";

const SignUp = ({}) => {
  const [email, setEmail] = useState("");
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [password, setPassword] = useState("");
  const [phoneNumber, setNumber] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState(new Date());

  const handleSignUp = () => {
    // Placeholder for sign-up logic
    console.log(email, firstname, password, dateOfBirth);
    // navigation.navigate('Login'); // Navigate to Login after sign-up
  };

  return (
    <View style={{ flex: 1, justifyContent: "center", padding: 20 }}>
      <Text variant={"displaySmall"} style={styles.title}>
        Signup
      </Text>
      <Text variant={"titleMedium"}>
        Please enter your information to get started
      </Text>
      <View>
        <TextInput
          label="Email"
          value={email}
          onChangeText={setEmail}
          mode="outlined"
          style={styles.inputText}
        />
        <TextInput
          label="First Name"
          value={firstname}
          onChangeText={setFirstName}
          mode="outlined"
          style={styles.inputText}
        />
        <TextInput
          label="Last Name"
          value={lastname}
          onChangeText={setLastName}
          mode="outlined"
          style={styles.inputText}
        />
      </View>
      {/* <View>
        <TextInput
          label="Street Address"
          value={""} // You need to implement the state for street address
          onChangeText={() => {}} // You need to implement the function to set street address
          mode="outlined"
        />
        <TextInput
          label="Phone Number"
          value={phoneNumber}
          onChangeText={setNumber}
          mode="outlined"
          keyboardType="phone-pad"
        />
      </View>
      <TextInput
        label="Password"
        value={password}
        onChangeText={setPassword}
        mode="outlined"
        secureTextEntry
      /> */}
      <Button mode="contained" onPress={handleSignUp} style={styles.button}>
        Sign Up
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  title: {
    marginBottom: 20,
    textAlign: "center",
  },
  bar: {
    textAlign: "left",
    fontSize: 18,
    padding: 10,
  },
  button: {
    margin: 20,
    width: 150,
    alignSelf: "center",
  },
  inputText: {
    fontSize: 16,
    fontWeight: "300",
    width: 500,
    alignSelf: "center",
    margin: 15,
  },
});

export default SignUp;
