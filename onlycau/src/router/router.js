import Vue from "vue";
import VueRouter from "vue-router";

// 引入组件
import homepage from "../homepage.vue"
import blog from "../blog.vue"
import new_blog from "../new_blog.vue"
import message from "../message.vue"
import SignIn from "../SignIn.vue"
import SignUp from "../SignUp.vue"
// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
    {
      path:"/blogs/:blog_type",
      component:homepage
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
