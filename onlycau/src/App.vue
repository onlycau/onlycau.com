<template>
  <div id="app">
    <div v-if='show_header'>
      <MyHeader></MyHeader>
      <NavTop></NavTop>
      <Welcome></Welcome>
      <router-view></router-view>
      <Footer></Footer>
    </div>
    <div v-else>
      <router-view></router-view>
    </div>
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
  },
  computed:{
    show_header(){
      return this.$route.path !== '/author'
    }
  }

}
</script>

<style>
*{
  margin: 0px;
  padding: 0px;
}
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