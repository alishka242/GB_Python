//пример callback

const arr = (callback) => {

    const summ = 1 + 1;
    setTimeout(() => {
        callback(summ);
    }, 2000);
    
}


const b = (content) => {
    console.log('hello', content);
}

arr(b);