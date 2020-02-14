<template>
  <div class="management">
    <el-container>
    <el-header height="80px">
      <span @click='test()'>Header</span>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu
          :default-active="current_path"
          :router='true'
          class="el-menu-vertical-demo"
          background-color="#545c6400"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="/management">
            <i class="el-icon-s-home"></i>
            <span slot="title">主页</span> 
          </el-menu-item>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>文章管理</span>
            </template>
              <el-menu-item index="/management/blog_list">
                <i class="el-icon-document"></i>
                <template slot="title">文章列表</template>
              </el-menu-item>
              <el-menu-item index="/management/blog_new">
                <i class="el-icon-document-add"></i>
                <template slot="title">添加文章</template>
              </el-menu-item>
              <el-menu-item index="/management/blog_edite/1">
                <i class="el-icon-edit"></i>
                <template slot="title">修改文章</template>
              </el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-s-comment"></i>
              <span slot="title">评论管理</span>
            </template>
          </el-submenu>
          <el-menu-item index="4">
            <i class="el-icon-collection-tag"></i>
            <span slot="title">标签管理</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-container>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
      <el-footer>
        <div id="footer">
            onlycau©2019<br>
            <a href="http://www.miit.gov.cn">渝ICP备19009971号</a>
        </div>
      </el-footer>
  </el-container>
  </div>
</template>

<script>
  export default{
    name:'management',
    computed:{
      current_path(){
        return this.$route.path.replace(/\/\d+/,'/1') //默认修改文章demo blog_id 1
      }
    },
    methods:{
      test(){
        window.console.log(this.$route.path)
      },
    }
  }
</script>
<style>
.management>section{
  height: 100vh;
  background: url(https://s2.ax1x.com/2020/02/07/1gnLdI.jpg) no-repeat;
  background-size:100% 100%; 
  background-attachment:fixed;
}
section .el-main{
  overflow: hidden;
  padding: 0px;
}
</style>