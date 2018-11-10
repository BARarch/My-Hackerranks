'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowls = 'aeiou';
    for (let cha of s) {
        if (vowls.includes(cha)){
            console.log(cha);
        }        
    }
    for (let cha of s) {
        if (!(vowls.includes(cha))){
            console.log(cha);
        }        
    }
    
}
function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
