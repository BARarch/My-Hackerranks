var res = document.getElementById('res');

var btn0 = document.getElementById('btn0');
var btn1 = document.getElementById('btn1');

var btnClr = document.getElementById('btnClr');
var btnEql = document.getElementById('btnEql');

var btnSum = document.getElementById('btnSum')
var btnSub = document.getElementById('btnSub')
var btnMul = document.getElementById('btnMul')
var btnDiv = document.getElementById('btnDiv')

var parseOpperands = function(results) {
    return results.match(/\d+/g);
};

btn0.onclick = function() {
    res.innerHTML = res.innerHTML + '0';
};

btn1.onclick = function() {
    res.innerHTML = res.innerHTML + '1';
};

btnClr.onclick = function() {
    res.innerHTML = '';
};

btnSum.onclick = function() {
    res.innerHTML = res.innerHTML + '+';
};

btnSub.onclick = function() {
    res.innerHTML = res.innerHTML + '-';
};

btnMul.onclick = function() {
    res.innerHTML = res.innerHTML + '*';
};

btnDiv.onclick = function() {
    res.innerHTML = res.innerHTML + '/';
};

btnEql.onclick = function() {
    var ex = res.innerHTML;
    var result;
    opperands = parseOpperands(ex).map(bi => parseInt(bi, 2));
    
    if (ex.match(/\+/)) {
        result = opperands[0] + opperands[1];
    }else if (ex.match(/\-/)) {
        result = opperands[0] - opperands[1];
    }else if (ex.match(/\*/)) {
        result = opperands[0] * opperands[1];
    }else if (ex.match(/\//)) {
        result = parseInt(opperands[0] / opperands[1]);
    }
    res.innerHTML = result.toString(2);
};
