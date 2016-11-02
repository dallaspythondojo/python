
function sum(x, y) {
    var sum = 0
    for (var i = x; i <= y; i++) {
        sum += i;
    }
    console.log(sum);
}

sum(1, 2);

function min(arr){
    var min = arr[0];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    console.log(min);
}
min([1,5,90,25,-3,0]);

function avg(arr){
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i]
    }
    console.log(sum / arr.length);
}

avg([1,5,90,25,-3,0]);

//Anonymous functions assigned to variables.

var sum = function(x, y) {
    var sum = 0
    for (var i = x; i <= y; i++) {
        sum += i;
    }
    return sum;
}

var min = function(arr){
    var min = arr[0];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

var avg = function(arr){
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i]
    }
    return sum / arr.length;
}
var object = {
    sum: function(x, y) {
        var sum = 0
        for (var i = x; i <= y; i++) {
            sum += i;
        }
        return sum;
    },
    min: function(arr){
       var min = arr[0];
       for (var i = 0; i < arr.length; i++) {
           if (arr[i] < min) {
               min = arr[i];
           }
       }
       return min;
   },
    avg: function(arr){
          var sum = 0;
          for (var i = 0; i < arr.length; i++) {
              sum += arr[i]
          }
          return sum / arr.length;
      }
  }
var person = {
    name: "Jess",
    distance: 0,
    say_name: function(){
        console.log(person.name);
        return person
    },
    say_something: function(phrase) {
        console.log(person.name + " says: " + phrase);
        return person
    },
    walk: function(){
        console.log(person.name + " is walking.")
        person.distance += 3
        return person
    },
    run: function(){
        console.log(person.name + " is running.")
        person.distance += 10
        return person
    },
    crawl: function(){
        console.log(person.name + " is crawling.")
        person.distance += 1
        return person
    }
}

person.say_name().say_something('Hokay').walk().run().crawl();
