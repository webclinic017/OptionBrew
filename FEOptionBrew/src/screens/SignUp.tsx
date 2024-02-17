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
        SignUp
      </Text>
      <TextInput
        label="Email"
        value={email}
        onChangeText={setEmail}
        mode="outlined"
      />
      <TextInput
        label="First Name"
        value={firstname}
        onChangeText={setFirstName}
        mode="outlined"
      />
      <TextInput
        label="Last Name"
        value={lastname}
        onChangeText={setLastName}
        mode="outlined"
      />
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
      <TextInput
        label="Password"
        value={password}
        onChangeText={setPassword}
        mode="outlined"
        secureTextEntry
      />
      <Button mode="contained" onPress={handleSignUp}>
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
});

export default SignUp;
