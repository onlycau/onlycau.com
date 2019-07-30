import Vue from 'vue'
import router from "./router/router.js"    // import router 的router 一定要小写， 不要写成Router, 否则报 can't match的报错

import axios from 'axios'

import App from './App.vue'

Vue.prototype.$axios = axios;

new Vue({
  el: '#app',
  axios,
  router,  // 注入到根实例中
  render: h => h(App)
})
