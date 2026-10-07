// Scam cards. tools/build.py inlines this (with the scams.json data as SCAMS) into pages that list scams,
// so cards draw while the page is parsed instead of popping in after a fetch.
const YT = "https://www.youtube.com/@scamray";
function card(s) {
  const href = s.url || YT;
  const tags = [s.via, s.type, s.after].map(t => `<span>${t}</span>`).join("");
  // the square thumbnail already shows the scam's name, so the card skips a separate title
  return `<a class="vcard" href="${href}" aria-label="${s.title.replace(/"/g, "&quot;")}"><div class="thumb" role="img" aria-label="${s.title.replace(/"/g, "&quot;")}" style="background-image:url(assets/thumbs/${s.id}.jpg?v=sq1)"></div>
<p>${s.blurb}</p><div class="tags">${tags}</div></a>`;
}
// newest first: by posted date when posted, otherwise by planned order
const newest = (a, b) => (b.posted || "").localeCompare(a.posted || "") || b.order - a.order;
// only videos that are actually posted show on the site; SCAMS is written into the page by tools/build.py
const loadScams = () => SCAMS.filter(s => s.posted);
