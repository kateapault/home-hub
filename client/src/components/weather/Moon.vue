<template>
    <div class="moon-container card">
        <div class="moon-info">
            <div class="moon-emoji">{{ emoji }}</div>
            <div
                v-if="fullMoonIsNext"
                class="moon-next"
            >
                <div>🌕 {{ formatDate(nextFullMoon) }}</div>
                <div>🌑 {{ formatDate(nextNewMoon) }}</div>
            </div>
            <div
                v-else
                class="moon-next"
            >
                <div>🌑 {{ formatDate(nextNewMoon) }}</div>
                <div>🌕 {{ formatDate(nextFullMoon) }}</div>
            </div>
        </div>
        <div class="moon-phase">{{ moonPhase }}</div>
    </div>
</template>

<script>
import axios from 'axios';
const dayMapping = {
    0: 'Sun',
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat'
}
export default {
    data() {
        return {
            emoji: "new",
            moonPhase: "",
            nextFullMoon: "",
            nextNewMoon: ""
        }
    },
    methods: {
        async getMoonInfo() {
            let url = 'http://127.0.0.1:5000/data/moon'
            let resp = await axios.get(url)
            this.moonPhase = resp.data.moon_phase
            this.emoji = resp.data.moon_icon
            this.nextNewMoon = Date.parse(resp.data.next_new_moon)
            this.nextFullMoon = Date.parse(resp.data.next_full_moon)
        },
        formatDate(timestamp) {
            let d = new Date(timestamp)
            return `${dayMapping[d.getDay()]}, ${d.getMonth() + 1}/${d.getDate()}`
        }
    },
    computed: {
        fullMoonIsNext() {
            return this.nextFullMoon && this.nextFullMoon < this.nextNewMoon
        }
    },
    mounted() {
        this.getMoonInfo()
    }


}

</script>