<!-- to do 改变留言后反馈 -->
<template>
  <div id="new_comment">
    <div>
      <span>给我留言</span>
    </div>
      <textarea id="comment_content" v-model="content" placeholder="写点什么..." /><br>
      <input v-model="username" placeholder="昵称" /><br>
      <input v-model="mailbox" placeholder="邮箱" /><br>
      <input id="comment_submit" type="button" @click='submit_comment()' value="提交评论"/>
  </div>
</template>
<script>
export default{
  name:'NewComment',
  props:['table_name'],
  data:function(){
    return {
      url:this.$Global.url + '/api/new_comment',
      content: '',
      username: '',
      mailbox: '',
    }
  },

  methods:{
    submit_comment(){
      let comment = {
        'content': this.content,
        'username': this.username,
        'mailbox': this.mailbox,
        'table_name': this.table_name,
        }
      this.$axios.post(this.url,comment).then((response)=>{
        if(response.data === 1){
          alert('ok')
          this.$router.go(0)
        }else{
          alert('Something wrong')
        }
      })
    },
  },
}
</script>
<style>
#new_comment span{
  margin: 5px;
}
#new_comment input{
  margin: 5px;
}
#comment_content{
  width: 90vw;
  margin: 10px 0 10px 5px;
  font-size: 140%;
  background-color: #eee;
}
</style>