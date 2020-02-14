<template>
  <div class="flex-container">
    <div class="container-query">
      <span>文章分类</span>
      <el-select
        v-model="value" 
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
    <div class="container-list">
      <div class="list-head">
          <el-row :gutter="20">
            <el-col :span="2">
              <div class="bg-purple">ID</div>
            </el-col>
            <el-col :span="4">
              <div class="bg-purple">标题</div>
            </el-col>
            <el-col :span="2">
              <div class="bg-purple">分类</div>
            </el-col>
            <el-col :span="2">
              <div class="bg-purple">标签</div>
            </el-col>
            <el-col :span="2">
              <div class="bg-purple">作者</div>
            </el-col>
            <el-col :span="6">
              <div class="bg-purple">摘要</div>
            </el-col>
            <el-col :span="2">
              <div class="bg-purple">阅读量</div>
            </el-col>
            <el-col :span="4">
              <div class="bg-purple">操作</div>
            </el-col>
          </el-row>

      </div>
      <div class="list-main"
        v-loading="loading"
        element-loading-text="拼命加载中"
        element-loading-spinner="el-icon-loading"
        element-loading-background="#00000080">
        <div v-for="blog in blogs" :key="blog.id">
          <el-row :gutter="20">
            <el-col :span="2">
              <div class="grid-content bg-purple">{{blog.id}}</div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">{{blog.title}}</div>
            </el-col>
            <el-col :span="2">
              <div class="grid-content bg-purple">{{blog.blog_type}}</div>
            </el-col>
            <el-col :span="2">
              <div class="grid-content bg-purple">标签</div>
            </el-col>
            <el-col :span="2">
              <div class="grid-content bg-purple">onlycau</div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">{{blog.summary}}</div>
            </el-col>
            <el-col :span="2">
              <div class="grid-content bg-purple">0</div>
            </el-col>
            <el-col :span="4">
              <div class="grid-content bg-purple">
                  <router-link :to="{ name: 'blog_edite', params: { blog_id: blog.id }}">
                    <el-button type="primary" icon="el-icon-edit" circle></el-button>
                  </router-link>
                  <el-button 
                    type="danger" 
                    icon="el-icon-delete" 
                    circle
                    style="margin-left: 10px"
                    @click="delete_blog(blog.id)">
                  </el-button>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </div>
    <div class="container-pag">
      <el-pagination
        :hide-on-single-page="total<11"
        :page-size="5"
        :total="total"
        :current-page.sync="currentPage"
        background
        layout="prev, pager, next">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default{
  name:'blog_list',
  data() {
    return {
      loading: true,
      // query
      options: [{
        options:[{
          value: 'all',
          label: '全部',
        }]
      },
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
      value: 'all',
      // list-main
      url: this.$Global.url + '/api/blog/select_blogs?blog_type=',
      begin: 0,
      blogs_count: 0,
      total: 0,
      currentPage:1,
      blogs:'',
    }
  },
  created(){
    this.select_blogs()
  },
  watch:{
    // 检测value变化 更新页面
    value(){
      this.select_blogs()
    },
    currentPage(){
      this.select_blogs()
    }
  },
  methods:{
    select_blogs(){
      this.loading = true
      let url = this.url + this.value + '&begin=' + (this.currentPage*5-5)
      this.$axios.get(url).then((response)=>{
        let middle
        [middle, ...this.blogs] = response.data
        this.total = middle.count
        this.loading = false
    })
    },
    delete_blog(blog_id) {
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        cancelButtonText: '取消',
        confirmButtonText: '确定',
        type: 'warning',
        center: true
      }).then(() => {
        let url = this.$Global.url + '/api/blog/delete?blog_id=' + blog_id
        this.$axios.get(url).then((response)=>{
          if(response.data === 1){
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            this.select_blogs()
          }
          else{
            this.$message({
              type: 'fali',
              message: '删除失败 请联系管理员'
            })
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  }
}
</script>

<style>
.flex-container{
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

}
/* 查询栏 */
.container-query{
  height: 40px;
  padding: 20px;
  background-color: white;
}
.container-query>span{
  margin-right: 20px;
}
/* 文章列表 */
.container-list{
  flex-grow: 1;
  background-color: #f1fcfcdd
}
.list-head>div.el-row {
  background-color: #ededed
}
.el-col{
  text-align: center;
  line-height: 36px;
}
.list-main div.el-col {
  overflow: hidden;
  text-overflow:ellipsis;
  white-space: nowrap;
}
.grid-content {
  border-radius: 4px;
  min-height: calc((100vh - 320px) / 5);
  line-height: calc((100vh - 320px) / 5);
}
/* 分页 */
.container-pag{
  text-align: center;
  background-color: white;
  margin: 0 0 10px 0;
}
</style>