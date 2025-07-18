const feedbackToggle = document.getElementById("intermediate-feedback-page-toggle");

if (feedbackToggle) {
  // Fetch current value from session
  fetch("/get-feedback-toggle")
    .then(res => res.json())
    .then(data => {
      feedbackToggle.checked = data.feedback_enabled;
    });

  // Update session when toggled
  feedbackToggle.addEventListener("change", () => {
    fetch("/set-feedback-toggle", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        feedback_enabled: feedbackToggle.checked
      })
    });
  });
}