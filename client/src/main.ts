import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { createPahoMqttPlugin } from 'vue-paho-mqtt'


const app = createApp(App)

app.use(createPinia())

app.use(createPahoMqttPlugin({
    PluginOptions: {
        autoConnect: true,
        showNotifications: true,
    },
    MqttOptions: {
        // host: 'http://localhost',
        // port: 1883,
        clientId: `Client-1234567`,
        mainTopic: 'Main',
        username: 'user_front_end',
        password: 'frontend',
        enableMainTopic: false
    }
}));

app.mount('#app');