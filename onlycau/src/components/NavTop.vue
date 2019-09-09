<!-- to do 如果链接为当前路径 链接背景色改变 -->
<template>
  <nav id="nav_top">
    <NavTopChild :sth='one'></NavTopChild>
    <NavTopChild :sth='two'></NavTopChild>
    <NavTopChild :sth='three'></NavTopChild>
    <NavTopChild :sth='four'></NavTopChild>
    <NavTopChild :sth='five'></NavTopChild>
    <NavTopChild :sth='six'></NavTopChild>
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
      one:{
        url:'home',
        name:'首页',
        types:[],
      },
      two:{
        url:"blogs/个人日记,计划总结",
        name:'生活随笔',
        types:['个人日记', '计划总结']
      },
      three:{
        url:"blogs/HTML,JavaScript,Python,Others",
        name:'学习记录',
        types:['HTML', 'JavaScript', 'Python', 'Others'],
      },
      four:{
        url:'blogs/软件配置,软件指令',
        name:'备忘录',
        types:['软件配置','软件指令']
      },
      five:{
        url:'author',
        name:'关于博主',
        types:[],
      },
      six:{
        url:'message',
        name:'给我留言',
        types:[],
      },
    }
  },
}
</script>

<style type="text/css">
#nav_top{
  display: flex;
  width: 100vw;
  justify-content: space-between;
  font-size: 150%;
  background-color: #C8C8A9;
}
</style>