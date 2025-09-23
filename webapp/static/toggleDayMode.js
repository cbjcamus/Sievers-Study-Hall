/*
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
*/

//<script>
const toggleInput = document.getElementById("mode-toggle");
if (toggleInput) {
  // For logged-in users: read from API; class already applied by server
  fetch("/api/settings").then(r=>r.json()).then(s => {
    toggleInput.checked = (s.theme === "day");
  });
  toggleInput.addEventListener("change", () => {
    const theme = toggleInput.checked ? "day" : "night";
    // update body instantly for better UX
    document.body.classList.toggle("day-mode", theme === "day");
    fetch("/api/settings", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({theme})
    });
  });
}
//</script>