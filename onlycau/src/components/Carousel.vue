<!-- to do 
    1.暂停功能
    2.修改图片滚动速度 尝试定长变换 而不是固定角度变换
    3.添加阴影 
-->
<template>
  <div class="carousel">
    <div class="carousel_left">
      <div class="contain_left">
          <img :class="{box_img:current_img==0}" src="../assets/1.png">
          <img :class="{box_img:current_img==1}" src="../assets/2.png">
          <img :class="{box_img:current_img==2}" src="../assets/3.png">
          <img :class="{box_img:current_img==3}" src="../assets/4.jpeg">
          <img :class="{box_img:current_img==4}" src="../assets/5.png">
      </div>
    </div>
    <div class="carousel_right">
      <div class="contain_right">
        <div><img src="../assets/1.png"></div>
        <div><img src="../assets/2.png"></div>
        <div><img src="../assets/3.png"></div>
        <div><img src="../assets/4.jpeg"></div>
        <div><img src="../assets/5.png"></div>
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'Carousel',
  data(){
    return{
      current_img:0,
      timeoutId:0,
      pause:false,
    }
  },
  mounted(){
    this.carousel()
  },
  watch:{
    pause(val){
      if(this.pause){
        clearInterval(this.timeoutId)
      }
      else{
        this.carousel()
      }
    }
  },
  methods:{
    carousel(){
      let contain_right = document.getElementsByClassName('contain_right')[0]
      let contain_left = document.getElementsByClassName('contain_left')[0]
      contain_right.getElementsByTagName('div')[(this.current_img)].style.transform = 'rotateX(0deg)'
      let top = 0
      // 定时移动焦点图片，到达列表尾翻页 位移图片
      this.timeoutId = setInterval(()=>{
        this.current_img = (this.current_img + 1)%5
        let ele_hide = contain_right.getElementsByTagName('div')[(this.current_img + 4)%5]
        let ele_show = contain_right.getElementsByTagName('div')[this.current_img]
        if((this.current_img === 0) || (this.current_img === 4)){
          let key = (this.current_img === 0)? 3:-3
          let timeoutId = setInterval(()=>{
            top += key
            contain_left.style.top = top + 'px'
            if(top < -96 || top > -1){
              clearInterval(timeoutId)
            }
          },16.7)
        }
        // 不能直接引用变化的图片序号
        let i = this.current_img
        // 随机选择翻转方向
        if(Math.random()>0.5){
          this.rotate_y(ele_hide, ele_show, Math.random()>0.5)
        }
        else{
          this.rotate_x(ele_hide, ele_show, Math.random()>0.5)
        }
        // to do 1 暂停功能待完善
        if(document.visibilityState == 'hidden'){
          this.pause = true
        }
      },5000)
    },
    rotate_y(ele_hide, ele_show, clockwise){
      ele_hide.style.transformOrigin = (clockwise?'0%':'100%') + ' 0%'
      ele_show.style.transformOrigin = (clockwise?'100%':'0%') + ' 0%'
      let degree_hide = 0
      let degree_show = 0
      let timeoutId = setInterval(()=>{
        degree_hide += clockwise?1:-1
        degree_show = ((Math.acos((1-Math.cos(degree_hide*Math.PI/180))))*180/Math.PI)
        ele_hide.style.transform = 'rotateY(' + degree_hide + 'deg)'
        ele_show.style.transform = 'rotateY(' + degree_show + 'deg)'
        if(degree_hide <= -90||degree_hide >= 90){
          clearInterval(timeoutId)
        }
      },16.7)
    },
    rotate_x(ele_hide, ele_show, clockwise){
      ele_hide.style.transformOrigin = '0% ' + (clockwise?'0%':'100%')
      ele_show.style.transformOrigin = '0% ' + (clockwise?'100%':'0%')
      let degree_hide = 0
      let degree_show = 0
      let timeoutId = setInterval(()=>{
        degree_hide += clockwise?1:-1
        degree_show = ((Math.acos((1-Math.cos(degree_hide*Math.PI/180))))*180/Math.PI)
        ele_hide.style.transform = 'rotateX(' + degree_hide + 'deg)'
        ele_show.style.transform = 'rotateX(' + degree_show + 'deg)'
        if(degree_hide <= -90||degree_hide >= 90){
          clearInterval(timeoutId)
        }
      },16.7)
    },
  },
}
</script>
<style>
.carousel{
  height: 400px;
  display: -webkit-flex; /* Safari */
  display: flex;
  justify-content: space-between;
}
/* 轮播图左侧导航*/
.carousel_left{
  overflow: hidden;
  flex:1;
  height: 400px;
  padding-right: 5px;
}
.contain_left{
  overflow: hidden;
  position: relative;
}
.box_img{
  border-color: blue;
}
.carousel_left img{
  border-style: solid;
  height: 91px;
  width: 190px;
}
/*3D翻转*/
.carousel_right{
  width: 800px;
  height: 400px;
}
.contain_right div{
  transform: rotateX(90deg);
  position: absolute;
}
.carousel_right img{
  height: 400px;
  width: 800px;
}
</style>