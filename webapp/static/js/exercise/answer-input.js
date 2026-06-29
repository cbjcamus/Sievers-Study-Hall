window.onload = function () {
    const input =
        document.getElementById("input-answer") ||
        document.getElementById("local-mc-input");

    if (input) {
        input.focus();
    }
};

document.addEventListener("DOMContentLoaded", function () {

    // INPUT EXERCISE
    const inputAnswer = document.getElementById("input-answer");

    if (inputAnswer) {
        inputAnswer.addEventListener("keypress", function (event) {
            if (event.key === "Enter") {
                event.preventDefault();

                const submitBtn = document.getElementById("input-submit-button");

                if (submitBtn) {
                    submitBtn.click();
                }
            }
        });
    }

    // WORD ORDER EXERCISE
    document.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {

            const wordOrderSubmitBtn = document.getElementById("word-order-submit-button");

            if (wordOrderSubmitBtn) {
                event.preventDefault();
                wordOrderSubmitBtn.click();
            }
        }
    });

});