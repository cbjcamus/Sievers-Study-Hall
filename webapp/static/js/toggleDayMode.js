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