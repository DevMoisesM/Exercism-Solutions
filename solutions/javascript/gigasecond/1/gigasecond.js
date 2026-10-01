//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (actualDate) => {
  const gigaSecond = 1000000000; 
  const copyActualDate = new Date(actualDate);

  copyActualDate.setSeconds(copyActualDate.getSeconds() + gigaSecond);

  return copyActualDate;
};
