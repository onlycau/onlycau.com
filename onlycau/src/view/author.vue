<template>
  <div id="author">
    <div id="fullpage_box">
      <div class="fullpage overview_">
        <AuthorOverview></AuthorOverview>
      </div>
      <div class="fullpage skill">
        <AuthorSkill></AuthorSkill>
      </div>
      <div class="fullpage experience"></div>
      <div class="fullpage project">
        <AuthorProject></AuthorProject>
      </div>
      <div class="fullpage contact">
        <AuthorContact></AuthorContact>
      </div>
    </div>
    <div id="nav_fullpage">
      <div class="nav_img" v-for='(img,index) in imgs' :key = 'img.id'>
        <div class='nav_img_right' @mouseenter='enter(index)' @mouseleave='leave(index)' @click='jump(index)'>
          <div v-show='current_page===index || is_enter[index]'>
            <MyCanvas :ps_msg='[img,Math.random()]'></MyCanvas>
          </div>
          <div class="dot" ></div>
        </div>
        <div v-show='is_enter[index]' class="nav_promt">
          <div class="nav_rec"> {{promt[index]}}</div>
          <div class="triangle_right"></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import MyCanvas from "../components/MyCanvas.vue"
import AuthorOverview from "../components/author/AuthorOverview.vue"
import AuthorSkill from "../components/author/AuthorSkill.vue"
import AuthorProject from "../components/author/AuthorProject"
import AuthorContact from "../components/author/AuthorContact.vue"
export default {
  name:'author',
  components:{
    MyCanvas,
    AuthorOverview,
    AuthorSkill,
    AuthorProject,
    AuthorContact,
  },
  data(){
    return {
      timeoutId:0,
      translateY:0,
      scroll_ele:'',
      previous:0,
      imgs : ['house','skill','experience','project','contact'],
      promt: ['首页','能力','经历','作品集','联系我'],
      is_enter_list:[0,0,0,0,0],
      is_enter_key:1,
    }
  },
  computed:{
    current_page:function(){
      return parseInt(-this.translateY / 40)
    },
    // 添加包含随机数计算属性代替watch
    is_enter:function(){
      return this.is_enter_list.map((item)=>{
         return item *= this.is_enter_key
      })
    }
  },
  mounted(){
    this.scroll_ele = document.getElementById('fullpage_box')
    window.addEventListener('mousewheel',this.throttle(this.handleScroll,200))
  },
  methods:{
    // 滚动页面相关函数
    throttle(func,wait){
      return ()=>{
        let now = Date.now()
        let that = this
        let args = arguments
        if(now - this.previous > wait){
          func.apply(that, args)
          this.previous = now
        }
      }
    },
    scroll(ele,key){
      setTimeout(()=>{
        this.timeoutId = setInterval(()=>{
          this.translateY += key
          ele.style.transform = 'translateY(' + this.translateY/2 + '%)'
          if(this.translateY%40 === 0){
            clearTimeout(this.timeoutId)
          }
        },16.7)
      },50)
    },
    handleScroll(){
      let ele = this.scroll_ele
      let e = window.event
      if(e.deltaY > 50 && (this.translateY > -160)){
        clearTimeout(this.timeoutId)
        this.scroll(ele,-1)
      }
      else if(e.deltaY < -50 && (this.translateY < 0)){
        clearTimeout(this.timeoutId)
        this.scroll(ele,1)
      }
      this.throttle_key = false
    },
    // 右侧导航栏
    jump(index){
      let ele = this.scroll_ele
      let key = this.current_page - index
      let timeoutId = setInterval(()=>{
        this.translateY += key
        ele.style.transform = 'translateY(' + this.translateY/2 + '%)'
        if(this.translateY === (index * -40)){
          clearTimeout(timeoutId)
        }
      },16.7)
    },
    enter(index){
      this.is_enter_list[index] = 1
      this.is_enter_key = Math.random()
    },
    leave(index){
      setTimeout(()=>{
        this.is_enter_list[index] = 0
        this.is_enter_key = Math.random()
      },100)
    }
  }
}
</script>
<style>
#author{
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
/* 全屏滚动页面*/
#fullpage_box{
}
.fullpage{
  height: 100vh;
  width: 100vw;
}
.overview_{
  background-color: #CCCC99;
}
.skill{
  background-color: #CCFFFF;
}
.experience{
  background-color: #9999FF;
}
.project{
  background-color: #CC99CC;
}
.contact{
  background-color: #CC9933;
}
/* 右侧导航栏*/
#nav_fullpage{
  position: fixed;
  right: 10px;
  bottom: 50vh;
  transform:translateY(30%);
  height: 200px;
  width: 120px;
}
.nav_img{
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  width: 120px;
  height: 36px;
  margin: 2px;
}
.nav_promt{
  display: flex;
  width: 80px;
  color: white;
  height: 24px;
  line-height: 24px;
  transform: translateY(6px);
}
/* 导航指示条*/
.nav_rec{
  width: 50px;
  background-color:#333333;
}
.triangle_right{
  width:0;
  border-top: 12px solid transparent;
  border-left: 24px solid #333333;
  border-bottom: 12px solid transparent;
}
.nav_img_right{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 36px;
  height: 36px;
  cursor: pointer;
}
.dot{
  position: absolute;
  width: 12px;
  height: 12px;
  background-color: grey;
  border-radius: 50%;
  z-index: -10;
}
</style>