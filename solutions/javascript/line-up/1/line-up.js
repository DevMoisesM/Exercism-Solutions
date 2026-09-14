//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  let strNumber = number.toString();
  const numberEnding = strNumber.slice(strNumber.length - 1);
  const numberEnding2Digits = strNumber.slice(strNumber.length - 2);

  if (numberEnding === "1" && numberEnding2Digits !== "11") {
    strNumber += "st";
  } else if (numberEnding === "2" && numberEnding2Digits !== "12") {
    strNumber += "nd";
  } else if (numberEnding === "3" && numberEnding2Digits !== "13") {
    strNumber += "rd";
  } else {
    strNumber += "th";
  }

  return name + ", you are the " + strNumber + " customer we serve today. Thank you!"
};
