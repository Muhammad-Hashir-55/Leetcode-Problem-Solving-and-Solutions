/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    let n = this.length
    if(n >0){
        return this[n-1]

    }
    else{
        return -1
    }
    
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
