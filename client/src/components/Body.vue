<template>
    <div class="body-container">
        <div style="display:flex;justify-content: space-between;padding: 20px;">
            <Moon />
            <DateTime />
            <Tide />
        </div>
        <div style="display:flex; justify-content: center;">
            <!-- <WeatherEtc /> -->
            <CurrentWeather />
        </div>
        <div>
            <WeatherWeek />
        </div>
    </div>
</template>

<script setup>
import DateTime from './DateTime.vue';
// import MqttTest from './MqttTest.vue';
// import MoonPhase from './MoonPhase.vue'
import Moon from './weather/Moon.vue'
import Tide from './weather/Tide.vue'
// import Weather from './Weather.vue'
import WeatherEtc from './WeatherEtc.vue';
import CurrentWeather from './weather/CurrentWeather.vue';
import WeatherWeek from './weather/WeatherWeek.vue';
// import HouseFeed from './HouseFeed.vue';
</script>