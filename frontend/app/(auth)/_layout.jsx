import { Redirect, Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";

import { Loader } from "../../components";

const AuthLayout = () => {
  
  return (
    <>
      <Stack>
        <Stack.Screen
          name="log-in"
          options={{
            headerShown: false,
          }}
        />
        <Stack.Screen
          name="forgot-pass"
          options={{
            headerShown: false,
          }}
        />
        <Stack.Screen
          name="sign-up"
          options={{
            headerShown: false,
          }}
        />
      </Stack>
      <StatusBar backgroundColor="#161622" style="light" />
    </>
  );
};

export default AuthLayout;