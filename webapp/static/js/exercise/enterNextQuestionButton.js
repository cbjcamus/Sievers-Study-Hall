document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        const nextBtn = document.querySelector(".next-question-button");
        if (nextBtn && !document.getElementById("answer")) {
            event.preventDefault();
            nextBtn.click();
        }
    }
});