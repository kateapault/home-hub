<template>
    <div style="display:flex;flex-direction: column; border: 1px solid purple;">
        <div>
            <div>{{ tempC }} C ({{ tempF }} F)</div>
            <div>Feels like {{ feelsLikeC }} C ({{ feelsLikeF }} F)</div>
            <div>
                <div>{{ weatherEmoji }}</div>
                <div>{{ weatherDescription }}</div>
            </div>
            <div>
                Humidity {{ humidity }}%
            </div>
            <div>
                Precipitation {{ precipitation }}"
            </div>
            <div>
                Wind: {{ windSpeed }} mph {{ windDirection }}, gusts {{ windGusts }} mph
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            tempF: 0,
            tempC: 0,
            weatherDescription: "",
            weatherEmoji: "",
            precipitation: "",
            humidity: 0,
            feelsLikeF: 0,
            feelsLikeC: 0,
            windSpeed: 0,
            windDirection: "",
            windGusts: 0
        }
    },
    methods: {
        async getWeatherInfo() {
            let url = 'http://127.0.0.1:5000/data/weather'
            let resp = await axios.get(url)
            console.log(resp.data)
            this.tempC = resp.data["temperature_c"]
            this.tempF = resp.data["temperature_f"]
            this.feelsLikeC = resp.data["apparent_temp_c"]
            this.feelsLikeF = resp.data["apparent_temp_f"]
            this.weatherEmoji = resp.data["weather_emoji"]
            this.weatherDescription = resp.data["weather_description"]
            this.precipitation = resp.data["precipitation"]
            this.humidity = resp.data["relative_humidity"]
            this.windSpeed = resp.data["wind_speed"]
            this.windDirection = resp.data["wind_direction"]
            this.windGusts = resp.data["wind_gusts"]
        },
    },
    mounted() {
        this.getWeatherInfo()
    }
}

</script>