import { StatusBar } from 'expo-status-bar';
import { ScrollView, Text, View, Image } from 'react-native';
import { Link } from 'expo-router';
import { Redirect, router } from 'expo-router';
import "../global.css";
import { SafeAreaView } from 'react-native-safe-area-context';

import { CustomButton } from '../components';
import { images } from '../constants';


export default function App() {
  return (
    <SafeAreaView className="bg-primary w-full h-full">
      <ScrollView contentContainerStyle={{height:'100%'}}>
        <View className='w-full h-full justify-center items-center px-4'>
            <Image className="h-[10vh]"
              source={ images.logo }
              resizeMode="contain"
              
            />

          <Text className='text-3xl text-secondary-200 font-bold text-center'>Uncover events you didn't know were there!</Text>
          
            <Image
              source={ images.cards }
              resizeMode="contain"
              style={{
                height: '300', // height adjustment of logo
                width: '380', // width adjustment of logo
             }}
           />


          <View className="relative mt-5"> 
          <Text className="text-sm font-pregular text-gray-100 mt-7 text-center">
          Helping you discover new experiences and exciting events happening in your city! 
          </Text>

          <CustomButton
            title="Continue with Email"
            handlePress={() => router.push("/sign-up")}
            containerStyles="mt-7"
          />

          </View>

        </View>
      </ScrollView>
      <StatusBar
      backgroundColor='#161622'
      style='light'
      
      />
    </SafeAreaView>
  );
}
