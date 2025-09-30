/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let n = arr.length
    let idx = 0
    let f = []
    while(idx < n){
        let temp = []
        for (let i=0;i<size;i++){
            temp.push(arr[idx])
            idx +=1
            if(idx == n){
                break
            }

        }
        f.push(temp)
    }
    return f
};
