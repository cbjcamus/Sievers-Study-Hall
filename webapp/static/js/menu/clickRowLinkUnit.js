document.querySelectorAll(".exercise-row").forEach(row => {
    row.addEventListener("click", event => {
        const link = row.querySelector(".exercise-link");

        if (!link) return;

        if (event.ctrlKey || event.metaKey) {
            window.open(link.href, "_blank");
        } else {
            window.location.href = link.href;
        }
    });
});

document.querySelectorAll(".refresh-form").forEach(form => {
    form.addEventListener("click", event => {
        event.stopPropagation();
    });
});