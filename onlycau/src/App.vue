<template>
  <div id="app">
    <MyHeader></MyHeader>
    <NavTop></NavTop>
    <Welcome></Welcome>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
import NavTop from './components/NavTop.vue'
import Welcome from './components/Welcome.vue'
import Footer from './components/Footer.vue'


export default {
  name: 'App',
  components:{
    MyHeader,
    NavTop,
    Welcome,
    Footer,
  }
}
</script>

<style>
</style>