function change_display(classname, i, display = false){
  if(display){
    document.getElementsByClassName(classname)[i].style.display = 'block'
  }
  else{
      document.getElementsByClassName(classname)[i].style.display = 'none'
  }
}

new Vue({
  el:'#sign_up',
  data:{
    name:'',
    password:'',
    name_right: false,
    password_right: false,
  },
  computed:{
    access_submit:function(){
      return this.name_right + this.password_right == 2
    }
  },
  methods:{
    check_name:function(){
      if (!this.name){
        change_display('name_point', 0, 1)
      }
      else if(this.name.indexOf(' ')!==-1){
        change_display('name_point', 1, 1)
      }
      else{
        this.name_right = true
      }
    },
    focus_name:function(){
      for(var i=0; i<3; i++){
        change_display('name_point', i)
      }
    },
    check_password:function(){
      for(var i=0; i<3; i++){
        change_display('password_point', i+1)
      }
      if (!this.password){
        change_display('password_point', 0 ,1)
      }
      else if(this.password.indexOf(' ')!==-1){
        change_display('password_point', 1, 1)
        }
      else if(this.password.length < 8){
        change_display('password_point', 2, 1)
      }
      else if ((/[0-9]/.test(this.password) + /[a-zA-Z]/.test(this.password) + /[^a-zA-Z0-9\s]/.test(this.password)) < 2){
        change_display('password_point',3 ,1)
      }
      else{
        this.password_right = true
      }
    },
    focus_password:function(){
      change_display('password_point', 0)
      for(var i=0; i<3; i++){
        change_display('password_point', i+1, 1)
      }
    },
    my_submit:function(){
      var url = '/sign_up/?name=' + this.name + '&password=' + this.password
      xmlhttp = new XMLHttpRequest()
      xmlhttp.open('get', url, false)
      xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded")
      xmlhttp.send()
      status_code = Number(xmlhttp.responseText)
      switch(status_code){
        case -1:
          alert('此用户名已存在');
          break;
        case 1:
        alert('注册成功')
        window.location = '/sign_in/'
        window.location.reaload()
      }

    }
  },
})