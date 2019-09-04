<template>
  <div id="AuthorProject">
    <div class="book">
      <div class="page_box" v-for='(value,index) in book' :key='value.id'>
        <div class="page_back page" @click='turning_prev(index)'>{{book[index][1]}}</div>
        <div class="page_positive page" @click='turning_next(index)'>{{book[index][0]}}</div>
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'AuthorProject',
  data(){
    return{
      book:[['pageA','pageB'],['pageC','pageD'],['pageE','pageF'],['pageG','pageH']]
    }
  },
  mounted(){
    for(let i in this.book){
      document.getElementsByClassName('page_positive')[i].style.zIndex = 100-i
      document.getElementsByClassName('page_back')[i].style.zIndex = i+100
    }
  },
  methods:{
    throttle(func,wait){
      return ()=>{
        let now = Date.now()
        let that = this
        let args = arguments
        if(now - this.previous > wait){
          func.apply(that, args)
          this.previous = now
        }
      }
    },
    turning_next(index){
      let ele_positive = document.getElementsByClassName('page_positive')[index]
      let ele_back = document.getElementsByClassName('page_back')[index]
      let degree_positive = 0
      let degree_back = -90

      let timeoutId_positive = setInterval(()=>{
        degree_positive += 2
        ele_positive.style.transform = 'rotateY(' + degree_positive + 'deg)'
        if(degree_positive === 90){
          clearTimeout(timeoutId_positive)
          let timeoutId_back = setInterval(()=>{
            degree_back += 2
            ele_back.style.transform = 'rotateY(' + degree_back + 'deg)'
            if(degree_back === 0){
              clearTimeout(timeoutId_back)
            }
          },16.7)
        }
      },16.7)
    },
    turning_prev(index){
      let ele_positive = document.getElementsByClassName('page_positive')[index]
      let ele_back = document.getElementsByClassName('page_back')[index]
      let degree_back = 0
      let degree_positive = 90

      let timeoutId_back = setInterval(()=>{
        degree_back -= 2
        ele_back.style.transform = 'rotateY(' + degree_back + 'deg)'
        if(degree_back === -90){
          clearTimeout(timeoutId_back)
          let timeoutId_positive = setInterval(()=>{
            degree_positive -= 2
            ele_positive.style.transform = 'rotateY(' + degree_positive + 'deg)'
            if(degree_positive === 0){
              clearTimeout(timeoutId_positive)
            }
          },16.7)
        }
      },16.7)
    }
  }
}
</script>
<style>
#AuthorProject{
  display: flex;
  width: 100vw;
  height: 100vh;
  justify-content: center;
  align-items: center;
}
.book{
  width: 80vw;
  height: 60vh;
}
.page_box{
  display: flex;
  position: absolute;
  width: 80vw;
  height: 60vh;
}
.page{
  width: 40vw;
  height: 60vh;
  border:1px solid #EEE;
  background-color: white;
}
.page_back{
  box-shadow: -4px -4px 5px 0;
  transform-origin: 100% 50% 0;
  transform: rotateY(-90deg);
}
.page_positive{
  box-shadow: 4px -4px 5px 0;
  transform-origin: 0 50% 0;
}
</style>