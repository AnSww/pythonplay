document.addEventListener('DOMContentLoaded', function () {
    const svg = document.querySelector('svg.road_vector');
    const path = svg.querySelector('path#motionPath');
    const length = path.getTotalLength(); // Получаем длину пути
    const numPoints = 20; // Желаемое количество точек
    const spacing = length / (numPoints + 1); // Рассчитываем расстояние между точками

    let n= 20;



                // Создаем шарик по вектору
    const movingObject = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    movingObject.setAttribute("id", "movingObject");
    movingObject.setAttribute("r", 40);
    movingObject.setAttribute("stroke", "#4A1757");
    movingObject.setAttribute("stroke-width", 4);
    movingObject.setAttribute("stroke-dasharray", "20 20");
    movingObject.setAttribute("fill", "#f5d8c6");
    svg.appendChild(movingObject);

    for (let i = 0; i <= numPoints; i++) {
        const point = path.getPointAtLength(i * spacing); // Получаем координаты точки на расстоянии i * spacing от начала пути
        const link = document.createElementNS("http://www.w3.org/2000/svg", "a");
        const levelUrl = `level${i}`;
        if (i<=n) {
            link.setAttributeNS("http://www.w3.org/1999/xlink", "href", levelUrl) // Устанавливаем ссылку
        }
        svg.appendChild(link);

        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("class", "dot");
        circle.setAttribute("cx", point.x);
        circle.setAttribute("cy", point.y);
        circle.setAttribute("r", 23);
        circle.setAttribute("fill", "#A781DA");
        if (i==0){
            circle.setAttribute("r", 27);
        }
        if (i==n){
            circle.setAttribute("fill", "#4A1757");
            circle.setAttribute("r", 27);
        }

        if (i < n) {
            circle.setAttribute("fill", "#4A1757");
            circle.setAttribute("stroke", "#A781DA");
            circle.setAttribute("stroke-width", 6);
        }
        link.appendChild(circle); // Добавляем круг внутрь ссылки

        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("class", "number");
        text.setAttribute("fill", "#4A1757");
        text.setAttribute("x", point.x);
        text.setAttribute("y", point.y);
if (i !== 0) {
    text.textContent = i.toString();
}
        if (i == n) {
            text.setAttribute("fill", "white");
        }
        if (i < n) {
            text.setAttribute("fill", "#A781DA");
        }
        link.appendChild(text); // Добавляем текст внутрь ссылки
    }


    let duration;
    // Устанавливаем длину пути для анимации до нужной отметки уровня
    const pathLength = spacing * n;
    if (n<=7){
        duration = 500;
    }
    else if(n<=15){
        duration = 750;
    }
    else{
        duration = 1000;
    }
    let startTime;

    // Для башки змеи

    requestAnimationFrame(animate);

    // Для отметок уровней
    svg.addEventListener('click', function (event) {
        if (event.target.tagName.toLowerCase() === 'text') {
            const link = event.target.parentNode;
            const href = link.getAttribute('href');
            window.location.href = href;
        }
    });
        function animate(time) {
        if (!startTime) startTime = time;
        const elapsedTime = time - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        const point = path.getPointAtLength(progress * pathLength);
        movingObject.setAttribute("cx", point.x);
        movingObject.setAttribute("cy", point.y);
        if (progress < 1) {
            requestAnimationFrame(animate);
        }

    window.scrollTo({
            top: point.y - window.innerHeight / 10,
            behavior: 'smooth'
        });
    }
});
