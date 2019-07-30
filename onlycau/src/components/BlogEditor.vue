<template>
  <div id="write_blog">
    <editor ref='editor'></editor>
    <span @click='post_blog()'>post</span>
  </div>
</template>

<script>
import editor from './editor.vue'

export default {
  name: 'App',
  data:function(){
    return{
      text:''
    }
  },
  components: {
    editor
  },
  methods:{
    post_blog(){
      var data = {
        lala:this.$refs.editor.editorContent
      }
      var url = 'http://127.0.0.1:5000/push_blog/'
      this.$axios.post(url,data).then(()=>{
        alert('hehe')
      })
    }
  }

}
</script>