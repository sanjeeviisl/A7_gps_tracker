from pydub import AudioSegment
from pydub.playback import play
import io

data = open('parrot.mp3', 'rb').read()

song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
play(song)


