<template>
    <div class="tide-container">
        <div class="tide-status">
            <div class="tide-emojis">{{ emojis }}</div>
            <div class="tide-status-label">{{ tideStatus }} Tide</div>
        </div>
        <div
            v-if="highTideIsNext"
            class="tide-next-tide-block"
        >
            <div class="tide-next-tide">Next High Tide at {{ formatDate(nextHighTide) }}</div>
            <div class="tide-next-tide">Next Low Tide at {{ formatDate(nextLowTide) }}</div>
        </div>
        <div
            v-else
            class="tide-next-tide-block"
        >
            <div class="tide-next-tide">Next Low Tide at {{ formatDate(nextLowTide) }}</div>
            <div class="tide-next-tide">Next High Tide at {{ formatDate(nextHighTide) }}</div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { $mqtt  } from 'vue-paho-mqtt';

const tideStatus = ref("status");
const nextHighTide = ref(Date.now());
const nextLowTide = ref(Date.now());
const emojis = ref("emojiiiis");

const highTideIsNext = true;

function formatDate(timestamp) {
    let d = new Date(timestamp)
    if (d.getDay() == new Date().getDay()) {
        return `${d.getHours()}:${d.getMinutes()} today` 
    }
    return `0${d.getHours()}:${d.getMinutes()} tomorrow`
}

$mqtt.subscribe("weather/tide", (message) => {
    let data = JSON.parse(message);
    console.log(message)
    emojis.value = data.emojis;
    tideStatus.value = data.tide_status;
    nextHighTide.value = Date.parse(data.next_high_tide);
    nextLowTide.value = Date.parse(data.next_low_tide);
})

</script>