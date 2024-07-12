<template>
    <div class="weather-week-container">
        <div v-for="d in week">
            <WeatherDay :day="d.day"/>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { $mqtt } from 'vue-paho-mqtt';
import WeatherDay from './WeatherDay.vue';

const week = [
    {day: 'Monday'},
    {day: 'Tuesday'},
    {day: 'Wednesday'},
    {day: 'Thursday'},
    {day: 'Friday'},
    {day: 'Saturday'},
    {day: 'Sunday'},
]

</script>