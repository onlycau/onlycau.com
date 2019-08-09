<template>
  <div id="welcome">
    <span id="welcome_">欢迎来访</span>
    <div id="is_logged">
      <div v-if='logged'>
        <span id="sign_in" @click="to_('sign_in')">{{name}}</span>
        <span id="sign_up" @click="to_('sign_out')">退出</span>
      </div>
      <div v-else>
        <span @click="to_('sign_in')">登录</span>
        <span @click="to_('sign_up')">注册</span>
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'Welcome',
  data:function(){
    return {
      logged:0,
      name:'',
    }
  },
  created(){
    this.is_logged()
  },
  watch:{
    // 检测路由参数变化 手动重新请求博客摘要内容然后回流重绘页面
    $route(){
      this.is_logged()
    }
  },
  methods:{
    is_logged(){
      const url = 'http://127.0.0.1:5000/user/is_logged'
      this.$axios.get(url).then((response)=>{
        if (response.data.logged === 1){
          this.name = response.data.name
          this.logged = 1
        }
        else{
          this.logged = 0
        }
      })
    },
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
#is_logged{
  float: right;
}
#is_logged span{
  color: green;
  margin-right: 10px;
  cursor: pointer;
}
#is_logged > span:hover{
  color: red;
}
</style>