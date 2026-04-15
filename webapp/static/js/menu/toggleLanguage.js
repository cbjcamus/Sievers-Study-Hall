function toggleLangMenu() {
    var menu = document.getElementById('lang-menu');
    var btn  = document.querySelector('.lang-button');
    var isOpen = menu.classList.toggle('show');
    if (btn) btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}

// close when clicking outside
document.addEventListener('click', function(e) {
    var menu = document.getElementById('lang-menu');
    var btn = document.querySelector('.lang-button');
    if (!menu || !btn) return;
    if (!menu.contains(e.target) && !btn.contains(e.target)) {
    if (menu.classList.contains('show')) {
        menu.classList.remove('show');
        btn.setAttribute('aria-expanded', 'false');
    }
    }
});