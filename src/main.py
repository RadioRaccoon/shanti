# Beat tracking example

import librosa
import matplotlib.pyplot as plt
from pathlib import Path


# File Path
fp = Path(__file__).parents[1] / 'Samples' / 'Sea Shanty2.mp3'
print(fp)

if fp.exists() :
    wf, sr = librosa.load(fp)
    tempo, beat_frames = librosa.beat.beat_track(y=wf, sr=sr)

    print("Estimated tempo: {:.2f} beats per minute.".format(tempo))

    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    librosa.display.waveshow(wf, sr=sr, axis='time')

    plt.show()
