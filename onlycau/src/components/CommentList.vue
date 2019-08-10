<template>
  <div> 
    <div class="comment" v-for="comment in comments">
      <p class="comment.content">{{comment.content}}</p>
      <span class="comment.user">{{comment.username}}</span>
      <span class="comment.date">{{comment.date}}</span>
    </div>
    <div id="comment_page_turning">
      <span v-show='current_page - 1' @click='action(-1)'>上一页</span>
      <span v-show='current_page > 3' @click='action(-current_page+1)'>1</span>
      <span v-show='current_page > 4'>...</span>
      <span v-show='isShow(num)' v-for='num in list' @click='action(num)'><span v-show='num==0'>|</span>{{current_page + num}}</span>
      <span v-show='current_page + 3 < max_page'>...</span>
      <span v-show='current_page + 2 < max_page' @click='action(max_page- current_page)'>{{max_page}}</span>
      <span v-show='current_page < max_page' @click='action(1)'>下一页</span>
    </div>
  </div>
</template>
<script>
export default{
  name:'CommentList',
  data:function(){
    return {
      comments:{},
      url: this.$Global.url + '/api/comments?begin=',
      begin: 0,
      comments_count: 0,
      current_page: 1,
      per_page_count:10,
      max_page:0,
      list:[-2,-1,0,1,2],
    }
  },
  props:['table'],
  created(){
    this.select_comment(0)
  },
  methods:{
    isShow(num){
      if(this.$data.current_page + num > 0 && this.$data.current_page + num <= this.$data.max_page){
        return true
      }
    },
    action(n){
      this.$data.current_page = this.$data.current_page + n
      this.select_comment(this.$data.current_page * 10)
    },
    select_comment(begin){
      let url = this.$data.url + begin +'&table=' + this.table
      this.$axios.get(url).then((response)=>{
        let middle
        [middle, ...this.$data.comments] = response.data
        this.$data.comments_count = middle.count
        this.$data.max_page = ((middle.count - (middle.count % this.$data.per_page_count)) / this.$data.per_page_count)
      })
    }
  }
}
</script>
<style>
#comment_page_turning{
  text-align: center;
}
#comment_page_turning > span{
  margin-left: 5px;
  margin-right: 5px;
  cursor: pointer;
}
#comment_page_turning > span:hover{
  background-color: green;
}
</style>