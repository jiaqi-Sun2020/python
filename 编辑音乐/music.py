from pydub import AudioSegment
second =1000 #
song = AudioSegment.from_mp3(r"1.mp3")
# (song[33*1000:63*1000])*2.export('end_of_time_slice.mp3')
ten_seconds = 10 * second
last_five_seconds = -5 * second
beginning = song[:ten_seconds] + 6
ending = song[last_five_seconds:] - 5

new_song = beginning + song[ten_seconds:last_five_seconds] + ending

new_song.export('45_1.mp3')

