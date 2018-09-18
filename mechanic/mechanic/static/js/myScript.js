document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
  });


function myCarFunction(){
  
  
var myCars = ['Lexus', 'Alph Romeo', 'Honda', 'Nissan','VW', 'Skoda', 'Landrover', 'Kia', 'Mazda', 'Jaguar', 'Suzuki', 'Toyota', 'Volvo', 'SEAT', 'Hyundai', 'Ford','Peugeot','Audi','Mini','Mercedes', 'BMW'];
  
var theBest = myCars[Math.floor(Math.random() * myCars.length)];
document.getElementById("bestCar").innerHTML = theBest; 
}