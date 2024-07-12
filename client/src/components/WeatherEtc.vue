<template>
    <div class="section">
        <div class="weatheretc-container-daily" style="display: flex;">
            <DailyWeather />
            <div style="display: flex;flex-direction: column;">
                <Moon />
                <!-- <Tide /> -->
            </div>
        </div>
        <WeeklyWeather />
    </div>
</template>

<script setup>
// import WeeklyWeather from './weather/WeeklyWeather.vue';
import DailyWeather from './weather/DailyWeather.vue';
import Tide from './weather/Tide.vue';
import Moon from './weather/Moon.vue';
// import Moon from './weather/Moon.vue';
</script>