window.onload = function () {
  const answer = document.getElementById("answer");
  if (answer) answer.focus();
};

document.addEventListener("DOMContentLoaded", function () {
  const answer = document.getElementById("answer");
  if (!answer) return;

  answer.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      const submitBtn = document.getElementById("submit-button");
      if (submitBtn) submitBtn.click();
    }
  });
});