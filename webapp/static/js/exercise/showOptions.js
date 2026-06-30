document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".show-options-button").forEach(button => {

        const targetId = button.dataset.target;
        const target = document.getElementById(targetId);

        if (!target) return;

        button.addEventListener("click", () => {
            target.style.display = "block";
            button.style.display = "none";
        });

    });
});