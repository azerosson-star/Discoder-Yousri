const { createElement } = require("react")

cap = document.getElementById('capital')
taux = document.getElementById('taux')
dur = document.getElementById('duree')
mensualite = document.getElementById('mensualite')
nbMois = dur * 12



mens = (cap*taux/12)/(1 - Math.pow(1+taux/12, -nbMois))
console.log(mens)


calc(function(item)
{
let calc= item.getElementById('calc'); 
if(calc){
    item.addEventListener("click",function(){
        mensualite.innerHTML.createElement(mens)
    });

}
