<template>
  <div class="blogsummary" v-if='data'>
     <div class='overview'>
      <div class='overview_top'>
        <span class='blog_type' @click="to_blogs(data.blog_type)">{{data.blog_type}}</span>
        <span class='blog_title' @click="to_blog()">{{data.title}}</span>
      </div>
      <div class="overview_mid">
        <div>
          <a :href='picture_author'><img :src='random_picture'/></a>
        </div>
        <div class='blog_text'>
          <p>{{data.summary}}</p>
        </div>
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
    return {
      pictures : this.$Global.pictures,
      random_picture : '',
      picture_author: '',
    }
  },
  created(){
    let picture_links = Object.keys(this.pictures)
    this.random_picture = picture_links[Math.round(Math.random() * (picture_links.length - 1))]
    this.picture_author = this.pictures[this.random_picture]
  },
  props:['data'],
  methods:{
    to_blogs(blog_type){
      this.$router.replace('/blogs/'+blog_type)
    },
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
/*分类 标题*/
.blog_type{
  color: red;
  cursor: pointer;
}
.blog_title{
  font-size: 150%;
  color: green;
  padding-left: 30px;
  cursor: pointer;
}
/*正文 配图*/
.overview_mid{
  display: flex;
  margin-top: 10px;
  margin-bottom: 10px;
}
.blogsummary img{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 100px;
}
.blog_text{
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 20px;
}
/*作者 事件*/
.blog_author{
  color: red;
  padding-right: 20px;
}
.blog_date{
  padding-right: 10px;
}
</style>