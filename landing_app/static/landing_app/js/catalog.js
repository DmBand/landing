'use strict'

const catalogBtn = document.querySelectorAll('.catalog-btn');
const catalogButtons = document.querySelector('.catalog-buttons');

function activeBtn(event) {       
    if (event.target.tagName == 'BUTTON') {
        const product = event.target.dataset.product; 
        catalogBtn.forEach((btn) => btn.classList.remove('btn-active'))
        event.target.classList.add('btn-active');
        const currentDiv = document.querySelector('.active-product');
        currentDiv.classList.remove('active-product');
        const div = document.querySelector(`.one-product-container-${product}`);
        div.classList.add('active-product')
    }   
}

catalogButtons.addEventListener('click', activeBtn)
