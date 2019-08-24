<template>
  <div id="home">
    <div class="content">
      <Carousel></Carousel>
      <NavPage></NavPage>
    </div>
    <aside class="sidebar" v-show='screenWidth>1000' @click='test()'>
      to do
    </aside>
  </div>
</template>
<script>
import Carousel from "../components/Carousel.vue"
import NavPage from "../components/NavPage.vue"
export default{
  name:'home',
  components:{
    Carousel,
    NavPage,
  },
  data(){
    return{
      screenWidth:document.body.clientWidth
    }
  },
  mounted(){
      const that = this
      window.onresize = ()=>{
          return (()=>{
              window.screenWidth = document.body.clientWidth
              that.screenWidth = window.screenWidth
          })()
      }
  },
  watch: {
// 找到的最早此文章来源https://www.cnblogs.com/erbingbing/p/6340930.html?utm_source=itdadao&utm_medium=referral
      screenWidth (val) {
          if (!this.timer) {
              this.screenWidth = val
              this.timer = true
              let that = this
              setTimeout(function () {
                  // that.screenWidth = that.$store.state.canvasWidth
                  that.timer = false
              }, 400)
          }
      }
  }
}
</script>
<style>
#home{
  display: -webkit-flex; /* Safari */
  display: flex;
}
.content{
  width: 100%;
}
.sidebar{
  margin-top: 5px;
  background-color: #A934A2;
  width:30vw;
}
</style>