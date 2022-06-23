'use strict'

const hamburger = document.querySelector('.header-burger');
const navList = document.querySelector('.nav-list');
const body = document.querySelector('body');

function toggleMenu() {
    hamburger.classList.toggle('active');
    navList.classList.toggle('active');
    body.classList.toggle('lock')
}
hamburger.addEventListener('click', toggleMenu);
navList.addEventListener('click', toggleMenu);