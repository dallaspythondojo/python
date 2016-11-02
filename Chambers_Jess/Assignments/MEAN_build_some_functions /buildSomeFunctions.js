function runningLogger(){
    console.log("I am running!")
}

runningLogger();

function multiplyByTen(x) {
    console.log(x *= 10)
}

multiplyByTen(5);

function stringReturnOne() {
    console.log("hello")
}

function stringReturnTwo() {
    console.log("bye")
}

stringReturnTwo();
stringReturnOne();

function caller(x) {
    if (x === typeof function(){}){
        x()
    }
}

caller(stringReturnOne());

function myDoubleConsoleLog(x,y) {
    if (x && y === typeof function(){}){
        console.log(x);
        console.log(y);
    }
}

myDoubleConsoleLog(stringReturnOne(), stringReturnTwo());

function caller2(x) {
    console.log('starting');
    if (typeof(x) === 'function'){
        setTimeout(x, 2000)
    }
    console.log('ending');
    return 'Interesting'
}

caller2(stringReturnOne);
