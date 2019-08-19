<template>
  <div>
    <div v-if='blogs_count'>
      <div id="summary" v-for='blog in data'>
        <BlogSummary :data='blog'></BlogSummary>
      </div>

      <div id="blogs_page_turning">
        <span v-show='current_page - 1' @click='action(-1)'>上一页</span>
        <span v-show='current_page > 3' @click='action(-current_page+1)'>1</span>
        <span v-show='current_page > 4'>...</span>
        <span v-show='isShow(num)' v-for='num in list' @click='action(num)'><span v-show='num==0'>|</span>{{current_page + num}}</span>
        <span v-show='current_page + 3 < max_page'>...</span>
        <span v-show='current_page + 2 < max_page' @click='action(max_page- current_page)'>{{max_page}}</span>
        <span v-show='current_page < max_page' @click='action(1)'>下一页</span>
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
      url: this.$Global.url + '/api/blog/select_blogs?blog_type=',
      blog_type:this.$route.params.blog_type,
      begin: 0,
      blogs_count: 0,
      current_page: 1,
      per_page_count:5,
      max_page:0,
      list:[-2,-1,0,1,2],
      }
  },
  created(){
    this.select_blogs(0)
  },
  watch:{
    // 检测路由参数变化 手动重新请求博客摘要内容然后回流重绘页面
    $route(){
      this.select_blogs(0)
    }
  },
  methods:{
    isShow(num){
      if(this.$data.current_page + num > 0 && this.$data.current_page + num <= this.$data.max_page){
        return true
      }
    },
    action(n){
      this.$data.current_page = this.$data.current_page + n
      this.select_blogs(this.$data.current_page * 5)
    },
    select_blogs(begin){
      let url = this.$data.url + (this.$route.params.blog_type?this.$route.params.blog_type:'all') + '&begin=' + (this.$data.current_page*5-5)
      this.$axios.get(url).then((response)=>{
        // this.$data.data = response.data
        // this.$data.max_page = response.data[0].blog_count/5
        // this.$data.data.shift()
        // 解构赋值拆分 返回文章的数量与内容
        let middle
        [middle, ...this.$data.data] = response.data
        this.$data.blogs_count = middle.count
        this.$data.max_page = ((middle.count - (middle.count % this.$data.per_page_count)) / this.$data.per_page_count)
    })
    },
  }
}
</script>

<style type="text/css">
/* 翻页栏*/
#blogs_page_turning{
  margin-top: 20px;
  text-align: center;
}
#blogs_page_turning > span{
  margin-left: 5px;
  margin-right: 5px;
  cursor: pointer;
}
#blogs_page_turning > span:hover{
  background-color: red;
}
</style>