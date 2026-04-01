// on impémente une classe pour gérer la nouvelle balise my-icon 
class IconComponent extends HTMLElement {

  connectedCallback() {

    const name = this.getAttribute("name");
    const spin = this.hasAttribute("spin");
    const classes = this.className;
    this.innerHTML = `<svg class="icon ${classes} ${spin ? "icon-spin" : ""}"><use href="#icon-${name}"></use></svg>`;
  }
}

// on intègre le fichier sprite dans le HTML
fetch('./assets/icons/sprite.svg')
  .then(response => response.text())
  .then(svg => {
    const container = document.createElement('div');
    container.style.display = 'none';
    container.innerHTML = svg;
    document.body.prepend(container);
  });

// on définie la nouvelle balise
customElements.define("my-icon", IconComponent);
