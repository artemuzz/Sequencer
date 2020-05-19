notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
noteMidiMappings = {}

for e1, v in enumerate(range(-2, 9)):
    for e2, k in enumerate(range(12)):
        iteration = (e1 * 12) + e2
        if iteration > 128:
            break
        else:
            note = notes[k] + ' ' + str(v)
            noteMidiMappings[iteration] = note


me.parent().store('noteMidiMappings', noteMidiMappings)
print(noteMidiMappings)