function personConstructor(name){
    var person = {
        name: name,
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
    };
    return person;
}

x = personConstructor('Jess').say_something('Hokay').walk();
x.run();

function ninjaConstructor(name, cohort) {
    var ninja = {
        name: name,
        cohort: cohort,
        belts: ['Yellow', 'Red', 'Black'],
        level: 0,
        level_up: function(){
            if (ninja.level < 2) {
                ninja.level += 1;
                belt = ninja.belts[ninja.level]
            }
            return ninja;
        }
    }
    return ninja;
}

y = ninjaConstructor('Jess', 'Dallas').level_up();
console.log(y);
y.level_up()
console.log(y);
