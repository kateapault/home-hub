<script setup>
import Body from './components/Body.vue'; 
import { $mqtt } from 'vue-paho-mqtt';
$mqtt.connect();
</script>

<template>
  <main>
    <Body />
  </main>
</template>

<style scoped>

</style>