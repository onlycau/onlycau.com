<!-- to do 服务端添加密码验证 防止xss攻击 双向绑定代替ref -->
<template>
  <div id="new_blog">
    <h2>随便写写文章啦</h2>
    <div  id="new_blog_title">
      <input ref='title_value' placeholder="输入文章标题" maxlength="50">
    </div>

    <div><editor ref='editor'></editor></div>
    <div>
      文章摘要:<textarea id="new_blog_summary" v-model='summary' name="content"  placeholder="大概写了啥..."></textarea>
    </div>
    <div id="new_blog_tag">文章标签</div>

    <div>
      文章分类:
      <span class="new_blog_type" v-for="type in blog_types">
        <label @click='change_type(type)'><input type="radio" name="blog_type" value=type>{{type}}</label>
      </span>
    </div>
    <div id="new_blog_author">
      文章作者:<span id="author_onlycau">{{new_blog_author}}</span>
    </div>
    <div id="post_blog">
      <span @click='post()'>发布</span>
    </div>
  </div>
</template>

<script>
import editor from './components/editor.vue'

export default{
  name:'new_blog',
  data:function(){
    return{
      url: 'http://127.0.0.1:5000/api/blog/new',
      new_blog_author:'onlycau',
      blog_types:['个人日记', '计划总结', 'HTML', 'JavaScript', 'Python', 'Others', '软件配置', '软件指令'],
      blog_type:'Others',
      summary:''
    }
  },
  components:{
    editor,
  },
  methods:{
    change_type(blog_type){
      this.$data.blog_type = blog_type
    },
    // todo 输入检查
    post(){
      let data={
        'title': this.$refs.title_value.value,
        'blog_type': this.$data.blog_type,
        'text': this.$refs.editor.editorContent,
        'summary': this.$data.summary,
      }
      this.$axios.post(this.$data.url, data).then((response)=>{
        alert('ok')
        this.$router.replace('/blogs/all')
        })
    }
  }
}
</script>
<style>
#new_blog>div{
  margin:5px;
}
#new_blog input{
  padding-left: 10px;
  padding-right: 10px;
}
#new_blog_title{
  margin: 20px 5px 20px 0px;
}
#new_blog_title input{
  text-align: left;
  font-size: 140%;
  width: 100%;
  height: 30px;
  background-color: #eee;
}
#editor{
  margin: 20px;
}
.new_blog_type{
  font-size: 130%;
  width: 60px;
  margin: 5px;
}
#author_onlycau{
  font-size: 140%;
  margin: 0px 0px 10px 10px;
  color:red;
}
#post_blog{
  font-size: 140%;
  text-align: center;
}
#new_blog_summary{
  width: 100%;
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 120%;
  background-color: #eee;
}
</style>