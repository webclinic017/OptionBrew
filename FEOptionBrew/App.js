import { GluestackUIProvider } from "@gluestack-ui/themed";
import { config } from "@gluestack-ui/config"; // Optional if you want to use default theme
import Login from "./src/screens/Login";

export default function App() {
  return (
    <GluestackUIProvider config={config}>
      <Login />
    </GluestackUIProvider>
  );
}
