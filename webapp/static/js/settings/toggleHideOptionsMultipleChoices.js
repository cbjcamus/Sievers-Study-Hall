const hideOptionsMultipleChoicesToggle = document.getElementById("hide-options-multiple-choices-toggle");

if (hideOptionsMultipleChoicesToggle) {
  hideOptionsMultipleChoicesToggle.checked = true;

  fetch("/api/settings")
    .then(r => r.json())
    .then(s => {
      hideOptionsMultipleChoicesToggle.checked = !!s.hide_options_multiple_choices;
    })
    .catch(() => {
      hideOptionsMultipleChoicesToggle.checked = true;
    });

  hideOptionsMultipleChoicesToggle.addEventListener("change", () => {
    fetch("/api/settings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        hide_options_multiple_choices: hideOptionsMultipleChoicesToggle.checked
      })
    });
  });
}