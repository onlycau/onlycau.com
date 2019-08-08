<template>
  <div id="welcome">
    <span id="welcome_">欢迎来访</span>
    <div id="sign_in_up" v-if='true'>
      <span id="sign_in" @click="to_('sign_in')">登录</span>
      <span id="sign_up" @click="to_('sign_up')">注册</span>
    </div>
    <div v-else></div>
  </div>
</template>
<script>
export default{
  name:'Welcome',
  methods:{
    to_(url){
      this.$router.push('/user/' + url)
    }
  }
}
</script>
<style>
#welcome{
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 5px;
}
#sign_in_up{
  float: right;
}
#sign_in_up span{
  color: green;
  margin-right: 10px;
  cursor: pointer;
}
#sign_in_up > span:hover{
  color: red;
}
</style>