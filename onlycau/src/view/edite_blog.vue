<!-- 已删除 留存-->
<template>
  <div id="new_blog">
    <h2>随便改改文章啦</h2>
    <div  id="new_blog_title">
      <input v-model='title' placeholder="输入文章标题" maxlength="50">
    </div>

    <div><editor ref='editor'></editor></div>
    <div>
      文章摘要:<textarea id="new_blog_summary" v-model='summary' name="content"  placeholder="大概写了啥..."></textarea>
    </div>
    <div id="new_blog_tag">文章标签</div>

    <div>
      文章分类:
      <span class="new_blog_type" v-for="type in blog_types" :key="type.id">
        <label @click='change_type(type)'><input type="radio" name="blog_type" value=type>{{type}}</label>
      </span>
    </div>
    <div id="new_blog_author">
      文章作者:<span id="author_onlycau">{{new_blog_author}}</span>
    </div>
      <div>输入权限码<input v-model='password'></div>
    <div id="post_blog">
      <span @click='post()'>修改</span>
      <span @click='delete_blog()'>删除</span>
    </div>
  </div>
</template>

<script>
import editor from '../components/editor.vue'

export default{
  name:'edite_blog',
  data:function(){
    return{
      url: this.$Global.url + '/api/blog/edite',
      blog_id :this.$route.params.blog_id,
      title:'',
      new_blog_author:'onlycau',
      blog_types:['个人日记', '计划总结', 'HTML', 'JavaScript', 'Python', 'Others', '软件配置', '软件指令'],
      blog_type:'Others',
      summary:'',
      password:'',
    }
  },
  mounted(){
    this.get_blog(this.blog_id)
  },
  components:{
    editor,
  },
  methods:{
    get_blog(id){
      const url = this.$Global.url + '/api/blog/select_blog?blog_id=' + id
      this.$axios.get(url).then((response)=>{
        this.title = response.data.title
        this.$refs.editor.editor.txt.html(response.data.text)
        this.$refs.editor.editorContent = response.data.text
        this.blog_type = response.data.blog_type
        this.summary = response.data.summary
      })
    },
    change_type(blog_type){
      this.$data.blog_type = blog_type
    },
    // todo 输入检查
    post(){
      const url = this.url
      let data={
        'blog_id':this.blog_id,
        'title': this.title,
        'blog_type': this.blog_type,
        'text': this.$refs.editor.editorContent,
        'summary': this.summary,
        'password':this.password,
      }
      this.$axios.post(url, data).then((response)=>{
        if(response.data == 1){
          this.$router.replace('/blog/' + this.blog_id)
        }
        else if (response.data ==0){
          alert('错误权限码')
        }
        else{
          alert('一些奇怪的事发生了')
        }
        })
    },
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
#post_blog > span{
  margin-left: 10px;
  cursor: pointer;
}
#post_blog > span:hover{
  color: red;
}
#new_blog_summary{
  width: 100%;
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 120%;
  background-color: #eee;
}
</style>