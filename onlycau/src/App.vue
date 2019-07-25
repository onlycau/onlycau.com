<template>
    <div id="app">
      <MyHeader msg='hello vue'></MyHeader>
      <NavTop></NavTop>
      <router-link to="/sign_in">登录</router-link>
      <router-view></router-view>
      <Footer></Footer>
    </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
import NavTop from './components/NavTop.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    MyHeader,
    NavTop,
    Footer,
  }
}
</script>

<style>
a{
  text-decoration: none;
  outline: none;
  color: #FE4365;
}
</style>