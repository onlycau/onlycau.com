<template>
  <div id="author_contact">
    <div class="flex_box">
      <div class="short_word">
        <span>编程</span>
        <span>无畏</span>
        <span>梦想</span>
        <span>飞翔</span>
      </div>
      <div class="self_evaluation">
        <div>阅读影视</div>
        <div>爱探索，<span>不</span>爱学习</div>
        <div>享受生活，及时行乐</div>
        <div>编程即兴趣，代码即人生</div>
      </div>
      <div class="web_information">
        <div>
          <a href="http://github.com/onlycau" target="view_window"><img src="../../assets/github.svg">
          </a>
        </div>
        <div>
          <a href="https://www.zhihu.com/people/wu-yu-hao-7-94" target="view_window"><img src="../../assets/zhihu.svg">
          </a>
        </div>
        <div>
          <a href="http://onlycau.com" target="view_window"><img src="../../assets/blog.svg">
          </a>
        </div>
        <div>
          <a href="https://546359321@qq.com" target="view_window"><img src="../../assets/mail.svg">
          </a>
        </div>
      </div>
    </div>
    <div>
      <Footer></Footer>
    </div>
  </div>
</template>
<script>
import Footer from "../Footer.vue"
export default{
  name:'AuthorContact',
  components:{
    Footer
  }
}
</script>
<style>
#author_contact{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 100vw;
  height: 100vh;
}
.flex_box{
  flex: 0.8;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
/* 单词*/
.short_word{
  margin-top: 100px;
}
.short_word span{
  font-size: 140%;
  margin-left: 10px;
  margin-right: 10px;
}
.short_word span:nth-child(1){
  color: #0000CC;
}
.short_word span:nth-child(2){
  color: #993399;
}
.short_word span:nth-child(3){
  color: #339933;
}
.short_word span:nth-child(4){
  color: #FF0033;
}
/* 自我介绍*/
.self_evaluation div{
  font-size: 120%;
  color: white;
  margin-top: 10px;
  text-align: center;
}
.self_evaluation span{
  text-decoration: line-through red double;
}
/* 网络展现*/
.web_information div{
  display: inline-block;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  background: gray; 
  margin-left: 15px;
  margin-right: 15px;
}
.web_information img{
  width: 40px;
  height: 40px;
  transform: translate(12%,12%);
  cursor: pointer;
}
</style>