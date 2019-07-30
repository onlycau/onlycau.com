<template>
  <div id="blog">
    <div>{{data.title}}</div>
    <div v-html='data.text'></div>
    <div>{{data.date}}</div>
  </div>
</template>

<script>
  export default{
    name:'Blog',
    data:function(){
      return{
        data:{
          data:{}
        },
        blog_id:this.$route.params.blog_id
      }
    },
    mounted(){
      this.get_blog(this.blog_id)
    },
    methods:{
      get_blog(id){
        const url = 'http://127.0.0.1:5000/api/blog/select_blog?blog_id=' + id
        this.$axios.get(url).then((response)=>{
          this.$data.data = response.data
        })
    }
  },
}
</script>

<style>
  
</style>