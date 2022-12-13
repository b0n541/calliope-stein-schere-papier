let zug2 = 0
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    basic.clearScreen()
    basic.pause(1000)
    zug2 = randint(1, 3)
    if (zug2 == 1) {
        stein()
    } else if (zug2 == 2) {
        schere()
    } else {
        papier()
    }
})
function papier () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
}
function stein () {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        . # # # .
        . # # # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . . . .
        `)
}
function schere () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        . # # # .
        `)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
}
