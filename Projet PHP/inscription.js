
const inputMdp = document.getElementById('mdp');
const iconOuvert = document.getElementById('icon-oeil-ouvert');
const iconFerme = document.getElementById('icon-oeil-ferme');

document.getElementById('toggle-mdp').addEventListener('click', () => {
    
    const isHidden = inputMdp.type === 'password';
    

    inputMdp.type = isHidden ? 'text' : 'password';
    
  
    iconOuvert.style.display = isHidden ? 'none' : 'block';
    iconFerme.style.display = isHidden ? 'block' : 'none';
});