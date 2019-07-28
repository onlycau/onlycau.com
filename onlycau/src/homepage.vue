<template>
    <div id="homepage">
      <NavPage></NavPage>
      <router-link to="/sign_in">登录</router-link>
      <router-view></router-view>
    </div>
</template>

<script>

import NavPage from './components/NavPage.vue'

export default {
  name: 'App',
  components: {
    NavPage,
  }
}
</script>

<style>
a{
  text-decoration: none;
  outline: none;
  color: #FE4365;
}
</style>