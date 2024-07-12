<template>
    <div class="moon-container card">
        <div class="moon-info">
            <div class="moon-emoji">{{ emoji }}</div>
            <div
                v-if="fullMoonIsNext"
                class="moon-next"
            >
                <div>🌕 {{ nextFullMoon }}</div>
                <div>🌑 {{ nextNewMoon }}</div>
            </div>
            <div
                v-else
                class="moon-next"
            >
                <div>🌑 {{ nextNewMoon }}</div>
                <div>🌕 {{ nextFullMoon }}</div>
            </div>
        </div>
        <div class="moon-phase">{{ moonPhase }}</div>
        hi moon
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { $mqtt } from 'vue-paho-mqtt';
// import { formatDate } from '..';

const emoji = ref("hi");
const moonPhase = ref("moon phase");
const nextFullMoon = ref('next');
const nextNewMoon = ref('new');

const fullMoonIsNext = true;

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

$mqtt.subscribe("weather/moon", (data) => {
    console.log(data);
    let response = JSON.parse(data);
    // console.log(response.emoji);
    // this.emoji = response.moon_icon;
    moonPhase.value = response.moon_phase;
    // console.log(new Date(Date.now()));
    // console.log(formatDate(Date.now()));
    nextFullMoon.value = formatDate(Date.parse(response.next_full_moon));
    nextNewMoon.value = formatDate(Date.parse(response.next_new_moon));
})

</script>