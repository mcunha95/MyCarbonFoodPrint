
<template>
  <div id="main-page">
    <PredCountry/>
  </div>
</template>

<script>
import PredCountry from '@/components/PredCountry'

export default {
  name: 'MainPage',
  components: {
    PredCountry
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
