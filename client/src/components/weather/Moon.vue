<template>
    <div class="moon-container card">
        <div class="moon-info">
            <div class="moon-emoji">{{ emoji }}</div>
            <div
                v-if="nextFullMoon < nextNewMoon"
                class="moon-next"
            >
                <div>🌕 {{ formatDate(nextFullMoon) }}</div>
                <div>🌑 {{ formatDate(nextNewMoon) }}</div>
            </div>
            <div
                v-else
                class="moon-next"
            >
                <div>🌑 {{ formatDate(nextNewMoon) }}</div>
                <div>🌕 {{ formatDate(nextFullMoon) }}</div>
            </div>
        </div>
        <div class="moon-phase">{{ moonPhase }}</div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { $mqtt } from 'vue-paho-mqtt';
// import { formatDate } from '..';

const emoji = ref("hi");
const moonPhase = ref("moon phase");
const nextFullMoon = ref(Date.now());
const nextNewMoon = ref(Date.now());

const dayMapping = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
};

function formatDate(timestamp) {
    let d = new Date(timestamp);
    return `${dayMapping[d.getDay()]}, ${d.getMonth() + 1}/${d.getDate()}`
};

$mqtt.subscribe("weather/moon", (message) => {
    let data = JSON.parse(message);
    moonPhase.value = data.moon_phase;
    emoji.value = data.moon_icon;
    nextFullMoon.value = Date.parse(data.next_full_moon);
    nextNewMoon.value = Date.parse(data.next_new_moon);
});

</script>