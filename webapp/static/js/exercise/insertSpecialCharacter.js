function insertChar(char) {
    const input = document.getElementById('answer');
    const start = input.selectionStart;
    const end = input.selectionEnd;
    const text = input.value;
    input.value = text.slice(0, start) + char + text.slice(end);
    input.focus();
    input.setSelectionRange(start + 1, start + 1);
}