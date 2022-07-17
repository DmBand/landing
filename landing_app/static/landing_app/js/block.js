'use strict'

let product = 'chocolate';

const myObs = new ResizeObserver(entries => {    
    
    let oneProductDIV;
    let divListMain = [];
    let divList = [];
    let oneProduct = [];
    let productName = [];
    let productDescription = [];
    
    entries.forEach(e => {
        if (e.target.id === product) {
            oneProductDIV = e.target.childNodes; 
        }
        
        if (oneProductDIV) {
            oneProductDIV.forEach(e => {
                if (e.tagName == 'DIV' && e.className == 'one-product') {
                    divListMain.push(e);                    
                }            
            })

            divListMain.forEach(e => { 
                if (e.tagName === 'DIV') {
                    divList.push(e.childNodes);          
                }                     
            })

            divList.forEach(e => {
                oneProduct.push(e);             
            })

            oneProduct.forEach(e => {
                for (let tag of e) {
                    if (tag.tagName === 'P' && tag.className === 'product-name') {
                        productName.push(tag.clientHeight);
                    } else if (tag.tagName === 'P' && tag.className === 'product-description') {
                        productDescription.push(tag.clientHeight);
                    }
                }          
            })

            oneProduct.forEach(e => {
                for (let tag of e) {
                    if (tag.tagName === 'P' && tag.className === 'product-name') {
                        tag.style.minHeight = `${Math.max.apply(null, productName)}px`;
                    } else if (tag.tagName === 'P' && tag.className === 'product-description') {
                        tag.style.minHeight = `${Math.max.apply(null, productDescription)}px`;
                    }
                }
            })    
        }               
    })
})

function onLoad() {
    if (window.screen.availWidth > 660) {
        const defaultDiv = document.getElementById(product);
        myObs.observe(defaultDiv); 
    }
}

function changeHeight(event) {
    if (window.screen.availWidth > 660) {
        if (event.target.tagName == 'BUTTON') {
            product = event.target.dataset.product;
            const div = document.getElementById(product);
            myObs.observe(div);         
        }
    }
}

const catalogButtons = document.querySelector('.catalog-buttons');
document.addEventListener('DOMContentLoaded', onLoad);
catalogButtons.addEventListener('click', changeHeight);