// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let totalBird = 0;
  
  for (let index = 0; index < birdsPerDay.length; index++) {
    totalBird += birdsPerDay[index];
  }

  return totalBird;
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  let birdsCount = 0;
  const firstDayWeek = (7 * week) - 6;
  const lastDayWeek = 7 * week;
  
  for (let index = firstDayWeek - 1; index < lastDayWeek; index++) {
    birdsCount += birdsPerDay[index];
  }

  return birdsCount;
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {void} should not return anything
 */
export function fixBirdCountLog(birdsPerDay) {
  
  for (let index = 0; index < birdsPerDay.length; index++) {
    if (index % 2 == 0) {
      birdsPerDay[index] = birdsPerDay[index] + 1;
    } else {
      continue
    }
  }
}
