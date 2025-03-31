function updateCountdown() {
    const now = new Date();
    let year = now.getFullYear();
    
    // Set the birthday this year. 
    let birthDay = new Date(year, 5, 12, 0, 0, 0);

    // If passed, update the date to the next year.
    if (now > birthDay) {
        birthDay = new Date(year + 1, 5, 12, 0, 0, 0);
    }

    // Distance from now to birday. 
    const distance = birthDay - now;

    //Calculate days, hours, minutes, seconds.
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Animation to let the displayment more fluent
    function animateNumber(element, value) {
        if (element.textContent !== value.toString().padStart(2, '0')) {
            element.style.transform = 'rotateX(90deg)';
            setTimeout(() => {
                element.textContent = value.toString().padStart(2, '0');
                element.style.transform = 'rotateX(0deg)';
            }, 150);
        }
    }
    
    animateNumber(document.getElementById('days'), days);
    animateNumber(document.getElementById('hours'), hours);
    animateNumber(document.getElementById('minutes'), minutes);
    animateNumber(document.getElementById('seconds'), seconds);
}

updateCountdown();
setInterval(updateCountdown, 1000);