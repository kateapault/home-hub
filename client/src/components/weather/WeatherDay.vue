<template>
    <div class="weather-day-container">

        <div>{{ day }}</div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    day: String,
});
</script>