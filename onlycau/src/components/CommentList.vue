<template>
  <div> 
    <div class="comment" v-for="comment in comments" :key='comment.id'>
      <p class="comment-content">{{comment.content}}</p>
      <span class="comment-user">{{comment.username}}</span>
      <span class="comment-date">{{comment.date}}</span>
    </div>
    <div class="comments_page_turning">
      <span class="btn-page_turning" :class="{'btn-disabled':current_page<=1}" @click='jump_page(-1)'><上一页</span>
      <span v-show='current_page > 3' @click='jump_page(-current_page+1)'>1</span>
      <span class='ellipsis' v-show='current_page > 4'>...</span>
      <span 
        v-for='num in list' 
        :key='num.id' 
        :class="{'current_page':num===0}"
        v-show='is_show(num)' 
        @click='jump_page(num)'
      >{{current_page + num}}</span>
      <span class="ellipsis" v-show='current_page + 3 < max_page'>...</span>
      <span v-show='current_page + 2 < max_page' @click='jump_page(max_page- current_page)'>{{max_page}}</span>
      <span class="btn-page_turning" :class="{'btn-disabled':current_page>=max_page}" @click='jump_page(1)'>下一页></span>
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
  props:['table_name'],
  created(){
    this.select_comment(0)
  },
  methods:{
    is_show(num){
      if(this.current_page + num > 0 && this.current_page + num <= this.max_page){
        return true
      }
    },
    jump_page(n){
      this.current_page = this.current_page + n
      this.select_blogs(this.current_page * this.per_page_count)
    },
    select_comment(begin){
      let url = this.$data.url + begin +'&table_name=' + this.table_name
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
.btn-disabled{
  pointer-events: none;
  color: #CACACA;
}
/* 评论 */
.comment{
  margin:20px;
  padding: 10px 15px;
  line-height: 25px;
  width: 800px;
  background: #FAFAFA;
  border: 1px #EEE solid;
  border-radius: 3px;
  font-size: 14px;
}
.comment-content{
  color: #111;
}
.comment-user{
  margin-right: 10px;
  color:#CCC;
}
.comment-date{
  color:#CCC;
}
/* 翻页栏*/
.comments_page_turning{
  margin-top: 20px;
  text-align: center;
}
.btn-page_turning{
  background-color: #EEE;
}
.btn-page_turning:hover{
  background-color: #FFF;
}

.comments_page_turning > span:not([class="ellipsis"]){
  padding: 2px 6px;
  margin: 0 1px 0 2px;
  border:solid 1px #ccc;
  border-radius: 2px;
  cursor: pointer;
}
.current_page{
  background-color: red;
  color:white;
}
.comments_page_turning > span:not([class="btn-page_turning"],[class="ellipsis"]):hover{
  background-color: red;
  color:white;
}
</style>