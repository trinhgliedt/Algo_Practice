// page 41 algorithm book
// Statistics to Doubles
// Implement a ‘die’ that randomly returns an
// integer between 1 and 6 inclusive. Roll a pair of
// these dice, tracking the statistics until doubles
// are rolled. Display the number of rolls , min , max ,
// and average .
function statisticToDoubles(){
    let die1 = null;
    let die2 = undefined;
    let rollCount = 0;
    while (die1 !== die2){
        die1 = Math.floor(Math.random()*6) + 1;
        die2 = Math.floor(Math.random()*6) + 1;
        console.log("die1: ", die1, ", die2: ", die2);
        rollCount ++;
    }
    // console.log("die1: ", die1, ", die2: ", die2);
    return rollCount;
}
console.log(statisticToDoubles());