document.addEventListener('DOMContentLoaded', function () {
    const svg = document.querySelector('svg');
    const path = document.querySelector('path');
    const length = path.getTotalLength(); // Получаем длину пути
    const numPoints = 22; // Желаемое количество точек
    const spacing = length / (numPoints + 1); // Рассчитываем расстояние между точками

    for (let i = 1; i <= numPoints; i++) {
        const point = path.getPointAtLength(i * spacing); // Получаем координаты точки на расстоянии i * spacing от начала пути
        const link = document.createElementNS("http://www.w3.org/2000/svg", "a");
        const levelUrl = `level${i}`;
        link.setAttributeNS("http://www.w3.org/1999/xlink", "href", levelUrl) // Устанавливаем ссылку
        svg.appendChild(link);

        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("class", "dot");
        circle.setAttribute("cx", point.x);
        circle.setAttribute("cy", point.y);
        circle.setAttribute("r", 23);
        link.appendChild(circle); // Добавляем круг внутрь ссылки

        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("class", "number");
        text.setAttribute("x", point.x);
        text.setAttribute("y", point.y);
        text.textContent = i.toString();
        link.appendChild(text); // Добавляем текст внутрь ссылки
    }
    svg.addEventListener('click', function (event) {
        if (event.target.tagName.toLowerCase() === 'text') {
            const link = event.target.parentNode;
            const href = link.getAttribute('href');
            window.location.href = href; // Переход на URL ссылки
        }
    });
});

