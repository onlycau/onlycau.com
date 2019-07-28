<template>
  <div id="blog">
    <span>{{data.text}}</span>
  </div>
</template>

<script>
  export default{
    name:'blog',
    data:function(){
      return{
        data:{},
        blog_id:this.$route.params.id
      }
    },
    mounted(){
      this.get_blog(this.blog_id)
    },
    methods:{
      get_blog(id){
        const url = 'http://127.0.0.1:5000/get_blogs/?id=' + id
        this.$axios.get(url).then((response)=>{
          this.$data.data = response.data[0]
        })
    }
  },
}
</script>

<style>
  
</style>