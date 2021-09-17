
window.addEventListener('load', () => {
  const wrapper = document.querySelector(".wrapper");
  wrapper.classList.add("wrapper-finish");
});


let burger = document.querySelector(".burger");
let menu = document.querySelector(".menu");
burger.addEventListener("click", () => {
  menu.classList.toggle("active");
});
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