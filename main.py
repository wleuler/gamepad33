gamePad.onEvent(GamerBitPin.P15, GamerBitEvent.Up, function () {
    radio.sendNumber(0)
    basic.showNumber(0)
})
gamePad.onEvent(GamerBitPin.P13, GamerBitEvent.Up, function () {
    radio.sendNumber(0)
    basic.showNumber(0)
})
gamePad.onEvent(GamerBitPin.P14, GamerBitEvent.Up, function () {
    radio.sendNumber(0)
    basic.showNumber(0)
})
gamePad.onEvent(GamerBitPin.P8, GamerBitEvent.Down, function () {
    radio.sendNumber(1)
    basic.showNumber(1)
})
gamePad.onEvent(GamerBitPin.P15, GamerBitEvent.Down, function () {
    radio.sendNumber(4)
    basic.showNumber(4)
})
gamePad.onEvent(GamerBitPin.P14, GamerBitEvent.Down, function () {
    radio.sendNumber(3)
    basic.showNumber(3)
})
gamePad.onEvent(GamerBitPin.P13, GamerBitEvent.Down, function () {
    radio.sendNumber(2)
    basic.showNumber(2)
})
gamePad.onEvent(GamerBitPin.P8, GamerBitEvent.Up, function () {
    radio.sendNumber(0)
    basic.showNumber(0)
})
radio.setGroup(1)
