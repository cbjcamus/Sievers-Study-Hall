document.querySelectorAll(".section-header").forEach(header => {
    header.addEventListener("click", () => {
        const section = header.closest(".section");

        section.classList.toggle("collapsed");

        const isCollapsed = section.classList.contains("collapsed");
        const button = header.querySelector(".section-toggle");

        if (button) {
            button.setAttribute("aria-expanded", !isCollapsed);
        }
    });
});