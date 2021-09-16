const menu = document.querySelector('#nav');
let isOpen = false;

function changeMenu() {
    let menuHeight = menu.offsetHeight
    console.log(menuHeight)

    if (!isOpen) {
        menu.style.top = `${menuHeight}px`;
        isOpen = true;
    } else {
        menu.style.top = '0';
        isOpen = false;
    }
}