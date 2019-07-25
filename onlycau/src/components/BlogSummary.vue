<template>
  <div v-if='data'>
    <div class='overview'>
      <div class='overview_top'>
        <span class='blog_sort'>{{data.sort}}</span>
        <span class='blog_title'>{{data.title}}</span>
      </div>
      <div class='blog_text'>
        <p>{{data.text}}</p>
      </div>
      <div class='overview_bottom'>
        <span class='blog_author'>作者:{{data.author}}</span>
        <span class='blog_date'>时间:{{data.date}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    name:'BlogSummary',
    data:function(){
      return {}
    },
    props:['data']
  }
</script>