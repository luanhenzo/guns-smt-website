const menu = document.querySelector('#nav');
const menuAnchors = document.querySelectorAll('#nav a');
let isOpen = false;

function changeMenu() {
    let menuHeight = menu.offsetHeight
    console.log(menuHeight)

    if (!isOpen) {
        menu.style.top = `${menuHeight}px`;
        for (let i = 0; i < menuAnchors.length; i = i + 1 ) {
            menuAnchors[i].style.pointerEvents = 'auto'
        }
        isOpen = true;
    } else {
        menu.style.top = '0';
        for (let i = 0; i < menuAnchors.length; i = i + 1 ) {
            menuAnchors[i].style.pointerEvents = 'none'
        }
        isOpen = false;
    }
}