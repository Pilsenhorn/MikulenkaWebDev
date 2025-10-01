console.log("Script loaded!");

document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("nav");
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  const hero = document.querySelector(".hero");

  const heroHeight = hero.offsetHeight;

  function updateHeader() {
    if (window.scrollY < heroHeight - 50) {
      nav.classList.add("nav-light");
      nav.classList.remove("nav-dark");

      menuToggle.classList.add("hamburger-light");
      menuToggle.classList.remove("hamburger-dark");
    } else {
      nav.classList.add("nav-dark");
      nav.classList.remove("nav-light");

      menuToggle.classList.add("hamburger-dark");
      menuToggle.classList.remove("hamburger-light");
    }
  }

  updateHeader();
  window.addEventListener("scroll", updateHeader);

  menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
  });
});


