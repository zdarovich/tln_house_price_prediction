<template>
  <div class="container">
    <section>
      <PostForm></PostForm>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import Table from './Table'
import VueChartJS from './VueChartJS'
import PostForm from './PostForm'

export default {
  components: {PostForm, VueChartJS, Table},
  data () {
    return {
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
