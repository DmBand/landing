'use strict'

const container = document.querySelector('.questions-cotainer');
const title = document.querySelectorAll('.question-title');
const qustion = document.querySelectorAll('.question-text');

function activeQuestion(event) {
    event.target.classList.toggle('deg');
    const div = event.target.nextElementSibling;
    div.classList.toggle('active-text');
}

container.addEventListener('click', activeQuestion);