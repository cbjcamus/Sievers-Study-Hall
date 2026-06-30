const hideOptionsWordOrderToggle = document.getElementById("hide-options-word-order-toggle");

if (hideOptionsWordOrderToggle) {
  hideOptionsWordOrderToggle.checked = true;

  fetch("/api/settings")
    .then(r => r.json())
    .then(s => {
      hideOptionsWordOrderToggle.checked = !!s.hide_options_word_order;
    })
    .catch(() => {
      hideOptionsWordOrderToggle.checked = true;
    });

  hideOptionsWordOrderToggle.addEventListener("change", () => {
    fetch("/api/settings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        hide_options_word_order: hideOptionsWordOrderToggle.checked
      })
    });
  });
}