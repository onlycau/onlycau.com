<template>
  <div id="navpage">
    <div v-if='blogs_count'>
      <div class="content_summary" v-for='blog in data' :key='blog.id'>
        <BlogSummary :data='blog'></BlogSummary>
      </div>

      <div class="blogs_page_turning">
        <span class="btn-page_turning" :class="{'btn-disabled':current_page<=1}" @click='jump_page(-1)'><上一页</span>
        <span v-show='current_page > 3' @click='jump_page(-current_page+1)'>1</span>
        <span class='ellipsis' v-show='current_page > 4'>...</span>
        <span 
          v-for='num in list' 
          :key='num.id' 
          :class="{'current_page':num===0}"
          v-show='is_show(num)' 
          @click='jump_page(num)'
        >{{current_page + num}}</span>
        <span class="ellipsis" v-show='current_page + 3 < max_page'>...</span>
        <span v-show='current_page + 2 < max_page' @click='jump_page(max_page- current_page)'>{{max_page}}</span>
        <span class="btn-page_turning" :class="{'btn-disabled':current_page>=max_page}" @click='jump_page(1)'>下一页></span>
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
    this.select_blogs()
  },
  // 导航路由无效 待解决后替换watch
  // beforeRouteUpdate(to,form,next){
  //   this.select_blogs(0)
  //   next()
  // },
  watch:{
    // 检测路由参数变化 手动重新请求博客摘要内容然后回流重绘页面
    $route(){
      this.select_blogs()
    }
  },
  methods:{
    is_show(num){
      if(this.current_page + num > 0 && this.current_page + num <= this.max_page){
        return true
      }
    },
    jump_page(n){
      this.current_page = this.current_page + n
      this.select_blogs(this.current_page * this.per_page_count)
    },
    select_blogs(){
      let url = this.url + (this.$route.params.blog_type?this.$route.params.blog_type:'all') + '&begin=' + (this.current_page*5-5)
      this.$axios.get(url).then((response)=>{
        // this.data = response.data
        // this.max_page = response.data[0].blog_count/5
        // this.data.shift()
        // 解构赋值拆分 返回文章的数量与内容
        let middle
        [middle, ...this.data] = response.data
        this.blogs_count = middle.count
        this.max_page = ((middle.count - (middle.count % this.per_page_count)) / this.per_page_count)
    })
    },
  }
}
</script>

<style type="text/css">
#navpage{
  margin: 5px;
}
#navpage .btn-disabled{
  pointer-events: none;
  color: #CACACA;
}
/* 翻页栏*/
.blogs_page_turning{
  margin-top: 20px;
  text-align: center;
}
.btn-page_turning{
  background-color: #EEE;
}
.btn-page_turning:hover{
  background-color: #FFF;
}

.blogs_page_turning > span:not([class="ellipsis"]){
  padding: 2px 6px;
  margin: 0 1px 0 2px;
  border:solid 1px #ccc;
  border-radius: 2px;
  cursor: pointer;
}
.current_page{
  background-color: red;
  color:white;
}
.blogs_page_turning > span:not([class="btn-page_turning"],[class="ellipsis"]):hover{
  background-color: red;
  color:white;
}
/*日志摘要*/
.content_summary{
  background-color: #E1E1E1;
}
</style>