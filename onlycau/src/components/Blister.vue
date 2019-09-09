<template>
  <div ref='blister' class="blister">{{ps_msg}}</div>
</template>
<script>
export default{
  name:'Blister',
  props:['ps_msg'],
  data(){
    return{
      scale:1,
    }
  },
  mounted(){
    this.change()
  },
  methods:{
    change(){
      let ele = this.$refs.blister
      let key = 0
      setInterval(()=>{
        key = this.scale<1.001?0.01:-0.01
        let timer = setInterval(()=>{
          this.scale += key
          ele.style.transform = 'scale(' + this.scale + ')'
          if(this.scale > 1.099 || this.scale < 1.01){
            clearTimeout(timer)
          }
        },100)
      },1100)
    }
  }
}
</script>
<style>
.blister{
  text-align: center;
  border-radius: 50%;
  line-height: 60px;
  height: 60px;
  width: 60px;
  background: radial-gradient(rgba(255,0,0,0),rgba(255,255,255,1))
}
</style>