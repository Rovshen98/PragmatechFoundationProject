
 let names = document.querySelector(".name");
 let surnames = document.querySelector(".surname");
 
 
 document.querySelector('.btn').addEventListener('click', (event) => {
    event.preventDefault();
    let nametext  =document.createElement("p");
    document.body.appendChild(nametext)
    let surnametext =document.createElement("p");
    document.body.appendChild(surnametext);
    nametext.textContent = names.value;
    surnametext.textContent = surnames.value;
})