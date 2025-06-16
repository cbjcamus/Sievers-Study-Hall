const toggleInput = document.getElementById("mode-toggle");

// On page load:
const isDayMode = localStorage.getItem("mode") === "day";
if (isDayMode) {
  document.body.classList.add("day-mode");
  if (toggleInput) toggleInput.checked = true;
}

if (toggleInput) {
  toggleInput.addEventListener("change", () => {
    const isDayMode = toggleInput.checked;
    document.body.classList.toggle("day-mode", isDayMode);
    localStorage.setItem("mode", isDayMode ? "day" : "night");
  });
}