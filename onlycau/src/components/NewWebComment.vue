<template>
  <div id="new_web_comment">
    <div>
      给我留言
    </div>
    <form action="/api/new_web_comment" method="get">
      <textarea id="web_comment_content" name="content" placeholder="写点什么..." /><br>
      <input id="web_comment_name" type="text" name="username" placeholder="昵称" /><br>
      <input id="web_comment_name" type="text" name="mailbox" placeholder="邮箱" /><br>
      <input id="web_comment_submit" type="submit" value="提交评论"/>
    </form>
    <CommentList></CommentList>
  </div>
</template>
<script>
import CommentList from './CommentList.vue'
export default{
  name:'NewWebComment',
  components:{
    CommentList:CommentList
  }
}
</script>
<style>
#new_web_comment{
  margin-left: 5px;
  margin-right: 5px;
}
#web_comment_content{
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 140%;
  background-color: #eee;
}
#web_comment_submit{
  margin-left: 10px;
}
</style>