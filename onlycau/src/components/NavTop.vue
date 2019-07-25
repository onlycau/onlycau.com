<template>
  <div>
    <nav id="nav_top">
      <ul>
        <li><a href="http://127.0.0.1:5000/">首页</a></li>
        <li v-on:mouseover='show_dropdown()' v-on:mouseleave='dis_dropdown()' @click = 'dis_dropdown()'><a href="">学习笔记</a>
          <div id="dropdown">
            <span class="drop_content">JavaScript</span><br>
            <span class="drop_content">HTML</span><br>
            <span class="drop_content" @click="get_summary('python')">Python</span><br>
            <span class="drop_content" @click="get_summary('others')">Other</span><br>
          </div>
        </li>
        <li><a href="">个人简历</a></li>
      </ul>
    </nav>

    <BlogSummary :data='data[0]'></BlogSummary>
    <BlogSummary :data='data[1]'></BlogSummary>
    <BlogSummary :data='data[2]'></BlogSummary>
    <BlogSummary :data='data[3]'></BlogSummary>
    <BlogSummary :data='data[4]'></BlogSummary>
  </div>
</template>

<script>
  import BlogSummary from './BlogSummary.vue'

  export default{
    name:'NavTop',
    data:function(){
      return {
        data:{},
        url:'http://127.0.0.1:5000/get_blogs/?sort='
      }
    },
    components:{
      BlogSummary:BlogSummary
    },
    mounted(){
      this.get_summary('homepage')
    },
    methods:{
      show_dropdown(){
        document.getElementById('dropdown').style.display='block',
        document.getElementById('dropdown').style.backgroundColor='#D1BA74'
      },
      dis_dropdown(){
        document.getElementById('dropdown').style.display='none'
      },
      get_summary(sort){
      this.$axios.get(this.$data.url + sort).then((response)=>{
        this.$data.data = response.data
      })
          }
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
  display: none;
  position: absolute;
  text-align: left;
/*  width: 100px;*/
  padding-left: 15px;
  padding-right: 15px;
}
/* 博客文章概览的样式 */
.overview{
  margin: 30px 10px 0px 10px;
}
.overview_top{
  text-align: left;
}
.overview_bottom{
  text-align: right;
}
.blog_sort{
  color: red;
}
.blog_title{
  font-size: 150%;
  color: green;
  padding-left: 30px;
}
.blog_author{
  color: red;
  padding-right: 20px;
}
.blog_date{
  padding-right: 10px;
}
</style>