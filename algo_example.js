const isMultiple = (i) => {
    if(i%3 == 0)
        console.log('Hello')
    if(i%5 == 0)
        console.log('World')
    if(i%7 == 0)
        console.log('Yoo')
    if(i%7!=0 && i%3!=0 && i%5!=0)
        console.log(i)
}

for (let i = 1; i <= 100; i++) {
    isMultiple(i);
} 