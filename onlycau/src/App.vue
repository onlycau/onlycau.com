<template>
    <div id="app">
      <MyHeader></MyHeader>
      <NavTop></NavTop>
      <router-view></router-view>
      <Footer></Footer>
    </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
import Footer from './components/Footer.vue'
import NavTop from './components/NavTop.vue'

export default {
  name: 'App',
  components:{
    MyHeader,
    Footer,
    NavTop,
  }
}
</script>

<style>
</style>