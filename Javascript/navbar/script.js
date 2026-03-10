let sub = document.querySelectorAll(".nav-links > div");

sub.forEach(function(item) {
    let submenu = item.querySelector(".subhidden");
    

    if (submenu) {
        submenu.classList.add("hidden"); 
    
        item.addEventListener("mouseenter", function() {
            submenu.classList.remove("hidden");
        });
        
        item.addEventListener("mouseleave", function() {
            submenu.classList.add("hidden");
        });
    }
    
  
    item.addEventListener("mouseenter", function() {
        item.style.transform = "scale(1.1)";
    });


    item.addEventListener("mouseleave", function() {
        item.style.transform = ""; 
    });
});

let navbar = document.querySelector(".navbar");
let bouton = document.getElementById('bouton')

bouton.addEventListener('click', () => {

  navbar.classList.toggle('verticale');
});