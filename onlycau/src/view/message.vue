<template>
  <div>
    <Comment :blog_id='blog_id'></Comment>
  </div>
</template>
<script>
import Comment from '../components/Comment'

export default{
  name:'message',
  components:{
    Comment
  },
  data(){
    return {
      blog_id:'0'
    }
  }
}
</script>