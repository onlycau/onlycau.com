<template>
  <div id="PageTurning">
    <div v-if='is_show_page'>
      <span><a><</a></span>
      <span><a>{{pages.current_page}}</a></span>
      <span><a>></a></span>
    </div>
  </div>
</template>

<script>
  export default{
    name:'PageTurning',
    data:function(){
      return {}
    },
    props:['pages'],
    computed:{
      is_show_page:function(){
        return (this.pages.blog_count>2)
      }
    }
  }
</script>

<style>
  #PageTurning{
    font-size: 150%;
  }
</style>