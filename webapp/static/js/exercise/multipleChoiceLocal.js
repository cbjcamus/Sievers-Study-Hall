document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("local-mc-input");
    const button = document.getElementById("local-mc-submit");
    const options = document.getElementById("local-mc-options");
    const form = input.closest("form");

    function normalize(text) {
        return text.trim().toLowerCase();
    }

    button.addEventListener("click", () => {
        const userAnswer = input.value;
        const correctAnswer = window.LOCAL_MC_CORRECT;

        if (normalize(userAnswer) === normalize(correctAnswer)) {
            const hidden = document.createElement("input");
            hidden.type = "hidden";
            hidden.name = "answer";
            hidden.value = userAnswer;
            form.appendChild(hidden);

            form.submit();
        } else {
            options.style.display = "block";
            button.style.display = "none";
        }
    });

    input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            event.preventDefault();
            button.click();
        }
    });
});