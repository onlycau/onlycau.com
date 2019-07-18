new Vue({
  el:'#nav_top',
  methods:{
    show_dropdown:function(){
      this.$el.getElementsByTagName('div')[0].style.display='block',
      this.$el.getElementsByTagName('div')[0].style.backgroundColor='#D1BA74'
    },
    dis_dropdown:function(){
      this.$el.getElementsByTagName('div')[0].style.display='none'
    },
    new_sort:function(sort){
      return (vm.change_sort(sort))
    }
  },
})
//服务器指定url请求一个json数据包得到反序列话后的对象
function my_request(sort,action='get', async=false){
  var xmlhttp = new XMLHttpRequest;
  xmlhttp.open(action,"/get_blogs/?sort=" + sort,async);
  xmlhttp.send();
  return JSON.parse(xmlhttp.responseText);
  /*暂时不用异步
  xmlhttp.onreadystatechange = function(){
    if(xmlhttp.readyState==4 && xmlhttp.status ==200){
      return JSON.parse(xmlhttp.responseText);
    }
  }*/
}
//

var blogs = my_request("homepage")
var count = 0
var componnet_summary = {
      data:function(){
        if (blogs[count] === undefined){
          blogs = my_request("homepage")
        }
        blogs[count].text = blogs[count].text.slice(0,200) + '......';
        return blogs[count++]
      },
      template:"<div class='overview'><div class='overview_top'><span class='blog_sort'>{{sort}}</span><span class='blog_title'>{{title}}</span></div><div class='blog_text'><p>{{text}}</p></div><div class='overview_bottom'><span class='blog_author'>作者:{{author}}</span><span class='blog_date'>时间:{{date}}</span></div></div>"
    }
var vm = new Vue({
  el:'#blogs',
  data:{
    hack_reset:true
  },
  components:{
    'div-summary':componnet_summary

  },
  methods:{
    change_sort:function(sort){
      count = 0
      blogs = my_request(sort)
      this.hack_reset = false
      this.$nextTick(()=>{
        this.hack_reset=true
      })
    }
  }
})