'use strict'

const catalogBtn = document.querySelectorAll('.catalog-btn');
const catalogButtons = document.querySelector('.catalog-buttons');
const catalog = document.querySelector('.catalog');

function activeBtn(event) {
    const product = event.target.dataset.product;
    catalogBtn.forEach((btn) => btn.classList.remove('btn-active'))
    event.target.classList.add('btn-active');
    const currentDiv = document.querySelector('.active-product');
    currentDiv.classList.remove('active-product');
    const div = document.querySelector(`.one-product-container-${product}`);
    div.classList.add('active-product')
}

catalogButtons.addEventListener('click', activeBtn)


// const portfolioBtn = document.querySelectorAll('.btn-portfolio');
// const portfolioImg = document.querySelectorAll('.portfolio-img');


// const portfolioBtns = document.querySelector('.portfolio-buttons');

// const changeImage = function changeImage(event) {
//     if (event.target.classList.contains('btn-portfolio')) {
//         const season = event.target.dataset.season;
//         portfolioImg.forEach(
//             (img, index) => (img.src = `./assets/img/${season}/${index + 1}.jpg`));
//         portfolioBtn.forEach(
//             (btn) => btn.classList.remove('active'));
//         event.target.classList.add('active');
//     }
// };


//Кеширование

// function preloadSummerImages(folderName) {
//     for (let i = 1; i <= 6; i++) {
//         const img = new Image();
//         img.src = `./assets/img/${folderName}/${i}.jpg`;
//     }
// }

// const seasons = ['winter', 'spring', 'summer', 'autumn'];

// seasons.forEach(elem => preloadSummerImages(elem))

// //_____________________________