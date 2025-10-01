/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let x = []
    let n = arr.length
    for (let i = 0;i<n;i++){
        if(fn(arr[i],i)){
            x.push(arr[i])
        }
    }
    return x
    
};
