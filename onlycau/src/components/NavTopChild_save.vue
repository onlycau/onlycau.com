<template>
  <div  @mouseover='show()'@mouseout='hide()' class="hi">
    <div @click="to_url(sth.url)">{{sth.name}}
    </div>
    <div v-show='isShow' class="dropdown">
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
    }
  },
  props:['sth'],
  methods:{
    show(){
      // this.$data.isShow=true
      let ele = document.getElementsByClassName('dropdown')
      ele[2].style.transform = 'rotateY(10deg)'
    },
    hide(){
      // this.$data.isShow=false
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
  transform:rotateY(50deg);
  position: absolute;
  text-align: left;
  width: 100px;
  padding-left: 15px;
  padding-right: 15px;
  background-color: #D1BA74;
}
</style>