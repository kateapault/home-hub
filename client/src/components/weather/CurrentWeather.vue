<template>
    <div style="display:flex;flex-direction: column; border: 1px solid purple;">
        <div>
            <div>{{ tempC }} C ({{ tempF }} F)</div>
            <div>Feels like {{ feelsLikeC }} C ({{ feelsLikeF }} F)</div>
            <div>
                <div>{{ weatherEmoji }}</div>
                <div>{{ weatherDescription }}</div>
            </div>
            <div>
                Humidity: {{ humidity }}%
            </div>
            <div>
                Precipitation: {{ precipitation }}"
            </div>
            <div>
                Wind: {{ windSpeed }} mph {{ windDirection }}, gusts {{ windGusts }} mph
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { $mqtt } from 'vue-paho-mqtt';

const tempF = ref(0);
const tempC = ref(0);
const weatherDescription = ref("descrip");
const weatherEmoji = ref("em");
const precipitation = ref("precip");
const humidity = ref(0);
const feelsLikeF = ref(0);
const feelsLikeC = ref(0);
const windSpeed = ref(0);
const windDirection = ref("N");
const windGusts = ref(0);

$mqtt.subscribe("weather/current", (message) => {
    let data = JSON.parse(message);
    tempC.value = data.temperature_c;
    tempF.value = data.temperature_f;
    feelsLikeC.value = data.apparent_temp_c;
    feelsLikeF.value = data.apparent_temp_f;
    weatherEmoji.value = data.weather_emoji;
    weatherDescription.value = data.weather_description;
    precipitation.value = data.precipitation;
    humidity.value = data.relative_humidity;
    windSpeed.value = data.wind_speed;
    windDirection.value = data.wind_direction;
    windGusts.value = data.wind_gusts;
})
</script>