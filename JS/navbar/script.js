
const items = document.querySelectorAll(".nav-links > div")

items.forEach(function(item) {
    const submenu = item.querySelector("div:last-child")
    submenu.classList.add("hidden"); 
    
    item.addEventListener("mouseover", function() {
        submenu.classList.remove("hidden");
    })
    
    item.addEventListener("mouseout", function() {
        submenu.classList.add("hidden");
    })
})
