//
// This is only a SKELETON file for the 'Raindrops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const convert = (number) => {
  let raindropSound = "";

  if (number % 3 == 0) {
    raindropSound += "Pling";
  } 
  if (number % 5 == 0) {
    raindropSound += "Plang";
  }
  if (number % 7 == 0) {
    raindropSound += "Plong";
  }
  if (number % 3 != 0 && number % 5 != 0 && number % 7 != 0) {
    raindropSound = (number).toString();
  }

  return raindropSound;
};
