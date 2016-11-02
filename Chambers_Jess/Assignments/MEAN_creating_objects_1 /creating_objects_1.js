function VehicleConstructor(name, numWheels, numPassengers) {
    var vehicle = {};
    vehicle.name = name;
    vehicle.numWheels = numWheels;
    vehicle.numPassengers = numPassengers;

    vehicle.makeNoise = function() {
        console.log("Beep Beep Beep")
    }
    return vehicle;
}

var Bike = VehicleConstructor("Minty", 2, 1);
Bike.makeNoise = function()
    {
        console.log('ring ring!');
    }
console.log(Bike.name);
Bike.makeNoise();

var Sedan = VehicleConstructor("Sadie", 4, 5);
Sedan.makeNoise = function()
    {
        console.log('Honk Honk!');
    }
console.log(Sedan.name);
Sedan.makeNoise();

var Bus = VehicleConstructor("Bussed", 8, 10);
Bus.pickUp = function(num)
    {
        Bus.numPassengers += num;
    }
Bus.pickUp(3);
console.log(Bus)
