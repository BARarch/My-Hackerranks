var countVal = 0
var counterBtn = document.createElement('button');
counterBtn.id = 'btn';
counterBtn.innerHTML = countVal;
counterBtn.style.background = '#FFFFFF';
document.body.appendChild(counterBtn);

counterBtn.onclick = function() {
    counterBtn.innerHTML = ++countVal;
};
