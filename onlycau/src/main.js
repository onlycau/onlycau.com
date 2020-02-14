import Vue from 'vue'
import router from "./router/router.js"    // import router 的router 一定要小写， 不要写成Router, 否则报 can't match的报错
// 工具包
import axios from 'axios'
import ElementUI from 'element-ui'

import 'element-ui/lib/theme-chalk/index.css'

import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// 自定义全局函数与变量
import global_ from './Global.vue'

import App from './App.vue'

Vue.prototype.$axios = axios;
Vue.prototype.$Global = global_
Vue.prototype.$test_msg = ''

Vue.use(ElementUI)
Vue.use(mavonEditor)
new Vue({
  el: '#app',
  axios,
  router,
  mavonEditor, // 注入到根实例中
  render: h => h(App)
})
