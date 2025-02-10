# CircuitPython I2S MP3 playback example.
# Plays a single MP3 once.
import board
import audiomp3
import audiobusio
import digitalio
import time

button = digitalio.DigitalInOut(board.GP22)
button.switch_to_input(pull=digitalio.Pull.UP)

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

audio = audiobusio.I2SOut(board.GP0, board.GP1, board.GP2)
mp3 = audiomp3.MP3Decoder(open("blue.mp3", "rb"))

while True:
    if not audio.playing and not button.value:
        print("playing audio")
        audio.play(mp3)

    time.sleep(0.1)
