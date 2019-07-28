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

    <div id="summary">
      <BlogSummary :data='data[1]'></BlogSummary>
      <BlogSummary :data='data[2]'></BlogSummary>
<!--     <BlogSummary :data='data[3]'></BlogSummary>
      <BlogSummary :data='data[4]'></BlogSummary>
      <BlogSummary :data='data[5]'></BlogSummary> -->
    </div>

    <div id="PageTurning">
      <!-- 待优化 1.直接点击序号跳转页面 2.跳页 3.样式更新-->
      <div v-if='max_page > 1'>
        <span v-if='current_page > 1' @click="get_summary(sort,--current_page)">&lt;</span>
        <span v-if='current_page > 2'>{{current_page - 2}}</span>
        <span v-if='current_page > 1'>{{current_page - 1}}</span>
        <span id="current_page">{{current_page}}</span>
        <span v-if='current_page < max_page '>{{current_page + 1}}</span>
        <span v-if='current_page < max_page - 1'>{{current_page + 2}}</span>
        <span v-if='current_page < max_page' @click="get_summary(sort,++current_page)">&gt;</span>
      </div>
    </div>
  </div>
</template>

<script>
  import BlogSummary from './BlogSummary.vue'

  export default{
    name:'NavPage',
    components:{
      BlogSummary:BlogSummary,
    },
    data:function(){
      return {
        data:{},
        url:'http://127.0.0.1:5000/get_blogs/?sort=',
        sort:'homepage',
        current_page:1,
        max_page:1,
        count: 2,
      }
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
      get_summary(sort='homepage', current_page=1){
        var url = this.$data.url + sort + '&begin=' + (current_page*2-2)
        this.$axios.get(url).then((response)=>{
          this.$data.data = response.data
          this.$data.max_page = response.data[0].blog_count/2
          this.$data.sort = sort;
          this.$data.current_page = current_page;
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
  /* 翻页栏*/
  #PageTurning{
    font-size: 150%;
    text-align: center;
    margin:10px 10px 10px 10px;
  }
  #current_page{
    color: red;
  }
</style>