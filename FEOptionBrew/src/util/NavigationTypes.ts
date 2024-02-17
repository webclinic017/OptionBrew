import { StackNavigationProp } from "@react-navigation/stack";

export type RootStackParamList = {
  Login: undefined;
  SignUp: undefined;
  ForgotPassword: undefined;
  // Add other screens here as needed
};

export type LoginScreenNavigationProp = StackNavigationProp<
  RootStackParamList,
  "Login"
>;
export type SignUpScreenNavigationProp = StackNavigationProp<
  RootStackParamList,
  "SignUp"
>;
