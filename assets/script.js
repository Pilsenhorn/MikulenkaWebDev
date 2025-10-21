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

  // Debug: ověříme, že DOMContentLoaded proběhl
  console.log("DOM fully loaded");
});

const form = document.querySelector("form");
if (!form) {
  console.error("Form not found! Check your selector.");
} else {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("Form submit clicked!");

    const data = new FormData(form);
    console.log("Form data:", Object.fromEntries(data.entries()));

    try {
      const res = await fetch("https://mikulenkawebdev.onrender.com/send", {
        method: "POST",
        body: data
      });

      console.log("Fetch response status:", res.status);

      if (res.ok) {
        alert("Zpráva odeslána!");
        form.reset();
      } else {
        const text = await res.text();
        console.error("Fetch error response:", text);
        alert("Chyba při odesílání: " + res.status);
      }
    } catch (err) {
      console.error("Fetch failed:", err);
      alert("Chyba při odesílání. Zkontrolujte konzoli.");
    }
  });
}
