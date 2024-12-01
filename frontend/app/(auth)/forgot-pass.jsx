import { useState } from "react";
import { Link, router } from "expo-router";
import { SafeAreaView } from "react-native-safe-area-context";
import { View, Text, ScrollView, Dimensions, Alert, Image } from "react-native";

import { images } from "../../constants";
import { CustomButton, FormField } from "../../components";
// import { getCurrentUser, logIn } from "../../lib/appwrite";
// import { useGlobalContext } from "../../context/GlobalProvider";

const ForgotPass = () => {
  const [form, setForm] = useState({
    email: "",
  });
  const [isSubmitting, setIsSubmitting] = useState(false)

  const submit = async () => {
 
  };

  return (
    <SafeAreaView className="bg-primary h-full">
      <ScrollView>
        <View
          className="w-full flex justify-center h-full px-4 my-2"
          style={{
            minHeight: Dimensions.get("window").height - 1000,
          }}
        >
          <Image
            source={images.logo}
            resizeMode="contain"
            className="w-[115px] h-[34px]"
          />

          <Text className="text-2xl font-semibold text-white mt-10 font-psemibold">
            Reset Password
          </Text>

          <FormField
            title="Email"
            value={form.email}
            handleChangeText={(e) => setForm({ ...form, email: e })}
            otherStyles="mt-7"
            keyboardType="email-address"
          />


          <CustomButton
            title="Reset"

            handlePress={submit}
            containerStyles="mt-7"
            isLoading={isSubmitting}
          />


        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

export default ForgotPass;