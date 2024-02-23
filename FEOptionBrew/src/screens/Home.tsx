import React from "react";
import { View, StyleSheet } from "react-native";
import { Button, Text, Image } from "react-native-elements";
import { useNavigation } from "@react-navigation/native";
import { StackNavigationProp } from "@react-navigation/stack";
import { AppDarkTheme } from "../styles/Theme"; // Adjust the path as needed
import { RootStackParamList } from "../util/NavigationTypes";

type HomeScreenNavigationProp = StackNavigationProp<RootStackParamList, "Home">;

const Home = () => {
  const navigation = useNavigation<HomeScreenNavigationProp>();

  return (
    <View style={styles.container}>
      <Text h3 style={styles.title}>
        Option Brew
      </Text>
      <Image
        source={require("../../assets/UndrawLogo.png")}
        style={styles.image}
        resizeMode="contain"
      />
      <Button
        title="Login"
        buttonStyle={{ backgroundColor: AppDarkTheme.colors.primary }}
        onPress={() => navigation.navigate("Login")}
      />
      <Button
        title="Sign Up"
        buttonStyle={{ backgroundColor: AppDarkTheme.colors.primary }}
        onPress={() => navigation.navigate("SignUp")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: AppDarkTheme.colors.background, // Use AppDarkTheme instead of DarkTheme
    padding: 10,
  },
  title: {
    color: AppDarkTheme.colors.text, // Use AppDarkTheme instead of DarkTheme
    marginBottom: 20,
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 20,
  },
});

export default Home;
