var headone = document.querySelector('#one')
var headtwo = document.querySelector('#two')

headone.addEventListener('Hello',function(){
    headone.textcontent="HELLO,DOM WORLD!";
    headone.style.color="red";
})
headtwo.addEventListener('Welcome',function(){
    headtwo.textcontent="WELCOME TO HOMEPAGE";
    headtwo.style.color="blue";
})
