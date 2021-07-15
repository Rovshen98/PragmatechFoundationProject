let myform = document.querySelector("form");
let fullname = document.querySelector("input.fullname");
let email = document.querySelector("input.email");
let theme = document.querySelector("input.theme");
let textarea = document.querySelector("input.tarea");



myform.addEventListener("submit", (e)=> {
     e.preventDefault();
     
    fullname.classList.add("fail");
     
});
    

    

