const instructionToggle = document.getElementById("instruction-page-toggle");

if (instructionToggle) {
  instructionToggle.checked = true;

  fetch("/api/settings")
    .then(r => r.json())
    .then(s => {
      instructionToggle.checked = !!s.instruction_page_enabled;
    })
    .catch(() => {
      instructionToggle.checked = true;
    });

  instructionToggle.addEventListener("change", () => {
    fetch("/api/settings", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        instruction_page_enabled: instructionToggle.checked
      })
    });
  });
}