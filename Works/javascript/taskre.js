
 let names = document.querySelector(".name");
 let surnames = document.querySelector(".surname");
 let input= document.querySelector(".input")
 
document.querySelector('.btn').addEventListener('click', (event) => {
    event.preventDefault();
    let result= document.createElement("div");
    result.className="result";
    let elem =["p","p"];
    let clas =["name","surname"];
    for (let i=0;i<elem.length;i++){
        let element=document.createElement(elem[i]);
        element.className=clas[i];
        if(element.classList.contains("name")){
            element.textContent=names.value
        }
        else if(element.classList.contains("surname")){
            element.textContent=surnames.value
        }
      
        
        result.appendChild(element);
    }
    document.querySelector(".input").appendChild(result);
   

    
    

   
   
});


