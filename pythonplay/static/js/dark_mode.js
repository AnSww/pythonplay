function darkmode() {
    const body = document.body;
    const buttons = document.querySelectorAll('.bnt');
    const wasDarkmode = localStorage.getItem('darkmode') === 'true';

    localStorage.setItem('darkmode', !wasDarkmode);
    body.classList.toggle('dark-mode', !wasDarkmode);
    buttons.forEach(button => {
        button.classList.toggle('dark-mode-bnt', !wasDarkmode);
    });

    // Сохраняем состояние классов кнопок в localStorage
    buttons.forEach(button => {
        const classList = button.classList;
        const isDarkModeBnt = classList.contains('dark-mode-bnt');
        localStorage.setItem(`button-${button.id}-darkmode`, isDarkModeBnt);
    });
}

document.querySelectorAll('.theme-mode').forEach(button => {
    button.addEventListener('click', darkmode);
});

function onload() {
    const body = document.body;
    const wasDarkmode = localStorage.getItem('darkmode') === 'true';

    body.classList.toggle('dark-mode', wasDarkmode);
    // Восстанавливаем состояние классов кнопок из localStorage
    const buttons = document.querySelectorAll('.bnt');
    buttons.forEach(button => {
        const isDarkModeBnt = localStorage.getItem(`button-${button.id}-darkmode`) === 'true';
        button.classList.toggle('dark-mode-bnt', isDarkModeBnt);
    });
}

document.addEventListener('DOMContentLoaded', onload);
