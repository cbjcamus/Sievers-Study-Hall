const feedbackToggle = document.getElementById("intermediate-feedback-page-toggle");
if (feedbackToggle) {
  fetch("/api/settings").then(r=>r.json()).then(s => {
    feedbackToggle.checked = !!s.feedback_enabled;
  });
  feedbackToggle.addEventListener("change", () => {
    fetch("/api/settings", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({feedback_enabled: feedbackToggle.checked})
    });
  });
}