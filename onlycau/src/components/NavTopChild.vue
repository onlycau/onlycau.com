<template>
  <div class="navtop_child" @mouseenter='show()' @mouseleave='hide()'>
    <div class="dropdown_title" @click="to_url(sth.url)" :class="{on_dropdown:on}">{{sth.name}} </div>
    <div class="dropdown" v-show='show_dropdown'>
      <div v-for='(type,index) in sth.types' :key='type.id' class="drop_content" :class="{on_dropdown:on}" @click="to_blogs(type)">
        {{type}}
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'NavTopChild',
  props:['sth'],
  data(){
    return{
      on: false,
      show_dropdown: false,
      eles: '',
      timeoutId : 0,
      type_count : 0,
    }
  },
  mounted(){
    this.eles = this.$el.getElementsByClassName('drop_content')
    this.type_count = this.sth.types.length
  },
  methods:{
    show(){
      this.on = true
      this.show_dropdown = true
      if(this.sth.types.length<1){
        return
      }
      let index = 0
      let timeoutId_show = setInterval(()=>{
        let ele = this.eles[index]
        // 标签未翻转时degree设置为90 反之为当时值 
        let degree = ele.style.transform?(parseInt(/\d{1,2}/.exec(ele.style.transform)[0])):90
        // 翻转单个标签
        let timeoutId = setInterval(()=>{
          degree -= 1
          ele.style.transform = 'rotateY(' + degree + 'deg)'
          if(!this.on || (degree%90===0)){
            clearInterval(timeoutId)
          }
        },5)
        if(!this.on || (++index === this.type_count)){
          clearTimeout(timeoutId_show)
        }
      },50)
    },
    hide(){
      this.on = false
      if(this.sth.types.length<1){
        return
      }
      let index = 0
      let timeoutId_hide = setInterval(()=>{
        let ele = this.eles[index]
        // 标签未翻转时degree设置为90 反之为当时值 
        let degree = ele.style.transform?(parseInt(/\d{1,2}/.exec(ele.style.transform)[0])):0
        // 翻转单个标签
        let timeoutId = setInterval(()=>{
          degree += 1
          ele.style.transform = 'rotateY(' + degree + 'deg)'
          if(this.on || (degree%90===0)){
            clearInterval(timeoutId)
          }
          if(!this.on && (degree === 90) && (index === this.type_count)){
            this.show_dropdown = false
          }
        },5)
        if(this.on || (++index === this.type_count)){
          clearTimeout(timeoutId_hide)
        }
      },50)
    },
    to_url(url){
      this.$router.push('/' + url)
    },
    to_blogs(blog_type){
      this.$router.push({path:('/blogs/'+blog_type)})
    },
  }
}
</script>

<style>
.navtop_child{
  position: relative;
  width: 130px;
  text-align: center;
  cursor: pointer;
}
/* 下拉菜单导航*/
.dropdown{
  position: absolute;
  z-index: 1;
  text-align: left;
}
/* 下拉菜单内容*/
.drop_content{
  width: 112px;
  height: 36px;
  line-height: 36px;
  padding-left: 18px;
  transform:rotateY(90deg);
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  border-radius: 2px;
  background-color: #C8C8A9;
}
.drop_content:hover{
  background-color: #C8C8A9;
}
.on_dropdown{
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  border-radius: 2px;
  background-color: #D1BA74;
}
</style>