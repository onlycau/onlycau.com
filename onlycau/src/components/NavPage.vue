<template>
  <div>
    <div v-if='blog_count'>
      <div id="summary" v-for='blog in data'>
        <BlogSummary :data='blog'></BlogSummary>
      </div>

      <div id="PageTurning">
        <!-- TODO: 1.直接点击序号跳转页面 2.跳页 3.样式更新-->
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
    <div v-else>
      啥都木有
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
        url:'http://127.0.0.1:5000/api/blog/select_blogs?blog_type=',
        blog_type:this.$route.params.blog_type,
        blog_count:0,
        current_page:1,
        max_page:1,
        count: 2,
      }
    },
    mounted(){
      this.get_summary(1)
    },
    watch:{
      // 检测路由参数变化 手动重新请求博客摘要内容然后回流重绘页面
      $route(){
        this.get_summary(1)
      }
    },
    methods:{
      get_summary(current_page=1){
        let url = this.$data.url + this.$route.params.blog_type + '&begin=' + (current_page*5-5)
        this.$axios.get(url).then((response)=>{
          // this.$data.data = response.data
          // this.$data.max_page = response.data[0].blog_count/5
          // this.$data.data.shift()
          // 解构赋值拆分 返回文章的数量与内容
          let count
          [count,...this.$data.data] = response.data
          this.$data.current_page = current_page
          this.$data.blog_count = count.blog_count
          this.$data.max_page = count.blog_count/5
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