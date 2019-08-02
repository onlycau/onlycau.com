<template>
  <div v-if='data'>
     <div class='overview'>
      <div class='overview_top'>
        <span class='blog_type'>{{data.blog_type}}</span>
        <span class='blog_title' @click="to_blog">{{data.title}}</span>
      </div>
      <div class='blog_text'>
        <p>{{data.text}}</p>
      </div>
      <div class='overview_bottom'>
        <span class='blog_author'>作者:{{data.author}}</span>
        <span class='blog_date'>时间:{{data.date}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    name:'BlogSummary',
    data:function(){
      return {}
    },
    props:['data'],
    methods:{
      to_blog:function(){
        this.$router.push('/blog/'+this.data.id)
      }
    }
  }
</script>

<style type="text/css">
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
.blog_type{
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