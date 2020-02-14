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
    skill(context){
      context.beginPath()
      context.translate(18,18)
      context.moveTo(3,-4)
      context.lineTo(-3,4)
      context.moveTo(6,-4)
      context.lineTo(12,0)
      context.lineTo(6,4)
      context.moveTo(-6,-4)
      context.lineTo(-12,0)
      context.lineTo(-6,4)
      context.strokeStyle = 'white'
      context.stroke()

    },
    experience(context){
      let degree = Math.asin(3/10)
      context.strokeStyle = 'white'
      context.beginPath()
      context.translate(18,18)
      context.arc(0,0,10,(-Math.PI/2 + degree),(Math.PI/6 - degree))
      context.stroke()
      context.beginPath()
      context.arc(0,0,10,(Math.PI/6 + degree),(Math.PI/6*5 - degree))
      context.stroke()
      context.beginPath()
      context.arc(0,0,10,(Math.PI/6*5 + degree),(Math.PI/2*3 - degree))
      context.stroke()
      context.beginPath()
      context.arc(0,-10,3,0,Math.PI * 2)
      context.stroke()
      context.beginPath()
      context.arc(8.6,5,3,0,Math.PI * 2)
      context.stroke()
      context.beginPath()
      context.arc(-8.6,5,3,0,Math.PI * 2)
      context.stroke()
      context.stroke()

    },
    project(context){
      context.beginPath()
      context.lineWidth = 0.5
      context.rect(9,9,6,6)
      context.rect(9,19,6,6)
      context.rect(19,19,6,6)
      context.strokeStyle = 'white'
      context.stroke()
      context.translate(22,12)
      context.rotate(45 * Math.PI / 180)
      context.lineWidth = 1
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