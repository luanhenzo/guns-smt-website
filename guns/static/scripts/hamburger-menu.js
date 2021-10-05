const menu = document.querySelector('#nav');
const menuAnchors = document.querySelectorAll('#nav a');
let isOpen = false;

function enableMenuAnchors() {
    for (let i = 0; i < menuAnchors.length; i = i + 1 ) {
            menuAnchors[i].style.pointerEvents = 'auto'
    }
}
function disableMenuAnchors() {
    for (let i = 0; i < menuAnchors.length; i = i + 1 ) {
            menuAnchors[i].style.pointerEvents = 'none'
    }
}

window.addEventListener('resize', function() {
    window.innerWidth > 800 ? enableMenuAnchors() : disableMenuAnchors()
}, true)
function changeMenu() {
    let menuHeight = menu.offsetHeight
    console.log(menuHeight)

    if (!isOpen) {
        menu.style.top = `${menuHeight}px`;
        enableMenuAnchors()
        isOpen = true;
    } else {
        menu.style.top = '0';
        disableMenuAnchors()
        isOpen = false;
    }
}