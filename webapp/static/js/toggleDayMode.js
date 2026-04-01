const toggleInput = document.getElementById("mode-toggle");

if (toggleInput) {
  toggleInput.checked = false;

  fetch("/api/settings")
    .then(r => r.json())
    .then(s => {
      toggleInput.checked = (s.theme === "day");
      document.body.classList.toggle("day-mode", s.theme === "day");
      localStorage.setItem("theme", s.theme);
    })
    .catch(() => {
      toggleInput.checked = false;
      document.body.classList.remove("day-mode");
      localStorage.setItem("theme", "night");
    });

  toggleInput.addEventListener("change", () => {
    const theme = toggleInput.checked ? "day" : "night";

    document.body.classList.toggle("day-mode", theme === "day");
    localStorage.setItem("theme", theme);

    fetch("/api/settings", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ theme })
    });
  });
}