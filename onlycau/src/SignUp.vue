<!--  !!!需要绑定的样式一定要提前理一遍 哪些样式与这属性有关 别后面再一个一个添加属性
      to do 1单个输入选项构建一个组件 传入属性和文本 2登录注册信息加密 3 属性绑定优化 
      4 this.wait 添加注册请求时候的等待图标-->
<template>
  <div id="for_center">
    <div id="sign_up">

      <div id="username">
        <input :class="border_color('name')" v-model='name' placeholder="用户名" maxlength='12' @focus="change('name',1)" @blur="change('name',0)"/>
        <div v-show='on_name+1'>
          <div class="name_point" v-show='!on_name&&!name_a'>
            <span v-if='name_a'>√</span>
            <span v-else>!</span>
            <span>密码不能为空</span>
          </div>
          <div class="name_point" v-show='on_name ||!name_b'>
            <span v-if='name_b'>√</span>
            <span v-else>!</span>
            <span>不能包含空格</span>
          </div>
          <div class="name_point" v-show='name_a && name_b && !name_c || on_name'>
            <span v-if='name_c'>√</span>
            <span v-else>!</span>
            <span>长度为3-12个字符</span>
          </div>
          <div class="name_point" v-show='name_a && name_b && name_c && (!name_d) && (!on_name)'>
            <span>!用户名已存在</span>
          </div>
        </div>
      </div>

      <div id="password">
        <input :class="border_color('password')" v-model='password' placeholder='密码' maxlength="12" @focus="change('password',1)" @blur="change('password',0)">
        <div v-show='on_password+1'>
          <div class="password_point" v-show='!on_password&&!password_a'>
            <span v-if='password_a'>√</span>
            <span v-else>!</span>
            <span>密码不能为空</span>
          </div>
          <div class="password_point" v-show='on_password ||!password_b'>
            <span v-if='password_b'>√</span>
            <span v-else>!</span>
            <span>不能包含空格</span>
          </div>
          <div class="password_point" v-show='password_a && password_b && !password_c || on_password'>
            <span v-if='password_c'>√</span>
            <span v-else>!</span>
            <span>长度为8-12个字符</span>
          </div>
          <div class="password_point" v-show='password_a && password_b && password_c && !password_d || on_password '>
            <span v-if='password_d'>√</span>
            <span v-else>!</span>
            <span>必须包含字母、数字、符号中两种</span>
          </div>
        </div>
      </div>

      <div id="password_twice">
        <input :class="border_color('password_twice')" v-model='password_twice' placeholder="确认密码" maxlength="12" @focus="change('password_twice', 1)" @blur="change('password_twice', 0)">
        <div v-show='(on_password_twice || (password != password_twice)) && (on_password_twice + 1)'>
          <span v-if='password == password_twice'>√</span>
          <span v-else>!</span>
          <span>密码一致</span>
        </div>
      </div>

      <div id="mailbox">
        <input :class="border_color('mailbox')" v-model='mailbox' placeholder="邮箱" maxlength="24" @focus="change('mailbox', 1)" @blur="change('mailbox', 0)">
        <div v-show='(on_mailbox || (!is_mailbox)) && (on_mailbox + 1)'>
          <span v-if='is_mailbox'>√</span>
          <span v-else>!</span>
          <span>一个可使用的邮箱</span>
        </div>
      </div>

      <div id="submit" v-if='allow_submit' @click='sign_up' v-show='!wait'>
        <button>立即注册</button>
      </div>
      <div id="submit_point" v-else>
        还有啥木有填好
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'SignUp',
  data:function(){
    return {
      url:'http://127.0.0.1:5000/user/sign_up',
      name:'',
      on_name:-1,
      name_d:false,
      password:'',
      on_password:-1,
      password_twice:'',
      on_password_twice:-1,
      mailbox:'',
      on_mailbox:-1,
      wait:false,
    }
  },
  computed:{
    name_a:function(){
      return (this.name.length > 0)
    },
    name_b:function(){
      return (this.name.indexOf(' ')==-1)
    },
    name_c:function(){
      return (this.name.length > 2)
    },
    password_a:function(){
      return (this.password.length > 0)
    },
    password_b:function(){
      return (this.password.indexOf(' ')==-1)
    },
    password_c:function(){
      return (this.password.length > 7)
    },
    password_d:function(){
      return ((/[0-9]/.test(this.password) + /[a-zA-Z]/.test(this.password) + /[^a-zA-Z0-9\s]/.test(this.password)) > 1)
    },
    is_mailbox:function(){
      return  /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/.test(this.mailbox)
    },
    allow_submit:function(){
      return this.name_d && this.password_a &&this.password_b && this.password_c && this.password_d &&this.is_mailbox && (this.password === this.password_twice)
    }
  },
  methods:{
    border_color(which){
      switch(which){
        case 'name':
        return this.on_name? 'active' : (this.name_d? '' : 'wrong')
        case 'password':
        return this.on_password? 'active' : ((this.password_a && this.password_b && this.password_c && this.password_d)? '' : 'wrong')
        case 'password_twice':
        return this.on_password_twice ? 'active' : ((this.password === this.password_twice)? '' : 'wrong')
        case 'mailbox':
        return this.on_mailbox? 'active' : (this.is_mailbox ? '' : 'wrong')
      }
    },
    change(which, n){
      switch(which){
        case 'name':
        this.on_name = n
        this.check_name()
        break;
        case 'password':
        this.on_password = n
        break;
        case 'password_twice':
        this.on_password_twice = n
        break;
        case 'mailbox':
        this.on_mailbox = n
        break;
      }
    },
    check_name(){
      if(this.name_a && this.name_b && this.name_c){
        const url = this.url + '?name=' +this.name
        this.$axios.get(url).then((response)=>{
          if (response.data[0] == 0){
            this.name_d = true
          }
          else{
            this.name_d = false
          }
        })
      }
      else{
        this.name_d = false
      }
    },
    sign_up(){
      let user = {
        'name':this.name,
        'password':this.password,
        'mailbox':this.mailbox,
      }
      this.wait = true
      this.$axios.post(this.url, user).then((response)=>{
        if (response.data == 1){
          this.wait = false
          alert('注册成功')
          this.$router.replace('/user/sign_in')
        }
        else{
          alert('某些意外的情况发生了')
        }
        })
    }
  },
}
</script>
<style>
#for_center{
  margin-top: 150px;
  margin-bottom: 150px;
  display: flex;
  justify-content: center;
}
#sign_up{
  font-size: 110%;
}
#sign_up > div{
  margin-bottom: 20px;
  width: 300px;
}
#sign_up input{
  font-size: 110%;
  width: 100%;
  height: 30px;
  padding-left: 10px;
  padding-right: 10px;
}
#submit{
  text-align: center;
}
#submit_point{
  color: red;
  text-align: center;
}
.active{
  border-color: #1E90FF;
}
.wrong{
  border-color: #e0202073;
}
</style>