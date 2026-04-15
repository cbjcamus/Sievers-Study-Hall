function toggleFlagForm(button) {
    const container = button.closest(".flag-form-container");
    const form = container.querySelector("form.flag-form");

    form.classList.toggle("hidden");

    if (!form.classList.contains("hidden")) {
      form.querySelector("textarea").focus();
    }
}