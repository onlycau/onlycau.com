<template>
    <div id="blogs">
      <NavPage></NavPage>
    </div>
</template>

<script>

import NavPage from '../components/NavPage.vue'

export default {
  name: 'blogs',
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