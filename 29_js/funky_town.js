// Daniel Keriazis, Raymond Wu (team DKRW)
// SoftDev1 pd7
// K28 -- Sequential Progression
// 2018-12-20

var fibonacci = (n) =>{
    if (n<=0)
        return 0;
    else if (n<=2)
        return 1;
    else
        return fibonacci(n-1) + fibonacci(n-2);
};

var gcd = (a,b) =>{
    if (a%b == 0)
        return b;
    else
        return gcd(b, a%b);

};

var students = ['peter','amit','jared', 'a','b'];
var randomStudent = () =>{
    var choice = Math.floor(Math.random() * students.length);
    return students[choice];
};

var answerElem = document.getElementById('mostRecentAnswer');

var doFib = () => {
    result = fibonacci(10);
    console.log(result);
    answerElem.innerHTML = result;
}

var doGCD = () => {
    result = gcd(50, 100);
    console.log(result);
    answerElem.innerHTML = result;
}

var doRandStudent = () => {
    result = randomStudent();
    console.log(result);
    answerElem.innerHTML = result;
}

var fibButton = document.getElementById("fib");
// console.log(fibButton);
// fibButton.addEventListener('click', ()=>console.log(fibonacci(10)) );
fibButton.addEventListener('click', doFib );

var gcdButton = document.getElementById("gcd");
// console.log(fibButton);
// gcdButton.addEventListener('click', ()=>console.log(gcd(50,100)) );
gcdButton.addEventListener('click', doGCD );

var randStudentButton = document.getElementById("randomStudent");
// console.log(fibButton);
// randStudentButton.addEventListener('click', ()=>console.log(randomStudent()) );
randStudentButton.addEventListener('click', doRandStudent );

// var c = document.getElementsByClassName('one');
// console.log(c);
// console.log(c[0]);



