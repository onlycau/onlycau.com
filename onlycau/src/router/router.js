import Vue from "vue";
import VueRouter from "vue-router";

// 引入组件
import homepage from "../homepage.vue"
import blog from "../blog.vue"
import new_blog from "../new_blog.vue"
import message from "../message.vue"

// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
    {
      path:"/blogs/:blogs_type",
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
    }

]

var router =  new VueRouter({
    routes
})
export default router;
