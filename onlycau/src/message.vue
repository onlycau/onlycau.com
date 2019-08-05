<template>
  <div>
    <NewComment :table='table'></NewComment>
    <CommentList :table='table'></CommentList>
  </div>
</template>
<script>
import NewComment from './components/NewComment.vue'
import CommentList from './components/CommentList'

export default{
  name:'message',
  components:{
    NewComment,
    CommentList
  },
  data(){
    return {
      table:'web_comments'
    }
  }
}
</script>