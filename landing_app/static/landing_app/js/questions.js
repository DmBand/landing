'use strict'

const container = document.querySelector('.questions-cotainer');

function activeQuestion(event) {
    if (event.target.tagName == 'H3') {
        event.target.classList.toggle('deg');
    }    
}

container.addEventListener('click', activeQuestion);