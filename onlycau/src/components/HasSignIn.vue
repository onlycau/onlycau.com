<template>
  <div id="welcome">
    <div v-if="has_sign_in">
        <a href="\user\">{{username}}</a>
        <a href="\sign_out\">退出</a>
    </div>
    <div v-else>
        <a href="\sign_in\">登录</a>
        <a href="\sign_up\">注册</a>
    </div>
  </div>
</template>

<script>
  export default {
    name:'HasSignIn'
  }
</script>