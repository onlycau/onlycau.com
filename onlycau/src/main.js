import Vue from 'vue'
import router from "./router/router.js"    // import router 的router 一定要小写， 不要写成Router, 否则报 can't match的报错

// 工具包
import axios from 'axios'

// 自定义全局函数与变量
import global_ from './Global.vue'
import base from './base.js'

import App from './App.vue'

Vue.prototype.$axios = axios;
Vue.prototype.$Global = global_
Vue.prototype.$test_msg = ''
Vue.use(base)

new Vue({
  el: '#app',
  axios,
  router,  // 注入到根实例中
  render: h => h(App)
})
