<template>
  <div id="home">
    <div class="content">
      <Carousel></Carousel>
      <NavPage></NavPage>
    </div>
    <aside class="sidebar" v-show='screenWidth>1100' @click='test()'>
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
      screenWidth:document.body.clientWidth,
    }
  },
  mounted(){
      window.onresize = ()=>{
          return (()=>{
              window.screenWidth = document.body.clientWidth
              this.screenWidth = window.screenWidth
          })()
      }
  },
  watch: {
      screenWidth (val) {
          if (!this.timer) {
              this.screenWidth = val
              let ele = document.getElementsByClassName('content')[0]
              if(val < 1300){
                ele.style.width = '800px'
              }else{
                ele.style.width = '1000px'
              }
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
  justify-content: center;
}
.content{
  width: 1000px;
  margin-right: 10px;
}
.sidebar{
  background-color: #A934A2;
  width:300px;
}
</style>