<template>
    <h2>mqtt message:</h2>
    <h1>{{ message }}</h1>
</template>

<script>
export default {
    data() {
        return {
            message: ""
        }
    },
    methods: {
        subscribe() {
            this.$mqtt.subscribe("weather/test", (data) => {
                this.message = data;
            })
        }
    },
    onMount() {
        subscribe();
    }
}
</script>