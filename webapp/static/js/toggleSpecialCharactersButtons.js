const specialCharToggle = document.getElementById("special-character-toggle");

if (specialCharToggle) {
  specialCharToggle.checked = true;

  fetch("/api/settings")
    .then(r => r.json())
    .then(s => {
      specialCharToggle.checked = !!s.special_characters_enabled;
    })
    .catch(() => {
      specialCharToggle.checked = true;
    });

  specialCharToggle.addEventListener("change", () => {
    fetch("/api/settings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        special_characters_enabled: specialCharToggle.checked
      })
    });
  });
}