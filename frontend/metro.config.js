const { getDefaultConfig } = require("expo/metro-config");
const { withNativeWind } = require("nativewind/metro");

const config = getDefaultConfig(__dirname);

module.exports = config;

config.resolver.assetExts = config.resolver.assetExts.filter(ext => ext !== "css");

config.resolver.sourceExts = [...config.resolver.sourceExts, "css"];

module.exports = withNativeWind(config, { input: "./global.css" });
