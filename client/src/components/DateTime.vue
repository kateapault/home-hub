<template>
    <div class="datetime" style="display: flex; justify-content: space-between;">
        <div id="datetime-time">{{ hour }}:{{ minute }}</div>
        <div id="datetime-day-date">
            <div id="datetime-day">{{ dayOfWeek }}</div>
            <div id="datetime-date">{{ month }} {{ day }}</div>
        </div>
    </div>
</template>

<script>
const dayMapping = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}
const monthMapping = {
    0: 'Jan',
    1: 'Feb',
    2: 'Mar',
    3: 'Apr',
    4: 'May',
    5: 'Jun',
    6: 'Jul',
    7: 'Aug',
    8: 'Sep',
    9: 'Oct',
    10: 'Nov',
    11: 'Dec'
}
export default {
    data() {

        return {
            hour: '',
            minute: '',
            second: '',
            timer: undefined
        }
    },
    methods: {
        setDateTime() {
            let d = new Date()
            this.hour = d.getHours() > 9 ? d.getHours() : `0${d.getHours()}`;
            this.minute = d.getMinutes() > 9 ? d.getMinutes() : `0${d.getMinutes()}`;
            this.second = d.getSeconds() > 9 ? d.getSeconds() : `0${d.getSeconds()}`;
        }

    },
    computed: {
        dayOfWeek() {
            return dayMapping[new Date().getDay()]
        },
        month() {
            return monthMapping[new Date().getMonth()]
        },
        day() {
            return new Date().getDate()
        }
    },
    beforeMount() {
        this.timer = setInterval(this.setDateTime,1000)
    },
    beforeUnmount() {
        clearInterval(this.timer)
    },
}
</script>