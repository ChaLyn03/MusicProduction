from mido import Message, MidiFile, MidiTrack

mid = MidiFile(ticks_per_beat=480)
track = MidiTrack()
mid.tracks.append(track)

# Set instrument to Acoustic Grand Piano
track.append(Message('program_change', program=0, time=0))

# Simple melody (C major)
notes = [
    60, 62, 64, 65, 67, 65, 64, 62, 60
]

for note in notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=480))

mid.save('simple_melody.mid')
