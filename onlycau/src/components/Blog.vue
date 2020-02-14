<template>
  <div id="blog">
    <div id="blog_title_blog">{{data.title}}</div>
        <div>
          <span id="blog_date_blog">{{data.date}}</span>
          <span id="blog_author_blog">{{data.author}}</span>
        </div>
    <div id="blog_text_blog" v-html='data.html'></div>
    <Comment :blog_id='id'></Comment>
  </div>
</template>

<script>
import Comment from './Comment'
export default{
  name:'Blog',
  components:{
    Comment
  },
  data:function(){
    return{
      data:{
        data:{}
      },
      blog_id:this.$route.params.blog_id,
      id:this.$route.params.blog_id
    }
  },
  mounted(){
    this.get_blog(this.blog_id)
  },
  methods:{
    get_blog(id){
      const url = this.$Global.url + '/api/blog/select_blog?blog_id=' + id
      this.$axios.get(url).then((response)=>{
        this.$data.data = response.data
      })
    }
  },
}
</script>

<style scoped>
#blog_title_blog{
  font-size: 200%;
  text-align: center;
  margin: 20px 5px 20px 5px;
}
#blog_text_blog{
  margin-top: 20px;
  margin-bottom: 20px;
}
#blog_date_blog{
  font-size: 120%;
  margin-right: 20px;
}
#blog_author_blog{
  font-size: 120%;
  color: blue;
}
</style>