
window.addEventListener('load', () => {
  const wrapper = document.querySelector(".wrapper");
  wrapper.classList.add("wrapper-finish");
});




let head_1=document.querySelector(".head_1");
let burger = document.querySelector(".burger");
let menu = document.querySelector(".menu");

document.onclick = function(e){
      
      if (e.target.className !== 'menu' && e.target.className !== 'burger'){
      
      menu.classList.remove("active")
  }
};

burger.onclick = function() {
     menu.classList.toggle("active");
     
};





let x = document.querySelector(".top-to");
window.addEventListener("scroll", () => {
  if (document.body.scrollTop > 130 || document.documentElement.scrollTop > 130) {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
});

function topfunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}