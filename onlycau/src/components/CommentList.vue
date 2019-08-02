<template>
  <div>
    <div class="comment" v-for="comment in comments">
      <p class="comment.content">{{comment.content}}</p>
      <span class="comment.user">{{comment.username}}</span>
      <span class="comment.date">{{comment.date}}</span>
    </div>
  </div>
</template>
<script>
export default{
  name:'CommentList',
  data:function(){
    return {
      comments:{},
      url:'/api/select_web_comments?begin=',
      begin:0,
    }
  },
  mounted(){
    this.select_comment(0)
  },
  methods:{
    select_comment(begin){
      let url = this.$data.url + begin
      this.$axios.get(url).then((response)=>{
        this.$data.comments = response.data
        this.$data.comments.shift()
      })
    }
  }
}
</script>