<template>
    <canvas :id='ps_msg[1]' class="my_canvas"></canvas>
</template>
<script>
export default{
  name:'MyCanvas',
  mounted(){
    let ele = document.getElementById(this.ps_msg[1])
    ele.width = 36
    ele.height = 36
    let context = ele.getContext("2d")
    // 黑圆
    context.beginPath()
    context.arc(18,18,18,0,Math.PI * 2)
    context.closePath()
    context.fillStyle = '#222222'
    context.fill()
    let str = 'this.' + this.ps_msg[0] + '(context)'
    eval(str)
  },
  props:['ps_msg'],
  methods:{
    house(context){
      // 白房子
      context.beginPath()
      context.moveTo(18,8)
      context.lineTo(8,16)
      context.lineTo(12,16)
      context.lineTo(12,24)
      context.lineTo(16,24)
      context.lineTo(16,16)
      context.lineTo(20,16)
      context.lineTo(20,24)
      context.lineTo(24,24)
      context.lineTo(24,16)
      context.lineTo(28,16)
      context.lineTo(18,8)
      context.closePath()
      context.strokeStyle = 'white'
      context.stroke()
    },
    project(context){
      context.strokeStyle = 'white'
      context.rect(9,9,6,6)
      context.rect(9,19,6,6)
      context.rect(19,19,6,6)
      context.stroke()
      context.translate(22,12)
      context.rotate(45 * Math.PI / 180)
      context.rect(-3,-3,6,6)
      context.stroke()
    },
    contact(context){
      context.beginPath()
      context.moveTo(9,12)
      context.lineTo(9,14)
      context.moveTo(9,16)
      context.lineTo(9,24)
      context.lineTo(27,24)
      context.lineTo(27,12)
      context.lineTo(9,12)
      context.lineTo(18,18)
      context.lineTo(27,12)
      context.strokeStyle = 'white'
      context.stroke()
    }
  }
}
</script>
<style>
</style>