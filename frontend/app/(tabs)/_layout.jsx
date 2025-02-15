import { View, Text, Image } from 'react-native';
import { Tabs, Redirect } from 'expo-router';
import "../../global.css";

import { icons } from '../../constants'

const TabIcon = ({ icon, color, name, focused }) => {
  return (
    <View className="flex items-center justify-center"> 
      <Image
        source={icon}
        resizeMode="contain"
        style={{
          tintColor: color,
          marginTop: 10,
          width: focused ? 35 : 25, // width adjustment of icons
          height: focused ? 35 : 25, // height adjustment of icons
        }}

      />
    </View>
  )
}

const TabsLayout = () => {
  return (
    <>
    <Tabs
        screenOptions={{
          tabBarActiveTintColor: "#FFA001",
          tabBarInactiveTintColor: "#CDCDE0",
          tabBarShowLabel: false,
          tabBarStyle: {
            backgroundColor: "#161622",
            borderTopWidth: 0.5, //
            borderTopColor: "#ffffff",
            height: 83, // height of tab bottom bar; 
          },
        }}
      >
        <Tabs.Screen
          name="home"
          options={{
            title: "Home",
            headerShown: false,
            tabBarIcon: ({ color, focused }) => (
              <TabIcon
                icon={icons.home}
                color={color}
                name="Home"
                focused={focused}
              />
            ),
          }}
        />
        <Tabs.Screen
          name="[query]"
          options={{
            title: "Search",
            headerShown: false,
            tabBarIcon: ({ color, focused }) => (
              <TabIcon
                icon={icons.search}
                color={color}
                name="Search"
                focused={focused}
              />
            ),
          }}
        />

        <Tabs.Screen
          name="tickets"
          options={{
            title: "Tickets",
            headerShown: false,
            tabBarIcon: ({ color, focused }) => (
              <TabIcon
                icon={icons.tickets}
                color={color}
                name="Tickets"
                focused={focused}
              />
            ),
          }}
        />
        <Tabs.Screen
          name="favourites"
          options={{
            title: "Favourites",
            headerShown: false,
            tabBarIcon: ({ color, focused }) => (
              <TabIcon
                icon={icons.favourites}
                color={color}
                name="Favourites"
                focused={focused}
              />
            ),
          }}
        />
        <Tabs.Screen
          name="profile"
          options={{
            title: "Profile",
            headerShown: false,
            tabBarIcon: ({ color, focused }) => (
              <TabIcon
                icon={icons.profile}
                color={color}
                name="Profile"
                focused={focused}
              />
            ),
          }}
        />
      </Tabs>
    </>
  )
}

export default TabsLayout