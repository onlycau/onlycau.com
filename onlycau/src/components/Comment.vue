<template>
  <div> 
    <div id="new_comment">
        <textarea id="comment-box" v-model="content" :placeholder="place_holder_reply" /><br>
        <input v-model="username" placeholder="昵称" /><br>
        <div id="comment-submit">
          <span v-show="is_show_btn_cancel" class="btn-reply btn-cancle" @click="cancel_relpy()">取消回复</span>
          <span class="btn-reply btn-red" @click='submit_comment()'>发表评论</span>
        </div>
    </div>

    <div 
    class="comment-list" 
    v-for="comment in comments"
    :key='comment.id'
    @mouseenter="change_is_show_btn_reply(comment,true)"
    @mouseleave="change_is_show_btn_reply(comment,false)">
      <div>
        <p class="comment-content">{{comment.content}}</p>
        <span class="comment-user">{{comment.username}}</span>
        <span class="comment-date">{{comment.date}}</span>
        <span v-show="comment.count" class="btn-reply-see" @click='is_show_reply=!is_show_reply'>{{is_show_reply?'隐藏':'查看'}}回复({{comment.count}})</span>
        <span v-show="comment.is_show_btn_reply" @click='change_reply_to(comment.username,comment.id)' class="btn-reply-new">回复</span>
      </div>
      <div v-if="comment.replys"  v-show='is_show_reply' class="reply">
        <div 
        class="replay-item" 
        v-for="item in comment.replys"
        :key="item.id"
        @mouseenter="change_is_show_btn_reply(item,true)"
        @mouseleave="change_is_show_btn_reply(item,false)">
          <span class="name-reply-from">{{item.username}}</span>
          <span class="reply-word">回复</span>
          <span class="name-reply-to">{{item.to_name}}</span>
          <span class="reply-time">{{item.date}}</span>
          <span v-show="item.is_show_btn_reply" @click='change_reply_to(item.username,comment.id)' class="btn-reply-new">回复</span>
          <p class="reply-content">{{item.content}}</p>
        </div>
      </div>
    </div>
    <div class="comments_page_turning">
      <span class="btn-page_turning" :class="{'btn-disabled':current_page<=1}" @click='jump_page(-1)'>&lt;上一页</span>
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
      <span class="btn-page_turning" :class="{'btn-disabled':current_page>=max_page}" @click='jump_page(1)'>下一页&gt;</span>
    </div>
  </div>
</template>
<script>
export default{
  name:'Comment',
  props:['blog_id'],
  data:function(){
    return {
      reply_to: false,
      is_show_btn_cancel: false,
      is_show_reply: false,
      place_holder_reply : "想对作者说点什么",
      content: '',
      username: '',
      comment_id: 0,
      comments:{},
      replys: {},
      // 翻页
      comments_url: this.$Global.url + '/api/comments?begin=',
      begin: 0,
      comments_count: 0,
      current_page: 1,
      per_page_count:10,
      max_page:0,
      list:[-2,-1,0,1,2],
    }
  },
  computed:{
    post(){
      return {
        blog_id:this.blog_id,
        comment_id: this.comment_id,
        from_uid: 0,
        to_uid: 0,
        username: this.username,
        to_name: this.reply_to,
        content: this.content
      }
    }
  },
  created(){
    this.select_comment(0)
  },
  methods:{
    submit_comment(){
      let url = this.$Global.url + '/api/new_comment'
      if (this.reply_to !== false){
        url = this.$Global.url + '/api/new_reply'
      }

      this.$axios.post(url,this.post).then((response)=>{
        if(response.data === 1){
          this.select_comment(this.reply_to !== false?this.begin:0)
        }else{
          alert('Something wrong')
        }
      })
    },
    change_reply_to(username,comment_id){
      this.comment_id = comment_id
      this.reply_to = username
      this.place_holder_reply = '回复：' + username
      this.is_show_btn_cancel = true
      document.querySelector("#comment-box").scrollIntoView(true)
    },
    change_is_show_btn_reply(item,key){
      if(item.is_show_btn_reply === null){
        this.$set(item,'is_show_btn_reply',true)
      }
      item.is_show_btn_reply = key
      this.$forceUpdate()
    },
    cancel_relpy(){
      this.is_show_btn_cancel = false
      this.reply_to = false
      this.place_holder_reply = "想对作者说点什么"
    },
    // 
    is_show(num){
      if(this.current_page + num > 0 && this.current_page + num <= this.max_page){
        return true
      }
    },
    jump_page(n){
      this.current_page = this.current_page + n 
      this.select_comment((this.current_page - 1) * this.per_page_count)
    },
    select_comment(begin){
      let url = this.$data.comments_url + begin +'&blog_id=' + this.blog_id
      this.$axios.get(url).then((response)=>{
        let middle
        [middle, ...this.$data.comments] = response.data
        this.$data.comments_count = middle.count
        this.$data.max_page = ((middle.count - (middle.count % this.$data.per_page_count)) / this.$data.per_page_count)
        for (let comment of this.$data.comments){
          let api_reply = this.$Global.url + '/api/replys?comment_id=' + comment.id
          this.$axios.get(api_reply).then((response)=>{
            comment.replys = response.data
            comment['count'] = response.data.length
            this.$forceUpdate()
          })
        }
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
/* 留言与回复 */
#new_comment{
  font-size: 12px;
  margin: 10px;
  width: 800px;
}
#comment-box{
  width: 800px;
  height: 60px;
  margin: 10px 0 10px 5px;
  padding: 4px 4px;
  font-size: 14px;
  background-color: #eee;
}
#comment-submit{
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}
span.btn-reply{
  font-size: 16px;
  height: 30px;
  line-height: 28px;
  min-width: 72px;
  margin-left: 20px;
  text-align: center;
  border: 1px solid #CA0C16;
  border-radius: 4px;
  padding: 0 8px;
  -webkit-appearance: button;
  transition: background-color .1s ease-in-out,border-color .1s ease-in-out;
  cursor: pointer;
}
span.btn-cancel{

}
span.btn-red{
  color: #FFF;
  background-color: #CA0C16;
}
/* 评论内容 */
.comment-list{
  margin: 20px;
  padding: 10px 15px;
  line-height: 25px;
  width: 800px;
  background: #FAFAFA;
  border: 1px #EEE solid;
  border-radius: 3px;
  font-size: 14px;
}
.comment-content{
  margin-bottom: 4px;
  margin-left: 20px;
  color: #111;
}
.comment-user{
  margin-right: 10px;
  color:#CCC;
  font-family: 'PingFangSC-Semibold';
  font-weight: bold;
}
.comment-date{
  color:#CCC;
}
/* 回复 */
span.btn-reply-new{
  float: right;
  color: #79A5E5;
  margin-right: 20px;
  cursor: pointer;
}
span.btn-reply-see {
  float: right;
  color: #79A5E5;
  margin-right: 10px;
  cursor: pointer;
}
p.reply-content{
  margin-left: 60px;
}
span.name-reply-from{
  color: #2E2E2E;
  margin-left: 30px;
  margin-right: 20px;
  font-family: 'PingFangSC-Semibold';
  font-weight: bold;
}
span.reply-word{
  color: #999;
}
span.name-reply-to{
  color: #2E2E2E;
  margin-left: 20px;
  margin-right: 20px;
  font-family: 'PingFangSC-Semibold';
}
span.reply-time{
  color: #CCC;
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