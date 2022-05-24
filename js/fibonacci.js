const fibonacci = (num) => {
    let result = 1;	
    let prevResult = 0;	
    if (num === 0){	
      return 0;	
    } else if (num === 1){	
      return 1;	
    }	
    for (let i = 2; i <= num; i++){	
      let tempResult = result;	
      result = result + prevResult;	
      prevResult = tempResult;	
    }	
    return result;
}

module.exports = {fibonacci}

console.log(fibonacci(3))