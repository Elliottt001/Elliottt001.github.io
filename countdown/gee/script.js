function updateCountdown() {
    const now = new Date();
    let year = now.getFullYear();
    
    let gaokaoDate = new Date(year, 5, 7, 9, 0, 0);
    
    if (now > gaokaoDate) {
        gaokaoDate = new Date(year + 1, 5, 7, 9, 0, 0);
    }
    
    const diff = gaokaoDate - now;
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);
    
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