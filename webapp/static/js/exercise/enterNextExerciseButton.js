document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        const btn = document.querySelector(".next-exercise-button");
        if (btn) {
            btn.click();
        }
    }
});