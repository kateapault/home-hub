<template>
    <div class="weather-week-container">
        <div v-for="d in weatherWeek">
            <WeatherDay :day="d"/>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { $mqtt } from 'vue-paho-mqtt';
import WeatherDay from './WeatherDay.vue';

const weatherWeek = ref([
    {date: Date.now()},
    {date: Date.now()},
    {date: Date.now()},
    {date: Date.now()},
    {date: Date.now()},
    {date: Date.now()},
    {date: Date.now()},
]);

$mqtt.subscribe("weather/week", (message) => {
    let data = JSON.parse(message)
    console.log(data)
    weatherWeek.value = data.map((d) => {
        return {
            date: Date.parse(d.date),
            precipitationChance: d.precipitation_chance,
            sunrise: Date.parse(d.sunrise),
            sunset: Date.parse(d.sunset),
            weatherDescription: d.weather_description,
            weatherEmoji: d.weather_emoji,
            maxTempF: d.maxTempF,
            maxTempC: d.maxTempC,
            minTempF: d.minTempF,
            minTempC: d.minTempC,
        }
    })
    // console.log(`made weather week: ${weatherWeek}`)
    // console.log(weatherWeek.value)
})

function formatDayDate(timestamp) {

}

function formatTime(timestamp) {

}


</script>