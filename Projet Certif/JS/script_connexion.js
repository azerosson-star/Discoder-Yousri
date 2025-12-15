document.addEventListener('DOMContentLoaded', function() {
    
    // Sélection des éléments
    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    // Écoute du clic sur l'icône
    togglePassword.addEventListener('click', function () {
        
        // 1. Basculer le type de l'input : password <-> text
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        
        // 2. Basculer l'icône : oeil <-> oeil barré
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    });
});