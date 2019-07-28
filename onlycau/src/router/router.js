import Vue from "vue";
import VueRouter from "vue-router";

// 引入组件
import homepage from "../homepage.vue"
import SignIn from "../SignIn.vue";
import blog from '../blog.vue'
import WriteBlog from '../WriteBlog.vue'

// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

const routes = [
    {
        path:"/sign_in",
        component: SignIn
    },
    {
      path:"/",
      component:homepage,
    },
    {
      path:"/blog/:id",
      component:blog
    },
    {
      path:"/write_blog",
      component:WriteBlog
    }
]

var router =  new VueRouter({
    routes
})
export default router;
