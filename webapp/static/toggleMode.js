const toggleButton = document.getElementById("mode-toggle");

// On page load:
const isDayMode = sessionStorage.getItem("mode") === "day";
if (isDayMode) {
  document.body.classList.add("day-mode");
}

if (toggleButton) {
  function updateButtonText(isDayMode) {
    toggleButton.textContent = isDayMode ? "Switch to Night Mode" : "Switch to Day Mode";
  }

    toggleButton.addEventListener("click", () => {
      const isDayMode = document.body.classList.toggle("day-mode");
      localStorage.setItem("mode", isDayMode ? "day" : "night");
      updateButtonText(isDayMode);
    });

  updateButtonText(isDayMode);
}
