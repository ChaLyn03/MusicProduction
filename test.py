from mido import Message, MidiFile, MidiTrack
import random

mid = MidiFile(ticks_per_beat=480)

voices = []
for _ in range(4):
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=0, time=0))
    voices.append(track)

# Pitch materials (intentionally clashing)
scales = [
    [60, 62, 63, 65, 67, 68, 71],      # C minor-ish
    [63, 65, 67, 68, 70, 72, 74],      # Eb lydian-ish
    [55, 57, 59, 60, 62, 64, 66],      # G chromatic cluster
    [48, 50, 51, 53, 55, 56, 59],      # Low-register instability
]

durations = [120, 240, 360, 480]  # irregular rhythmic grid

bars = 64
notes_per_bar = 6

for bar in range(bars):
    for v, track in enumerate(voices):
        scale = random.choice(scales)
        register_shift = random.choice([-12, 0, 12])

        for _ in range(notes_per_bar):
            note = random.choice(scale) + register_shift
            dur = random.choice(durations)

            track.append(Message('note_on', note=note, velocity=50, time=0))
            track.append(Message('note_off', note=note, velocity=50, time=dur))

mid.save("overcomplex_experiment.mid")
