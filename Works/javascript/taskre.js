
 let names = document.querySelector(".name");
 let surnames = document.querySelector(".surname");
 let input= document.querySelector(".input")
 
document.querySelector('.btn').addEventListener('click', (event) => {
    event.preventDefault();
    let result= document.createElement("div");
    result.className="result";
    let elem =["p","p","button"];
    let clas =["name","surname","buton"];
    for (let i=0;i<elem.length;i++){
        let element=document.createElement(elem[i]);
        element.className=clas[i];
        if(element.classList.contains("name")){
            element.textContent=names.value
        }
        else if(element.classList.contains("surname")){
            element.textContent=surnames.value
        }
        else if(element.classList.contains("buton")){
            element.textContent="Temizle"
        }
        
        result.appendChild(element);
    }
    document.querySelector(".input").appendChild(result);
   
    input.addEventListener("click", (e)=>{
        let klas =e.target.getAttribute("class");
        if(klas =="buton"){
            let parent=e.target.querySelector(".buton").parentElement;
            input.removeChild(parent);
        }
    })
    

   
   
});


