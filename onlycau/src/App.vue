<template>
    <div id="app">
      <MyHeader></MyHeader>
      <router-view></router-view>
      <Footer></Footer>
      <WriteBlog></WriteBlog>
    </div>
</template>

<script>
import MyHeader from './components/MyHeader.vue'
import Footer from './components/Footer.vue'
import WriteBlog from './WriteBlog.vue'

export default {
  name: 'App',
  components:{
    MyHeader,
    Footer,
    WriteBlog,
  }
}
</script>

<style>
</style>