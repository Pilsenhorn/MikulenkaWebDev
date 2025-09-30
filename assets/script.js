console.log("Script loaded!");

document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("nav");
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  const hero = document.querySelector(".hero");

  const heroHeight = hero.offsetHeight;

  // funkce pro změnu stylu podle pozice
  function updateHeader() {
    if (window.scrollY < heroHeight - 50) {
      nav.classList.add("nav-light");
      nav.classList.remove("nav-dark");

      // hamburger bílý
      menuToggle.style.color = "white";
    } else {
      nav.classList.add("nav-dark");
      nav.classList.remove("nav-light");

      // hamburger primary
      menuToggle.style.color = "var(--primary-color)";
    }
  }

  // spustí se na začátku i při scrollu
  updateHeader();
  window.addEventListener("scroll", updateHeader);

  // hamburger toggle menu
  menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
  });
});
