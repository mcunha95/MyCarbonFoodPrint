<template>
  <div id='country-pred'>
    <p>Based on your weekly food intake, you are probably from: {{country_pred}}</p>
  </div>
</template>

<script>
export default {
  name: 'CountryPred',
  data(){
    return{
      country_pred:''
    }
  },
  mounted(){
    this.$http.get(this.FLASK_URL+'/api/predict_country')
    .then(response => {
      this.country_pred = response.data
    })
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
