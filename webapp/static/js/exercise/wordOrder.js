const selectedContainer = document.getElementById("selected-words");
const availableContainer = document.getElementById("available-words");
const answerInput = document.getElementById("word-order-answer");

function setWordOrderContainerHeights() {
    const buttons = [...availableContainer.querySelectorAll(".word-order-word")];

    const originalParent = new Map();

    buttons.forEach(button => {
        originalParent.set(button, button.parentElement);
        selectedContainer.appendChild(button);
    });

    const requiredHeight = selectedContainer.offsetHeight;

    buttons.forEach(button => {
        originalParent.get(button).appendChild(button);
    });

    selectedContainer.style.height = `${requiredHeight}px`;
    availableContainer.style.height = `${requiredHeight}px`;
}

setWordOrderContainerHeights();

function updateAnswer() {
    const selectedWords = [...selectedContainer.querySelectorAll(".word-order-word")]
        .map(button => button.dataset.word);

    answerInput.value = selectedWords.join(" ");
}

function animateWordMove(clickedButton) {
    const buttons = [...document.querySelectorAll(".word-order-word")];
    const firstPositions = new Map();

    buttons.forEach(button => {
        firstPositions.set(button, button.getBoundingClientRect());
    });

    if (clickedButton.parentElement === availableContainer) {
        selectedContainer.appendChild(clickedButton);
    } else {
        availableContainer.appendChild(clickedButton);
    }

    buttons.forEach(button => {
        const firstPosition = firstPositions.get(button);
        const lastPosition = button.getBoundingClientRect();

        const deltaX = firstPosition.left - lastPosition.left;
        const deltaY = firstPosition.top - lastPosition.top;

        button.style.transform = `translate(${deltaX}px, ${deltaY}px)`;
        button.style.transition = "transform 0s";
    });

    requestAnimationFrame(() => {
        buttons.forEach(button => {
            button.style.transform = "translate(0, 0)";
            button.style.transition = "transform 200ms ease";
        });
    });
}

document.querySelectorAll(".word-order-word").forEach(button => {
    button.addEventListener("click", () => {
        animateWordMove(button);
        updateAnswer();
    });
});

// DRAG AND DROP
Sortable.create(selectedContainer, {
    group: "word-order",
    animation: 150,
    onSort: updateAnswer
});

Sortable.create(availableContainer, {
    group: "word-order",
    animation: 150,
    onSort: updateAnswer
});