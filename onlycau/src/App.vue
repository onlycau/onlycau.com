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
/*css 图形*/
.square{
  width:100%;
  height:100%;
  background-color: red;
}
.rectangle{
  width: 100%;
  height: 60%;
  background-color: red;
}
.circle{
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: red;
}
.oval{
  width:100%;
  height: 50%;
  border-radius: 50%;
  background-color: red;
}
.triangle_down{
  width: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-top: 100px solid red;
}
</style>