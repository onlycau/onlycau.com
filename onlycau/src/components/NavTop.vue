<template>
  <div>
    <nav id="nav_top">
      <ul>
        <li @click="to_blogs('all')">首页</li>
        <li @mouseover='show_dropdown()' @mouseleave='dis_dropdown()' @click = 'dis_dropdown()'><router-link to='/blogs/all'>学习笔记</router-link>
          <div id="dropdown">
            <span class="drop_content" @click="to_blogs('JavaScript')">JavaScript</span><br>
            <span class="drop_content" @click="to_blogs('HTML')">HTML</span><br>
              <span class="drop_content" @click="to_blogs('Python')" >Python</span><br>
              <span class="drop_content" @click="to_blogs('Others')">Other</span><br>
          </div>
        </li>
        <li><a href="">个人简历</a></li>
        <li><router-link to='/message'>给我留言</router-link></li>
      </ul>
    </nav>
  </div>
</template>

<script>
  export default{
    name:'NavTop',
    methods:{
      show_dropdown(){
        document.getElementById('dropdown').style.visibility='visible',
        document.getElementById('dropdown').style.backgroundColor='#D1BA74'
      },
      dis_dropdown(){
        document.getElementById('dropdown').style.visibility='hidden'
      },
      to_blogs(blog_type){
        this.$router.push('/blogs/'+blog_type)
      },
  }
}
</script>

<style type="text/css">
#nav_top ul{
  margin: 0px;
  padding-left: 0px;
  background-color: #C8C8A9;
}
#nav_top ul>li{
  display: inline-block;
  font-size: 150%;
  text-align: center;
  width: 130px;
}
#nav_top ul>li:hover{
  background-color: #D1BA74;
}
#dropdown {
  /*visibility 代替display 重绘代替回流https://zhuanlan.zhihu.com/p/53913989*/
  visibility:hidden;
  position: absolute;
  text-align: left;
/*  width: 100px;*/
  padding-left: 15px;
  padding-right: 15px;
}
</style>