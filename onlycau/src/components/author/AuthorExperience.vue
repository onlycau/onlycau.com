<template>
  <div id="author_experience">
    <div id="card" @click='test()'>
      <div class="card_left">
        <img :src="imgs[current_id]">
      </div>
      <div class="card_right">
        <div id="experience_time">{{experience[current_id].time}}</div>
        <div id="experience_text">{{experience[current_id].text}}</div>
      </div>
    </div>
    <div id="nav_point">
      <div class="point" :class="{'on_point':index==current_id}" v-for='index in [0,1,2]' :key='index.id' @click='ha(index)'></div>
    </div>
  </div>
</template>
<script>
export default{
  name:'AuthorExperience',
  data(){
    return {
      imgs:[
        require('../../assets/logo_book2.png'),
        require('../../assets/hand.jpg'),
        require('../../assets/northwest.jpg')
        ],
      current_id :0,
      experience :[
      {time:'2019.7-至今',text:'自学前端\n熟悉HTML5,CSS,Javascript\n熟悉Web标准，了解各浏览器间的差异并能独自解决其HTML兼容性问题。\n熟悉vue.js全家桶并有相关的项目经验\n熟悉python git linux Mysql 勉强能用的英语水平'},
      {time:'2016-2019',text:'服务业工作\n  零散了学了下编程\nc prime plus看了一半 \npython网站写了一半\n每天半小时英语忽悠了自己一年\n混日子中也许想清楚了自己要干嘛\n开始学习前端'},
      {time:'2013-2015',text:'西北大学,化学工程与工艺 \n  第一专业填的软件工程,结果专业差两分 调剂\n可以转专业,但自己贪玩放弃了可能. \n玩游戏两年,多次弃考后自己申请了退学'}
      ]
    }
  },
  methods:{
    ha(index){
      this.current_id = index
    },
    test(){
      // 原点为ele中点
      let ele = document.getElementById('card')
      let e = e||window.event
      let ele_width = parseInt(window.getComputedStyle(ele).width)
      let ele_offsetX = e.offsetX - (ele_width / 2)
      let rad = Math.atan(ele_offsetX / ele_width / 2)
      ele.style.transform = 'rotateY(' + rad + 'rad)'
    },
  }
}
</script>
<style>
#author_experience{
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#card{
  display: flex;
  width: 80vw;
  height: 40vh;
  background-color: rgba(255,255,255,0.3);
}
#card:hover{
  background-color: rgba(255,255,255,0.6);
  box-shadow: 0 0 10px 0;
}
.card_left{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30vw;
}
.card_left img{
  width: 20vw;
  height: 20vw;
}
.card_right{
  flex: 1;
}
#experience_time{
  color: red;
  margin: 30px;
  font-size: 180%;
}
#experience_text{
  line-height: 28px;
  margin: 20px;
  font-size: 110%;
  white-space: pre-line;
}
/* 导航点*/
#nav_point{
  display: flex;
  justify-content: center;
}
.point{
  margin: 5vw;
  border-radius: 50%;
  width: 15px;
  height: 15px;
  background-color: blue;
  cursor: pointer;
}
.on_point{
  background-color: red;
}
</style>