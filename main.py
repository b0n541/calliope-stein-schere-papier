def sehrHoch():
    basic.show_leds("""
        . . . . .
                # # # # .
                # # # # #
                # . . . #
                # . . . #
    """)
    music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))

def on_button_a():
    global spiel
    spiel = 1
    basic.clear_screen()
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def papier2():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)

def on_button_b():
    global spiel
    spiel = 2
    basic.clear_screen()
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_gesture_shake():
    global zug2
    if spiel == 1:
        basic.clear_screen()
        basic.pause(1000)
        zug2 = randint(1, 3)
        if zug2 == 1:
            stein2()
        elif zug2 == 2:
            schere2()
        else:
            papier2()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def tief():
    basic.show_leds("""
        . . . . .
                # . # # #
                # # # # #
                # . . . #
                # . . . #
    """)
    music.play_tone(131, music.beat(BeatFraction.SIXTEENTH))
def hoch():
    basic.show_leds("""
        . . . . .
                # # # . #
                # # # # #
                # . . . #
                # . . . #
    """)
    music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
def mittel():
    basic.show_leds("""
        . . . . .
                # # . # #
                # # # # #
                # . . . #
                # . . . #
    """)
    music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
def stein2():
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # #
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        . . # . .
                . # # # .
                . # # # .
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # #
                . # # # .
                . . . . .
    """)
def schere2():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
    """)
    basic.show_leds("""
        . . # . .
                . . # . .
                . . # . .
                . # # # .
                . # # # .
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
    """)
zug2 = 0
spiel = 0
basic.show_string("Knopf A oder B drücken")

def on_forever():
    if spiel == 2:
        if input.pin_is_pressed(TouchPin.P0):
            tief()
        elif input.pin_is_pressed(TouchPin.P1):
            mittel()
        elif input.pin_is_pressed(TouchPin.P2):
            hoch()
        elif input.pin_is_pressed(TouchPin.P3):
            sehrHoch()
        else:
            basic.show_leds("""
                . . . . .
                                # # # # #
                                # # # # #
                                # . . . #
                                # . . . #
            """)
basic.forever(on_forever)
