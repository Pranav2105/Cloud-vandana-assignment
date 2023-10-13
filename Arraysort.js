# Perform sorting of an array in descending order.
 const originalArray = [5, 1, 4, 2, 8];

// Sort the array in descending order
originalArray.sort(function(a, b) {
    return b - a;
});

console.log(originalArray); // Output will be [8, 5, 4, 2, 1]
 
