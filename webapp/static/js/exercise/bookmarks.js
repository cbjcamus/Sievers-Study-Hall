document.addEventListener("DOMContentLoaded", function () {
  const forms = document.querySelectorAll(".bookmark-form");
  if (!forms.length) return;

  forms.forEach(function (form) {
    form.addEventListener("submit", async function (event) {
      event.preventDefault();

      const icon = form.querySelector(".bookmark-icon");
      const full = form.dataset.iconFull;
      const empty = form.dataset.iconEmpty;

      const formData = new FormData(form);

      try {
        const response = await fetch(form.action, {
          method: "POST",
          body: formData,
          headers: { "X-Requested-With": "XMLHttpRequest" }
        });

        if (!response.ok) return;

        const data = await response.json();
        if (icon && full && empty && "bookmarked" in data) {
          icon.src = data.bookmarked ? full : empty;
        }
      } catch (err) {
        console.error("Bookmark error:", err);
      }
    });
  });
});