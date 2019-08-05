<template>
  <div id="new_comment">
    <div>
      给我留言
    </div>
    <form action="http://127.0.0.1:5000/api/new_comment" method="get">
      <textarea id="comment_content" name="content" placeholder="写点什么..." /><br>
      <input id="comment_name" type="text" name="username" placeholder="昵称" /><br>
      <input id="comment_name" type="text" name="mailbox" placeholder="邮箱" /><br>
      <input id='comment_table' type="text" name="table" :value='table'>
      <input id="comment_submit" type="submit" value="提交评论"/>
    </form>
  </div>
</template>
<script>
export default{
  name:'NewComment',
  props:['table']
}
</script>
<style>
#new_comment{
  margin-left: 5px;
  margin-right: 5px;
}
#comment_content{
  width: 100%;
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 140%;
  background-color: #eee;
}
#comment_submit{
  margin-left: 10px;
}
#comment_table{
  display: none;
}
</style>