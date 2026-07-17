const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

const closeNavigation = () => {
  if (!navToggle || !navLinks) return;
  navToggle.setAttribute("aria-expanded", "false");
  navLinks.classList.remove("is-open");
};

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const isOpen = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isOpen));
    navLinks.classList.toggle("is-open", !isOpen);
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      closeNavigation();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeNavigation();
      navToggle.focus();
    }
  });

  document.addEventListener("click", (event) => {
    if (event.target instanceof Node && !navToggle.contains(event.target) && !navLinks.contains(event.target)) {
      closeNavigation();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 880) closeNavigation();
  });
}

const currentPage = window.location.pathname.split("/").pop() || "index.html";
document.querySelectorAll(".nav-links a").forEach((link) => {
  const linkPage = link.getAttribute("href")?.split("#")[0];
  if (linkPage === currentPage) link.setAttribute("aria-current", "page");
});
