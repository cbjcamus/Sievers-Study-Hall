document.querySelectorAll(".unit-row").forEach(row => {
    row.addEventListener("click", () => {
        const link = row.querySelector(".unit-link");

        if (link) {
            window.location.href = link.href;
        }
    });
});