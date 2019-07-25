import Vue from 'vue'
import Axios from 'axios'

import App from './App.vue'
import router from "./router/router.js"    // import router 的router 一定要小写， 不要写成Router, 否则报 can't match的报错

Vue.prototype.$axios = Axios;

new Vue({
  el: '#app',
  Axios,
  router,  // 注入到根实例中
  render: h => h(App)
})

