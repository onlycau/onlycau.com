<template>
  <div>
    <div>
      <div id="summary">
        <BlogSummary :data='data[1]'></BlogSummary>
        <BlogSummary :data='data[2]'></BlogSummary>
  <!--     <BlogSummary :data='data[3]'></BlogSummary>
        <BlogSummary :data='data[4]'></BlogSummary>
        <BlogSummary :data='data[5]'></BlogSummary> -->
      </div>

      <div id="PageTurning">
        <!-- 待优化 1.直接点击序号跳转页面 2.跳页 3.样式更新-->
        <div v-if='max_page > 1'>
          <span v-if='current_page > 1' @click="get_summary(--current_page)">&lt;</span>
          <span v-if='current_page > 2'>{{current_page - 2}}</span>
          <span v-if='current_page > 1'>{{current_page - 1}}</span>
          <span id="current_page">{{current_page}}</span>
          <span v-if='current_page < max_page '>{{current_page + 1}}</span>
          <span v-if='current_page < max_page - 1'>{{current_page + 2}}</span>
          <span v-if='current_page < max_page' @click="get_summary(++current_page)">&gt;</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import BlogSummary from './BlogSummary.vue'

  export default{
    name:'NavPage',
    components:{
      BlogSummary:BlogSummary,
    },
    data:function(){
      return {
        data:{},
        url:'http://127.0.0.1:5000/api/blog/select_blogs?blogs_type=',
        blogs_type:this.$route.params.blogs_type,
        current_page:1,
        max_page:1,
        count: 2,
      }
    },
    mounted(){
      this.get_summary(1)
    },
    watch:{
      $route(){
        this.get_summary(1)
      }
    },
    methods:{
      get_summary(current_page=1){
        var url = this.$data.url + this.$route.params.blogs_type + '&begin=' + (current_page*2-2)
        this.$axios.get(url).then((response)=>{
          this.$data.data = response.data
          this.$data.max_page = response.data[0].blog_count/2
          this.$data.current_page = current_page;
      })
      },
    }
  }
</script>

<style type="text/css">
  /* 翻页栏*/
  #PageTurning{
    font-size: 150%;
    text-align: center;
    margin:10px 10px 10px 10px;
  }
  #current_page{
    color: red;
  }
</style>