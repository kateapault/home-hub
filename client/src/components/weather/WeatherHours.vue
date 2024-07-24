<template>
    <div class="weather-hours-container">

    </div>
</template>

<script setup>
import { ref } from 'vue';
import { $mqtt } from 'vue-paho-mqtt';
import WeatherHour from './WeatherHour.vue';

const weatherHours = ref([
    
])
</script>