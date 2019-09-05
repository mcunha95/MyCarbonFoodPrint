<template>
<div id="outer-nav">
    <div id="nav-bar">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#"></a>
            <div class="icon-bar">
                <a @click="goMainScreen()"><img src ="../assets/mcfp_icon.png" alt = "Logo" style = "width:30px; height:auto; "></a>
                <a @click="goMapScreen()"><i class="fa fa-map-o" style = "padding-left: 2em;"></i></a>
            </div>
            <a class="navbar-brand" href="#"></a>           
        </nav>
    </div>
</div>
</template>

<script>
export default {
    name:'FooterArea',
    data(){
        return{}
    },
    methods:{
        goMainScreen(){
            this.$router.push('/')
        },
        goMapScreen(){
            this.$router.push('/map')
        } 
    }
}
</script>

<style scoped>
</style>