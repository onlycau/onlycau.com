<template>
  <div id="author_skill">
    <div class="bar_box" v-for="(value,name,index) in skill">
      <div class="skill_name" @click='add_length(index,value)'>{{name}}</div>
      <div class="back_white"></div>
      <div class="process_bar"></div>
    </div>
  </div>
</template>
<script>
export default{
  name:'AuthorSkill',
  data(){
    return{
      skill:{
        HTML:70,
        CSS:70,
        JavaScript:70,
        Mysql:55,
        Python:65,
        linux:50,
        git:50
      }
    }
  },
  methods:{
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
  background:linear-gradient(to right,#0000CC,#66CCFF);
}
</style>