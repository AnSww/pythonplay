//Settings
// Открыть модальное окно
document.getElementById("open-settings-btn").addEventListener("click", function() {
    document.getElementById("settings-modal").classList.add("open")
})

// Закрыть модальное окно
document.getElementById("close-settings-btn").addEventListener("click", function() {
    document.getElementById("settings-modal").classList.remove("open")
})

// Закрыть модальное окно при клике вне его
document.querySelector("#settings-modal .modal__box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("settings-modal").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});



//Certificate
// Открыть модальное окно
document.getElementById("open-certificate-btn").addEventListener("click", function() {
    document.getElementById("certificate-modal").classList.add("open")
})

// Закрыть модальное окно
document.getElementById("close-certificate-btn").addEventListener("click", function() {
    document.getElementById("certificate-modal").classList.remove("open")
})

// Закрыть модальное окно при клике вне его
document.querySelector("#certificate-modal .modal__certificate").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("certificate-modal").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});

//achievement
// Открыть модальное окно
document.getElementById("open-achievement-btn").addEventListener("click", function() {
    document.getElementById("achievement-modal").classList.add("open")
})

// Закрыть модальное окно
document.getElementById("close-achievement-btn").addEventListener("click", function() {
    document.getElementById("achievement-modal").classList.remove("open")
})

// Закрыть модальное окно при клике вне его
document.querySelector("#achievement-modal .modal__achievement").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("achievement-modal").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});
