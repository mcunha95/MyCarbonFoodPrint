<template>
  <div id="app">
    <Header class='header'/>
    <router-view/>
    <Footer class='footer'/>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
  name: 'App',
  components:{Header, Footer}
}
</script>

<style>
#app {
  font-family: 'Pangram', sans-serif !important;
}
.footer {
    position: fixed; 
    bottom: 0;
    left: 0;
    right: 0;
    height: 50px;
    display: inline-block;
}
.header {
    margin-top: 0px; /* up to 60px does nothing*/
    }
</style>