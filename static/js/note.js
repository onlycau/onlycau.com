function show_blogs(p){
    var href = 'http://127.0.0.1:5000/blog/14'
    var a = document.createElement('a');
    a.setAttribute('href', href); 
    var a_text = document.createTextNode('14');
    a.appendChild(a_text);
    var position = document.getElementById(p);
    document.getElementsByClassName('month')[0].insertBefore(a, position)
}
function show_blogs2(p){
    var position = document.getElementById(p);
    added = "\<ul\>\<li\>\<a href='http://127.0.0.1:5000/blog/14'\>14\</a\>\</li\>\<li\>\<a href='http://127.0.0.1:5000/blog/13'\>13\</a\>\</li\>\<li\>\<a href='http://127.0.0.1:5000/blog/12'\>12\</a\>\</li\>\</ul\>"
    position.innerHTML = added;
}

function chkForm(){
    var password = document.getElementsByName('password')[0]
    var password2 = document.getElementsByName('password2')[0]
    if(password.value == password2.value){
        return true;}
    alert('different password');
    return false;
}
