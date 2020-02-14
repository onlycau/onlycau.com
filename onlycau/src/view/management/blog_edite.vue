<template>
  <div class="blog_edite">
    <div class="title_and_post">
      <el-input
        type="text"
        placeholder="请输入文章标题"
        v-model="blog.title"
        maxlength="30"
        show-word-limit
        style="width: calc(100% - 222px);margin-right: 10px;font-size: 120%;">
      </el-input>
        <el-button type="warning" disabled>保存草稿</el-button>
        <el-button type="primary" @click="dialogTableVisible = true">修改文章</el-button>
        <el-dialog 
          title="发布文章" 
          :visible.sync="dialogTableVisible"
          v-loading="loading"
          element-loading-text="加载中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="#00000080">
          <div class="release">
            <div>
              <span>文章标签</span>
              <el-button type="info" style="margin-left: 30px">to do</el-button>
            </div>
            <div class="blog_edite_type">
              <span>分类专栏</span>
              <el-select
                v-model="blog.blog_type" 
                filterable
                placeholder="请选择">
                <el-option-group
                  v-for="group in options"
                  :key="group.label"
                  :label="group.label">
                  <el-option
                    v-for="item in group.options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-option-group>
              </el-select>
            </div>
            <div class="form_privacy">
              <span>发布形式</span>
              <el-radio v-model="blog.privacy" label="public" style="margin-left: 30px">公开</el-radio>
              <el-radio v-model="blog.privacy" label="private">私密</el-radio>
            </div>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogTableVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="post_blog()"
            >确 定</el-button>
          </div>
        </el-dialog>
    </div>
    <mavon-editor 
        v-model="blog.text" 
        ref="md" 
        @change="change" 
        style="height: calc(100vh - 195px)"
    />
  </div>
</template>

<script>
export default{
  name:'blog_edite',
  data() {
    return { 
      loading: false,
      dialogTableVisible: false,
      get_url: this.$Global.url + '/api/blog/select_blog',
      post_url: this.$Global.url + '/api/blog/edite',
      blog:{
        blog_id: this.$route.params.blog_id,
        title: '',
        blog_type: '待选择',
        privacy: 'public',
        text: '', // 输入的markdown
        summary: 'haha',
        html: '',    // 及时转的html
      },
      // 分类列表
      options: [
      {
        label: '生活随笔',
        options: [{
          value: '个人日记',
          label: '个人日记'
        }, {
          value: '计划总结',
          label: '计划总结'
        }]
      }, {
        label: '学习记录',
        options: [{
          value: 'HTML',
          label: 'HTML'
        }, {
          value: 'Javascript',
          label: 'Javascript'
        }, {
          value: 'Python',
          label: 'Python'
        }, {
          value: 'Others',
          label: 'Others'
        }]
      }, {
        label: '备忘录',
        options: [{
          value: '软件配置',
          lable: '软件配置'
        }, {
          value: '软件指令',
          lable: '软件指令'
        }]
      }],
    }
  },
  mounted(){
    this.select_blog(this.blog.blog_id)
  },
  methods: {
    // 所有操作都会被解析重新渲染
    change(value, render){
        // render 为 markdown 解析后的结果[html]
        this.blog.text = value
        this.blog.html = render
    },
    // 提交
    select_blog(blog_id){
      this.$axios.get(this.get_url, {
        params: {
          blog_id: blog_id
        }
      }).then((response)=>{
        this.blog.title = response.data.title
        this.blog.blog_type = response.data.blog_type
        this.blog.summary = response.data.blog_type
        this.blog.text = response.data.blog_text
        this.blog.html = response.data.html
        this.$refs.md.d_value = response.data.text
      })
    },
    post_blog(){
      this.loading = true
      this.$axios.post(this.post_url, this.blog).then((response)=>{
        if(response.data){
          setTimeout(()=>{
            window.console.log(response.data)
            this.loading = false
            this.dialogTableVisible = false
            this.$router.push({path:"/management/blog_list"})
          },200)
        }
        })
    }
  },
}
</script>
<style>
.blog_edite{
  padding: 5px;
  background-color: #eee;
}
.title_and_post{
  margin: 0 0 5px 0;
}
.release>div{
  margin: 20px;
}
.blog_edite_type>span{
  margin-right: 30px;
}
</style>