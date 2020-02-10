// to do
// history 模式 服务器配置

import Vue from "vue";
import VueRouter from "vue-router";

// 引入组件
import home from "../view/home.vue"
import blogs from "../view/blogs.vue"
import blog from "../view/blog.vue"
import new_blog from "../view/new_blog.vue"
import edite_blog from "../view/edite_blog.vue"
import message from "../view/message.vue"
import SignIn from "../view/SignIn.vue"
import SignUp from "../view/SignUp.vue"

import author from "../view/author.vue"

import management from "../view/management/management.vue"
import blog_list from "../view/management/blog_list.vue"
import blog_new from "../view/management/blog_new.vue"
// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
    {
    path:'',
    redirect:'/home'
    },
    {
      path:"/home",
      component:home,
    },
    {
      path:"/blogs/:blog_type",
      component:blogs
    },
    {
      path:"/blog/:blog_id",
      component:blog
    },
    {
      path:"/new_blog",
      component:new_blog
    },
    {
      path:"/edite_blog/:blog_id",
      name: "edite_blog",
      component:edite_blog
    },
    {
      path:"/message",
      component:message
    },
    {
      path:"/user/sign_in",
      component:SignIn
    },
    {
      path:"/user/sign_up",
      component:SignUp
    },
    // about author
    {
      path:'/author',
      component:author
    },
    // management
    {
      path:'/management',component:management,
      children: [
      {
        path: 'blog_list',
        component: blog_list,
      },
      {
        path: 'blog_new',
        component: blog_new,
      }]
    },

]

var router =  new VueRouter({
  mode:'hash',
    routes
})
export default router;
