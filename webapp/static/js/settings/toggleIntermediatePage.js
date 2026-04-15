const feedbackToggle = document.getElementById("intermediate-feedback-page-toggle");

if (feedbackToggle) {
  feedbackToggle.checked = true;

  fetch("/api/settings")
    .then(r => r.json())
    .then(s => {
      feedbackToggle.checked = !!s.feedback_enabled;
    })
    .catch(() => {
      feedbackToggle.checked = true;
    });

  feedbackToggle.addEventListener("change", () => {
    fetch("/api/settings", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ feedback_enabled: feedbackToggle.checked })
    });
  });
}