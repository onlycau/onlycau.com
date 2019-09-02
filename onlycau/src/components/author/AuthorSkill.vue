<template>
  <div id="author_skill" @mouseenter='skill_bar(skill)'>
    <div class="bar_box" v-for="(value,name,index) in skill">
      <div class="skill_name" @click='add_length(index,value)'>{{name}}</div>
      <div class="back_white"></div>
      <div class="process_bar">
        {{value}}%
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'AuthorSkill',
  data(){
    return{
      skill:{
        HTML:75,
        CSS:70,
        JavaScript:70,
        Mysql:50,
        Python:65,
        linux:60,
        git:50
      }
    }
  },
  methods:{
    skill_bar(skill){
      let i = 0
      let ele_list = document.getElementsByClassName('process_bar')
      for(let name in skill){
        ele_list[i].style.width = '0'
        this.add_length(i, skill[name])
        i += 1
      }
    },
    // 定时器固定速度增长某进度条 索引为序号
    add_length(index,percentage){
      let ele = document.getElementsByClassName('process_bar')[index]
      let bar_length = 0
      let timeoutId = setInterval(()=>{
        bar_length += 1
        ele.style.width = bar_length + 'vw'
        if(bar_length === percentage){
          clearTimeout(timeoutId)
        }
      },16.7)
    }
  }
}
</script>
<style>
#author_skill{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
}
.bar_box{
  width: 80vw;
  height: 50px;
}
.skill_name{
  color: gray;
  margin-bottom: 5px;
  cursor: pointer;
}
.back_white{
  position: absolute;
  width: 80vw;
  height: 20px;
  background-color: #DDDDDD;
}
.process_bar{
  position: absolute;
  width: 0;
  height: 20px;
  background:linear-gradient(right,#2DE,#77E);
  text-align: center;
  line-height: 20px;
}
</style>