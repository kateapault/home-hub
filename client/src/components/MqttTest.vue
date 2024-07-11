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
                console.log('this should be showing up....')
                console.log(`got data: ${data}`);
                let response = JSON.parse(data)
                this.setMessage(response.text);
            })
        },
        setMessage(newMessage) {
            this.message = newMessage;
        }
    },
    mounted() {
        // this.$mqtt.connect();
        this.subscribe();
    }
}
</script>