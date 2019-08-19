<template>
  <div class="carousel">
    <div class="carousel_nav">
      <div><span></span></div>
      <div><span></span></div>
      <div><span></span></div>
      <div><span></span></div>
      <div><span></span></div>
    </div>
    <div class="carousel_main"></div>
  </div>
</template>
<script>
export default{
  name:'Carousel'
}
</script>
<style>
.carousel{
  height: 220px;
  display: -webkit-flex; /* Safari */
  display: flex;
}
.carousel_nav{
  margin: 5px;
  height: 100%;
  width: 30%;
}
.carousel_nav > div{
  height: 20%;
  background-color: #C3D324;
}
.carousel_main{
  margin: 5px;
  height: 100%;
  background-color: #A934A2;
  width:70%;
}
</style>