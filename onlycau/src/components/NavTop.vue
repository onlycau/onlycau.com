<!-- to do 如果链接为当前路径 链接背景色改变 -->
<template>
  <nav id="nav_top">
    <NavTopChild v-for='item in items' :nav_data='item' :key='item.id'></NavTopChild>
  </nav>
</template>

<script>
import NavTopChild from './NavTopChild.vue'
export default{
  name:'NavTop',
  components:{
    NavTopChild,
  },
  data(){
    return {
      items: [{
        url:'/home',
        name:'首页',
        types:[],
      },
      {
        url:"/blogs/个人日记,计划总结",
        name:'生活随笔',
        types:['个人日记', '计划总结']
      },
      {
        url:"/blogs/HTML,JavaScript,Python,Others",
        name:'学习记录',
        types:['HTML', 'JavaScript', 'Python', 'Others'],
      },
      {
        url:'/blogs/软件配置,软件指令',
        name:'备忘录',
        types:['软件配置','软件指令']
      },
      {
        url:'/author',
        name:'关于博主',
        types:[],
      },
      {
        url:'/message',
        name:'给我留言',
        types:[],
      }]
    }
  },
}
</script>

<style type="text/css">
#nav_top{
  display: flex;
  width: auto;
  margin-right: 3px;
  justify-content: space-between;
  flex-wrap: wrap;
  font-size: 150%;
  background-color: #C8C8A9;
}
</style>