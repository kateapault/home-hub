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

<script>
import axios from 'axios';

export default {
    data() {
        return {
            tideStatus: "",
            nextHighTide: "",
            nextLowTide: "",
            emojis: ""
        }

    },
    methods: {
        async getTideInfo() {
            let url = 'http://127.0.0.1:5000/data/tide'
            let resp = await axios.get(url)
            this.tideStatus = resp.data.tide_status
            this.emojis = resp.data.emojis
            this.nextHighTide = Date.parse(resp.data.next_high_tide)
            this.nextLowTide = Date.parse(resp.data.next_low_tide)
        },
        formatDate(timestamp) {
            let d = new Date(timestamp)
            if (d.getDay() == new Date().getDay()) {
                return `${d.getHours()}:${d.getMinutes()} today` 
            }
            return `0${d.getHours()}:${d.getMinutes()} tomorrow`
        }
    },
    computed: {
        highTideIsNext() {
            this.nextHighTide && this.nextHighTide < this.nextLowTide
        }
    },
    mounted() {
        this.getTideInfo()
    }
}
</script>