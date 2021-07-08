window.addEventListener('load', () =>{
    const wrapper= document.querySelector(".wrapper");
    wrapper.classList.add("wrapper-finish")
});

let burger = document.querySelector(".burger");
let menu= document.querySelector(".menu");

burger.addEventListener("click", ()=>{
    menu.classList.toggle("active")
})