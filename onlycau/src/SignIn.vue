<!-- to do 输入提示 请求加密 登录提示-->
<template>
  <div id="for_center">
    <div id="sign_in">
      <div id="head">
        <span>用户登录</span>
      </div>
      <div id="tips">
        <span v-show=''>!你还没有输入账号</span>
      </div>
      <div id="name">
        <input v-model='name' placeholder="用户名">
      </div>
      <div id="password">
        <input v-model='password' placeholder="密码">
      </div>
      <div id="my_submit">
        <span @click='my_submit()'>登录</span>
      </div>
      <div id="help">
        <span>忘了密码?</span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name:'SignIn',
  data:function(){
    return {
      url:this.$Global.url + '/user/sign_in',
      name:'',
      password:'',
    }
  },
  methods:{
    my_submit(){
      const data = {
        'name': this.name,
        'password': this.password
      }
      alert('wait')
      this.$axios.post(this.$data.url, data).then((response)=>{
        if(response.data == 1){
          this.$router.replace('/')
        }
        else if(response.data == -1){
          alert('用户名或者密码错误')
        }
        else{
          alert('某些奇怪的事发生了')
          this.$router.go(0)
        }
      })
    },
  }
}
</script>
<style scoped>
#sign_in{
  font-size: 110%;
  width: 300px;
  border-style:solid;
  border-radius: 5px;
  border-color: #A0b1C4;
  border-width: 2px;
}
#head{
  height: 50px;
  background-color: #F9FBFE;
  text-align: center;
  margin-bottom: 10px;
}
#head span{
  color: #333;
  /*居中线*/
  line-height: 50px;
}
#tips{
  font-size: 100%;
  height: 25px;
  text-align: center;
  line-height: 25px;
  color: red;
}
#sign_in input{

  height: 25px;
  min-height: 25px;
  width: 240px;
  padding-left: 10px;
  padding-right: 10px;
  margin-left: 18px;
  margin-top: 10px;
}
#my_submit{
  color: #384728;
  font-size: 120%;
  margin-top: 20px;
  margin-left: 20px;
  margin-right: 20px;
  height: 30px;
  cursor: pointer;
  text-align: center;
  background-color: #1E90FF;
}
#my_submit span{
  color: white;
  line-height: 30px;
}
#help{
  font-size: 80%;
  height: 20px;
  margin-top: 10px;
  margin-left: 70%;
  margin-bottom: 10px;
  cursor: pointer;
}
</style>