<!-- 已解决 快速进出标签乱翻转的问题 -->
<template>
  <div
    class="navtop_child" 
    :class='ClassObject'
    @mouseenter='transform(1)' 
    @mouseleave='transform(-1)'>
    <div
    class="dropdown_title"
    @click="to_url(nav_data.url)" >
      {{nav_data.name}} 
    </div>
    <div class="dropdown" v-show='status_code'>
      <div 
      v-for='type in nav_data.types' 
      :key='type.id'
      :class='{on_show:status_code>0}'
      class="drop_content" 
      @click="to_blogs(type)">
        {{type}}
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'NavTopChild',
  props:{
    nav_data:{
      type:Object
    }
  },
  data(){
    return{
      // 0:完全消失 1:出现中 -1:消失中  100:完全呈现
      status_code: 0,
      eles: '',
      type_count : 0,
      timeoutId: 0,
      count: 0,
      count_max: 0,
    }
  },
  computed:{
    degree_key(){
      return this.status_code % 100
    },
    ClassObject(){
      return {on_show:this.$route.path === this.nav_data.url || this.status_code > 0}
    }
  },
  mounted(){
    this.eles = this.$el.getElementsByClassName('drop_content')
    this.type_count = this.nav_data.types.length
    this.count = 90 + this.type_count * 10
    this.count_max = this.count
  },
  methods:{
    transform(i){
      this.status_code = i
      let eles = this.eles 
      if(this.timeoutId === 0){
        this.timeoutId = setInterval(()=>{
          this.count -= this.degree_key
          for(let i=0;i<this.type_count;i++){
            let degree = this.count - i * 10
            if(degree>90){
              degree = 90
            }else if(degree < 0){
              degree = 0
            }
            eles[i].style.transform = 'rotateY(' + degree + 'deg)'
          }
          if(this.count === 0 || this.count === this.count_max){
            clearTimeout(this.timeoutId)
            this.timeoutId = 0
            this.status_code = this.count === 0?100:0
          }
        },10)
      }
    },
    to_url(url){
      this.$router.push(url)
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
.on_show{
  background-color: #D1BA74;
}
</style>