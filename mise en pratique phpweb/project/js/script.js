document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (!email || !password) {
                alert('Veuillez remplir tous les champs.');
                return;
            }

            if (password.length < 6) {
                alert('Le mot de passe est trop court.');
                return;
            }

            console.log('Tentative de connexion pour :', email);
          
        });
    }
});

