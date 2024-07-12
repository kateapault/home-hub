<template>
    <div class="section">
        <div class="weatheretc-container-daily" style="display: flex;">
            <CurrentWeather />
            <div style="display: flex;flex-direction: column;">
                <Moon />
                <Tide />
            </div>
        </div>
        <WeatherWeek />
    </div>
</template>

<script setup>
import CurrentWeather from './weather/CurrentWeather.vue';
import Tide from './weather/Tide.vue';
import Moon from './weather/Moon.vue';
import WeatherWeek from './weather/WeatherWeek.vue';
</script>