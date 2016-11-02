var x = [3,5,"Dojo", "rocks", "Michael", "Sensei"];
for (var i = 0; i < x.length; i++) {
    console.log(x[i])
}
x.push(100);
x.push(["hello", "world", "Javascript is Fun"]);
console.log(x);

var sum = 0;
for (var i = 1; i <501; i++) {
    sum += i;
}
console.log(sum);

var arrTwo = [1,5,90,25,-3,0];
var min = 0;
for (var i = 0; i < arrTwo.length; i++) {
    if (arrTwo[i] < min) {
        min = arrTwo[i];
    }
}
console.log(min);

var sumTwo = 0;
for (var i = 0; i < arrTwo.length; i++) {
    sumTwo += arrTwo[i]
}
console.log(sumTwo/arrTwo.length);
