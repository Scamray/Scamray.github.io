// Shared bits: the Watch on menu closes when you tap elsewhere, and scam cards render from scams.json.
document.addEventListener("click", e => {
  document.querySelectorAll("details.watch[open]").forEach(d => { if (!d.contains(e.target)) d.removeAttribute("open"); });
});
const YT = "https://www.youtube.com/@scamray";
function card(s) {
  const href = s.url || YT;
  const tags = [s.via, s.type, s.after].map(t => `<span>${t}</span>`).join("");
  return `<a class="vcard" href="${href}"><div class="thumb" style="background-image:url(assets/thumbs/${s.id}.jpg)"></div>
<h3>${s.title}</h3><p>${s.blurb}</p><div class="tags">${tags}</div></a>`;
}
// newest first: by posted date when posted, otherwise by planned order
const newest = (a, b) => (b.posted || "").localeCompare(a.posted || "") || b.order - a.order;
async function loadScams() { return (await fetch("scams.json")).json(); }
