<!-- to do 逐渐定义自己的初始化样式 2更改router结构 去掉空div -->
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
  },
}
</script>

<style>
/* 淘宝初始化样式*/
body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,button,textarea,p,blockquote,th,td { margin:0; padding:0; }
body { background:#fff; color:#555; font-size:14px; font-family: Verdana, Arial, Helvetica, sans-serif; }
td,th,caption { font-size:14px; }
address, caption, cite, code, dfn, em, strong, th, var { font-style:normal; font-weight:normal;}
a {text-decoration:none;}
img { border:none; }
ol,ul,li { list-style:none; }
input, textarea, select, button { font:14px Verdana,Helvetica,Arial,sans-serif; }
table { border-collapse:collapse; }
html {overflow-y: scroll;}
.btn-disabled{
  cursor:not-allowed;
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