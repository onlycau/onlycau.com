<template>
  <div id="author_overview">
    <div id="head_portrait">
      <div  class="blister_box">
        <div id="age_positon">
          <Blister :ps_msg="'25岁'"></Blister>
        </div>
        <div id="live_positon">
          <Blister :ps_msg="'重庆'"></Blister>
        </div>
        <div id="learn_positon">
          <Blister :ps_msg="'自学'"></Blister>
        </div>
        <div id="is_work_positon">
          <Blister :ps_msg="'待业'"></Blister>
        </div>
      </div>
    </div>
    <div id="motto">
      <div id="motto_text">万物皆虚，万事皆允</div>
    </div>
    <div id="introduction">
      <div>我是onlycau，切图仔</div>
      <div>待业</div>
      <div>546359321@qq.com</div>
    </div>
  </div>
</template>
<script>
import Blister from '../Blister.vue'
export default{
  name:'AuthorOverview',
  components:{
    Blister
  },
  data(){
    return{
    }
  },
  methods:{
  },
}
</script>
<style>
#author_overview{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 100vh;
  color: white;
}
/* 头像*/
#head_portrait{
  border-radius: 50%;
  width: 160px;
  height: 160px;
  background: url('../../assets/hand.jpg');
  background-size:160px;
}
/*放置气泡*/
.blister_box>div{
  position: relative;
}
#age_positon{
  right:50px;
  bottom: 30px;
}
#live_positon{
  left:190px;
  bottom: 80px;
}
#learn_positon{
  right:60px;
  top: 50px;
}
#is_work_positon{
  left:180px;
}

/* 格言*/
#motto{
  border-bottom: 2px solid white;
  width: 70vw;
}
#motto_text{
  font-size: 150%;
  text-align: center;
}
/* 介绍*/
#introduction{
  font-size: 120%;
  transform: translateY(-10vh);
}
#introduction>div{
  text-align: center;
  margin: 10px;
}
</style>