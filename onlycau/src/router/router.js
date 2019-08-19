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
// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
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

]

var router =  new VueRouter({
    routes
})
export default router;
