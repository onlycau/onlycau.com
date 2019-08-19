<template>
  <div class="navtop_child" :class="{on:on}" @mouseenter='show()' @mouseleave='hide()'>
      <div @click="to_url(sth.url)">{{sth.name}} </div>
      <div class="dropdown" v-show='show_dropdown'>
        <div v-for='(blog_type,index) in sth.types' :key='index' class="drop_content" :class="blog_type" @click="to_blogs(blog_type)">
          {{blog_type}}
        </div>
      </div>
  </div>
</template>
<script>
export default{
  name:'NavTopChild',
  data(){
    return{
      on:false,
      on_show:false,
      on_hide:false,
      show_dropdown:false,
    }
  },
  computed:{
    transform:function(){
      return 'rotateY(' + this.degree + 'deg)'
    }
  },
  props:['sth'],
  methods:{
    show(n){
      this.on = true
      if(this.sth.types.length<2){
        return
      }
      // 显示下拉元素
      this.show_dropdown = true
      this.on_hide = false
      this.on_show = true
      setTimeout(()=>{
        let begin = 0
        let timeoutId_total = setInterval(()=>{
          let ele = document.getElementsByClassName(this.sth.types[begin])[0]
          let degree = 90
          // 元素未完全翻转时 获取其角度值
          if(ele.style.transform){
            degree = parseInt(/\d{1,2}/.exec(ele.style.transform)[0])
          }
          let timeoutId_one = setInterval(()=>{
            degree -= 1
            ele.style.transform = 'rotateY(' + degree + 'deg)'
            if(this.on_hide||(degree%90===0)){
              clearInterval(timeoutId_one)
            }
          },10)
          begin+=1
          if(this.on_hide||begin>this.sth.types.length-1){
            clearInterval(timeoutId_total)
          }
        },100)
      },100)
    },
    hide(n){
      this.on = false
      if(this.sth.types.length<2){
        return
      }
      this.on_show = false
      this.on_hide = true
      setTimeout(()=>{
        let begin = this.sth.types.length-1
        let timeoutId_total = setInterval(()=>{
          // 记录下拉菜单消失到第几个了(外部定时机结束时begin已为-1，)
          let key_show_dropdown = begin
          let ele = document.getElementsByClassName(this.sth.types[begin])[0]
          let degree = 0
          // 元素未完全翻转时 获取其角度值
          if(ele.style.transform){
            degree = parseInt(/\d{1,2}/.exec(ele.style.transform)[0])
          }
          let timeoutId_one = setInterval(()=>{
            degree += 1
            ele.style.transform = 'rotateY(' + degree + 'deg)'
            if(this.on_show||(degree%90===0)){
              clearInterval(timeoutId_one)
              if(this.show_dropdown&&!key_show_dropdown&&degree===90){
                this.show_dropdown = false
              }
            }
          },10)
          begin-=1
          if(this.on_show||begin<0){
            clearInterval(timeoutId_total)
          }
        },100)
      },100)
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

<style scoped>
.navtop_child{
  margin: 0px;
  padding-left: 0px;
  display: inline-block;
  font-size: 150%;
  text-align: center;
  width: 130px;
  cursor: pointer;
}
.dropdown {
  width: 130px;
  margin: 0;
  position: absolute;
  z-index: 1;
  text-align: left;
}
.drop_content{
  line-height: 36px;
  height: 36px;
  transform:rotateY(90deg);
  padding-left: 15px;
  padding-right: 15px;
  background-color: #C8C8A9;
}
.drop_content:hover{
  background-color: #D1BA74;
}
.on{
  background-color: #D1BA74;
}
</style>