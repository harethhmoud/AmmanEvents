import { useState } from "react";
import { View, Text, RefreshControl, FlatList, Image } from 'react-native'
import React from 'react'
import { SafeAreaView } from 'react-native-safe-area-context'

import { images } from "../../constants";
import SearchInput from '../../components/SearchInput';
import Trending from '../../components/Trending';
import EmptyState from '../../components/EmptyState';


const HomeTab = () => {

  const [refreshing, setRefreshing] = useState(false);

  const onRefresh = async () => {
    setRefreshing(true);
    await refetch();
    setRefreshing(false);
  };

  return (
    <SafeAreaView className="bg-primary h-full">
      <FlatList // LIST OF ITEMS
      // data={[{ id: 1 }, { id: 2 }, { id: 3 }]} // FROM BACKEND
      data={[]}
      keyExtractor={(item)  =>  item.$id}
      renderItem={({ item }) => (
        <Text className="text-3xl text-white">{item.id}</Text>
        )}
        ListHeaderComponent ={() => (
          <View className="my-6 px-4 space-y-6">
            <View className="justify-between items-start flex-row mb-6">
              <View>
              <Text className="font-pmedium text-sm text-gray-100">
                  Welcome Back
                </Text>
                <Text className="text-2xl font-psemibold text-white">
                  USERNAME
                </Text>
              </View>
              <View className="mt-1.5">
                <Image
                  source={images.logoSmall}
                  className="w-9 h-10"
                  resizeMode="contain"
                />
              </View>

            </View>
            <SearchInput />
            <View className="w-full flex-1 pt-5 mt-5 pb-5">
              <Text className="text-lg font-pregular text-gray-100 mb-3">
                Latest Videos
              </Text>

              <Trending posts={[ {id:1}, {id:2}, {id:3}] ?? []} />

            </View>
          </View>
        )}
        ListEmptyComponent={() => (
          <EmptyState
            title="No Videos Found"
            subtitle="No videos created yet"
          />
        )}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }
      />
    </SafeAreaView>
  )
}

export default HomeTab