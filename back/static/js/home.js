//轮播图 to do 失焦停止轮换 程序改进 增加可读性 添加点击切换图片按钮
let current_img = 4
function carousel(){
  setInterval(function(){
    let i = 0
    //运行完一遍 初始话图片位置
    if(current_img==0){
      document.getElementById('carousel_2').style.right=''
      document.getElementById('carousel_3').style.right=''
      document.getElementById('carousel_4').style.left=''
      current_img = 4
    }
    //正常平移图片
    if(current_img > 1){
      let img = document.getElementById('carousel_' + current_img)
      let timeoutId = setInterval(function(){
        i++
        img.style.right = i + 'vw'
        if (i == 100){
          clearInterval(timeoutId)
        }
      },10)
    }
    //图片到1后 移动图片4覆盖
    else{
      let img_4 = document.getElementById('carousel_4')
      img_4.style.left = '100vw'
      img_4.style.right = ''
      let timeoutId = setInterval(function(){
        i++
        img_4.style.left = (100-i) + 'vw'
        if (i==100){
          clearInterval(timeoutId)
        }
      },10)
    }
    current_img--
  },5000)
}
window.onload = function(){
  carousel()
}
//竖直滚动 to do 增加可读性 节流更换更优秀方式
let current_page = 1
var ok = true

function up(id){
  let page = document.getElementById(id)
  let i =100
  var timeoutId = setInterval(function(){
    i--
    page.style.top = -i + 'vh'
    if (i==0){
      clearInterval(timeoutId)
    }
  },10)
  if (current_page>1){
    current_page --
  }
}
function down(id){
  let page = document.getElementById(id)
  let i =0
  let timeoutId = setInterval(function(){
    i++
    page.style.top = -i + 'vh'
    if (i==100){
      clearInterval(timeoutId)
    }
  },8)
  if (current_page<4){
    current_page++
  }
}
window.onwheel = function(){
    var e = e || window.event
    timer = setTimeout(function() {
      ok = true
    },600)
    if(ok){
      if((e.deltaY > 50) && (current_page < 4)){
        down('page_' + current_page)
        ok = false
      }
      else if((e.deltaY < -50) && (current_page > 1)){
        up('page_' + (current_page-1))
        ok = false
      }
    }
}
