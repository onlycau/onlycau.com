<template>
  <div id="AuthorProject">
    <div class="book">
      <div class=""></div>
      <div class="book_box" v-for='(value,index) in book' :key='value.id'>
        <div class="page_back page" @click='turning_prev(index)'>
          <div class="page_box">
            <div class="page_title">{{book[index][1].title}}</div>
            <ul class="page_text">
              <li v-for='item in book[index][1].text' :key='item.id'>{{item}}</li>
            </ul>
          </div>
        </div>
        <div class="page_positive page" @click='turning_next(index)'>
          <div class="page_box">
            <div class="page_title">{{book[index][0].title}}</div>
            <ul class="page_text">
              <li v-for='item in book[index][0].text' :key='item.id'>{{item}}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default{
  name:'AuthorProject',
  data(){
    return{
      book:[]
    }
  },
  created(){
    // 初始book数据
    function Page(title,text){
      this.title = title
      this.text = text
      Page.prototype.name = '个人博客'
    }
    let list_0 = ['博客的创建,访问,删除','用户的登录,注册,注销','博客的评论与网站留言(待完善)','作者的简历']
    let list_1 = ['博客导航下拉菜单','首页轮播图','简历介绍页全屏滚动与侧边固定导航栏','技能页百分比显示','仿书籍项目介绍']
    let list_2 = ['博客已有功能的完善,样式补充','浏览器兼容与手机端适配','响应式布局','功能添加与重构']
    let list_3 = ['先写的网站,后添加的简历页,样式和细节一直在尽力写得更好','除了axios和富文本编辑器,其他功能都是自己慢慢实现的','网站很丑,后面会重构','github.com/onlycau.com']
    let page_0 = new Page('功能',list_0)
    let page_1 = new Page('样式设计',list_1)
    let page_2 = new Page('to do',list_2)
    let page_3 = new Page('关于本网站',list_3)
    this.book = [[page_0,page_1],[page_2,page_3]]
  },
  mounted(){
    for(let i in this.book){
      document.getElementsByClassName('page_positive')[i].style.zIndex = 100 - i
      document.getElementsByClassName('page_back')[i].style.zIndex = 100 + i
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
.book_box{
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
/* 单页内容*/
.page_box{
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.page_title{
  text-align: center;
  font-size: 150%;
  color: red;
  margin: 50px;
}
.page_text li{
  line-height: 40px;
  margin-left: 20px;
}
</style>