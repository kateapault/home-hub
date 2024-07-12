<template>
    <div>
        <DateTime />
    </div>
    <div class="container">
        <WeatherEtc />
        <!-- <Weather /> -->
        <MoonPhase />
        <MqttTest />
    </div>
</template>

<script setup>
import DateTime from './DateTime.vue';
import MqttTest from './MqttTest.vue';
import MoonPhase from './MoonPhase.vue'
import Weather from './Weather.vue'
import WeatherEtc from './WeatherEtc.vue';
// import HouseFeed from './HouseFeed.vue';
</script>