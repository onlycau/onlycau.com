<template>
  <div id="author_experience">
    <div id="card" @click='test()'>some content</div>
  </div>
</template>
<script>
export default{
  name:'AuthorExperience',
  methods:{
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
  justify-content: center;
  align-items: center;
}
#card{
  width: 80vw;
  height: 40vh;
  background-color: rgba(0,0,0,0);
}
#card:hover{
  background-color: rgba(255,255,255,0.6);
  box-shadow: 0 0 10px 0;
}
</style>