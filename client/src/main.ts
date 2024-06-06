import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { createPahoMqttPlugin } from 'vue-paho-mqtt'


const app = createApp(App)

app.use(createPinia())

app.mount('#app')
app.use(createPahoMqttPlugin({
    PluginOptions: {
        autoConnect: true,
        showNotifications: true,
    },
    MqttOptions: {
        host: '0.0.0.0',
        port: 1883,
        clientId: `Client-1234567`,
        mainTopic: 'Main',
        enableMainTopic: false,
        username: import.meta.env.VITE_FRONTEND_USERNAME,
        password: import.meta.env.VITE_FRONTEND_PW
    }
}))
