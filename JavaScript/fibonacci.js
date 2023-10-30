function fibonacci(n) {
    let ar = []
    if(n>=1) ar.push(1)
    if(n>=2) ar.push(1)
    for (let index = 2; index < n; index++) {
        let len = ar.length
        ar.push(ar[len-1]+ar[len-2])
    }
    return ar
}

console.log(fibonacci(10))