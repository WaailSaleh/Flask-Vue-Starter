<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld :msg="`Welcome to Your ${message} App`"/>
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  },
  data: () => ({
    message: '',
  }),
  mounted() {
    axios
      .get("/api/message")
      .then(response => response.data.message)
      .then(message => {
        this.message = message
      })
  },
}
</script>
