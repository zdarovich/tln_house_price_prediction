<template>
    <div class="columns">
      <div class="column">
          <Reactive :chart-data="datacollection"></Reactive>
          <button class="button is-primary" @click="fillData()">Randomize</button>
      </div>
    </div>
</template>

<script>
import Reactive from '@/components/Reactive'

export default {
  name: 'VueChartJS',
  props: {
    postForm: {
      type: Object
    }
  },
  components: {
    Reactive
  },
  data () {
    return {
      // instantiating datacollection with null
      datacollection: null
    }
  },
  created () {
    // anytime the vue instance is created, call the fillData() function.
    this.fillData()
  },
  methods: {
    fillData () {
      this.datacollection = {
        // Data for the y-axis of the chart
        labels: ['0', '50000', '100000', '150000', '200000', '250000'],
        datasets: [
          {
            label: 'Sale price probability',
            backgroundColor: '#8c67ef',
            // Data for the x-axis of the chart
            data: [0, 120, 300, 256, 180, 175]
          }
        ]
      }
    },
    getRandomInt () {
      // JS function to generate numbers to be used for the chart
      return Math.floor(Math.random())
    }
  }
}
</script>

<style scoped>

</style>
