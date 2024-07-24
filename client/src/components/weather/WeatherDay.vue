<template>
    <div class="weather-day-container">
        <div>{{ formatDayDate(day.date) }}</div>
        <div>
            <div>{{ day.weatherEmoji }}</div>
            <div>{{ day.weatherDescription }}</div>
        </div>
        <div>
            <div><span class="temp-high">H</span> {{ day.maxTempC }}C ({{ day.maxTempF }}F)</div>
            <div><span class="temp-low">L</span> {{ day.minTempC }}C ({{ day.minTempF }}F)</div>
        </div>
        <div>{{ day.precipitationChance }}% ☔</div>
        <div>
            <div>⬆️🌅 {{ formatSunriseSunset(day.sunrise) }}</div>
            <div>⬇️🌅 {{ formatSunriseSunset(day.sunset) }}</div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
defineProps({
    day: {
        date: Date,
        precipitationChance: Number,
        sunrise: Date,
        sunset: Date,
        weatherDescription: String,
        weatherEmoji: String,
        maxTempF: Number,
        maxTempC: Number,
        minTempF: Number,
        minTempC: Number,
    },
});

const dayMapping = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
};

function formatDayDate(timestamp) {
    let d = new Date(timestamp);
    return `${dayMapping[d.getDay()]}, ${d.getMonth() + 1}/${d.getDate()}`
};

function formatSunriseSunset(timestamp) {
    let d = new Date(timestamp)
    return `${d.getHours() < 10 ? '0' + d.getHours() : d.getHours()}:${d.getMinutes()}`
}

</script>