const boutton = document.querySelector('#btn');
const page = document.querySelector('body');

boutton.addEventListener('click', () => {
    page.classList.toggle('dark');
    
    if (page.classList.contains('dark')) {
        boutton.textContent = "Passer en mode clair";
    } else {
        boutton.textContent = "Passer en mode sombre";
    }
});