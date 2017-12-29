function randomChance(quarters) {
    var winnings = 0;
    for (i = 0; i < quarters; i++) {
        var play = Math.floor(Math.random() * 100) + 1; //the chances of winning
        var win = Math.floor(Math.random() * 51) + 50; //chances of how much you win
        if (play === 100) { //the chances of winning 1 in 100
            winnings += win;
        }
    }
    return winnings;
}

randomChance(50);