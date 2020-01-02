<!-- 第一次加载 如果宽度较小时去掉logo 减少所占高度 -->
<template>
  <div id="header">
    <div id="logo" v-if='client_width>415'>
      <img id="logo" src="../assets/logo_book2.png">
    </div>
    <div id="title" :class="{phone:client_width<416}">
      <h1><a href="http://onlycau.com">Onlycau的小站</a></h1>
    </div>
  </div>
</template>
<script>
  export default{
    name: 'MyHeader',
    data(){
      return{
        client_width:document.body.clientWidth
      }
    }
  }
</script> 

<style type="text/css">
#header{
  display: flex;
  display: -webkit-flex;
  width: auto;
  margin-right: 3px;
  align-items: center;
  background-color: #D1BA74;
}
#title{
  flex: 1;
  text-align: center;
}
#title h1{
  font-size: 300%;
  color: black;
}
/* 手机显示*/
.phone{
  height: 100px;
  line-height: 100px;
}
</style>