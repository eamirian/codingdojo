var amount = .01
var sum = .01
for (i = 2; i <= 30; i++) {
    amount = amount * 2;
    sum += amount;
    if (i == 30) {
        console.log("$" + sum)
    }
}