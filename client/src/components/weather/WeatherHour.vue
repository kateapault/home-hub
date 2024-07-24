<template>
    <div>
        <div>{{ weather.time }}</div>
        <div>{{ weather.weatherEmoji }}</div>
        <div>{{ weather.weatherDescription }}</div>
        <div>{{ weather.tempC }} C ({{ weather.tempF }} F)</div>
        <div>
            <div>{{ weather.humidity }}% 💧</div>
            <siv>{{ weather.precipChance }}% ☔</siv>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
defineProps({
    weather: {
        time: Date,
        tempF: Number,
        tempC: Number,
        humidity: Number,
        precipChance: Number,
        weatherDescription: String,
        weatherEmoji: String,
    }
})
</script>