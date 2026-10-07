// Shared bits: the Watch on menu closes when you tap elsewhere, and the sticky header line. Card helpers live in cards.js.
document.addEventListener("click", e => {
  document.querySelectorAll("details.watch[open]").forEach(d => { if (!d.contains(e.target)) d.removeAttribute("open"); });
});
// Sticky header: show its bottom line once the page has scrolled
(() => {
  const h = document.querySelector(".site-head");
  if (!h) return;
  const on = () => h.classList.toggle("scrolled", window.scrollY > 4);
  on(); window.addEventListener("scroll", on, { passive: true });
  // lets sticky bars sit right under the header
  const hh = () => document.documentElement.style.setProperty("--headh", h.offsetHeight + "px");
  hh(); new ResizeObserver(hh).observe(h);
})();
