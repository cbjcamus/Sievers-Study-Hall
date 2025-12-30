function toggleGuidanceHelp(forceClose = false) {
  const overlay = document.getElementById("guidance-overlay");
  if (!overlay) return;

  const isOpen = overlay.classList.contains("is-open");
  const nextOpen = forceClose ? false : !isOpen;

  overlay.classList.toggle("is-open", nextOpen);
  overlay.setAttribute("aria-hidden", nextOpen ? "false" : "true");
}

document.addEventListener("click", function (e) {
  const overlay = document.getElementById("guidance-overlay");
  if (!overlay || !overlay.classList.contains("is-open")) return;
  if (e.target === overlay) toggleGuidanceHelp(true);
});

document.addEventListener("keydown", function (e) {
  const overlay = document.getElementById("guidance-overlay");
  if (!overlay || !overlay.classList.contains("is-open")) return;
  if (e.key === "Escape") toggleGuidanceHelp(true);
});