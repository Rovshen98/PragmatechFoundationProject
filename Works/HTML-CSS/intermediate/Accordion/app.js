let accor= document.getElementsByClassName("accord")
let i
for(i=0;i < accor.length;i++){
    accor[i].addEventListener("click", function(){
      console.log(i)
        let panel = this.nextElementSibling;
        if(panel.style.display==="block"){
            panel.style.display="none"
            
        }
        else{
            
            panel.style.display="block"
        }
        

    });
}