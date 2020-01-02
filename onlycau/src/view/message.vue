<template>
  <div>
    <NewComment :table_name='table_name'></NewComment>
    <CommentList :table_name='table_name'></CommentList>
  </div>
</template>
<script>
import NewComment from '../components/NewComment.vue'
import CommentList from '../components/CommentList'

export default{
  name:'message',
  components:{
    NewComment,
    CommentList
  },
  data(){
    return {
      table_name:'web_comments'
    }
  }
}
</script>