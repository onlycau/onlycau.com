<template>
  <div class="hi" @mouseout='change(1)'>
      <div @mouseover='change(-1)' @click="to_url(sth.url)">{{sth.name}} </div>
      <div class="dropdown" :style="{transform:transform}">
        <div v-for='blog_type in sth.types' class="drop_content" @click="to_blogs(blog_type)">{{blog_type}}</div>
      </div>
  </div>
</template>
<script>
export default{
  name:'NavTopChild',
  data(){
    return{
      isShow:true,
      degree:90,
      timeoutId:0,
    }
  },
  computed:{
    transform:function(){
      return 'rotateY(' + this.degree + 'deg)'
    }
  },
  props:['sth'],
  methods:{
    change(key){
      if(this.timeoutId){
        clearInterval(this.timeoutId)
      }
      this.timeoutId = setInterval(()=>{
        this.degree += key
        if(this.degree % 90 === 0){
          clearInterval(this.timeoutId)
          this.timeoutId = 0
        }
      },10)
    },
    to_url(url){
      this.$router.push('/' + url)
    },
    to_blogs(blog_type){
      this.$router.replace('/blogs/'+blog_type)
    },
}
}
</script>

<style type="text/css">
.hi{
  margin: 0px;
  padding-left: 0px;
  background-color: #C8C8A9;
  display: inline-block;
  font-size: 150%;
  text-align: center;
  width: 130px;
  z-index: -1;
  cursor: pointer;
}
.hi:hover{
  background-color: #D1BA74;
}
.dropdown {
  transform:rotateY(90deg);
  position: absolute;
  text-align: left;
  width: 100px;
  padding-left: 15px;
  padding-right: 15px;
  background-color: #D1BA74;
}
</style>