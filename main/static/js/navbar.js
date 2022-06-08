const toggleBtn = document.getElementsByClassName('menu__toggle')[0];
const navMenu = document.getElementsByClassName('nav__list')[0];

toggleBtn.addEventListener('click', () => {
    navMenu.classList.toggle('active');
})