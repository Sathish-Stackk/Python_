let numbers = [1, 2, 3, 4, 5];

function customMap(arr, callback) {
    let result = [];

    for (let i = 0; i < arr.length; i++) {
        result.push(callback(arr[i], i));
    }

    return result;
}

let squares = customMap(numbers, n => n * n);

console.log(squares);
