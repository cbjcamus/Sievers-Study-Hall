document.addEventListener("DOMContentLoaded", () => {
    const savedScrollPosition = sessionStorage.getItem("resetScrollPosition");

    if (savedScrollPosition !== null) {
        window.scrollTo({
            top: Number(savedScrollPosition),
            behavior: "instant"
        });

        sessionStorage.removeItem("resetScrollPosition");
    }

    document.querySelectorAll(".refresh-form").forEach(form => {
        form.addEventListener("submit", () => {
            sessionStorage.setItem(
                "resetScrollPosition",
                String(window.scrollY)
            );
        });
    });
});