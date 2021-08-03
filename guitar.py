from fretboardgtr import ScaleGtr
global notes
notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
strings = ["E","A","D","G","B","E"]
note_dict = dict(enumerate(notes))
note_dict= dict((v, k) for k, v in note_dict.items())

def sharpen(note):
    for i in range(len(notes)):
        if note == notes[i]:
            return notes[i+1]

def flatten(note):
    for i in range(len(notes)):
        if note == notes[i]:
            return notes[i-1]

def major(note):
    def major_scale(note):
        notess = notes*3
        scale = notess[note_dict[note]:note_dict[note]+13]

        def filter(scale):
            mj_filter = [0,2,4,5,7,9,11,12]
            f_scale=[]
            for i in mj_filter:
                f_scale.append(scale[i])
            return f_scale
        return filter(scale)



    def store_major_scales():
        major_scales = {}
        for note in notes:
            major_scales[note] = major_scale(note)
        return major_scales

    print(note, "major scale -->", major_scale(note))
    global scale
    scale = major_scale(note)



    def maj_triads(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 4]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale
            major_triads[key] = filter(scale)
        return major_triads[note]

    def maj7_triads(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 4,6]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale
            major_triads[key] = filter(scale)

        return major_triads[note]

    def sevenths(note):
        x = flatten(maj7_triads(note)[3])
        sev_triads = maj7_triads(note)
        sev_triads[3] = x
        return sev_triads

    def minor_scale(note):
        notess = notes * 3
        scale = notess[note_dict[note]:note_dict[note] + 13]

        def filter(scale):
            mj_filter = [0, 2, 3, 5, 7, 8, 10, 12]
            f_scale = []
            for i in mj_filter:
                f_scale.append(scale[i])
            return f_scale

        return filter(scale)

    def store_minor_scales():
        minor_scales = {}
        for note in notes:
            minor_scales[note] = minor_scale(note)
        return minor_scales

    def min_triads(note):
        minor_triads = {}
        for key, val in store_minor_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 4]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale

            minor_triads[key] = filter(scale)
        return minor_triads[note]

    def diminished(note):
        dim_note = note
        dim_scale = major_scale(dim_note)

        def mfilter(scale):
            mj_filter = [0, 2, 4]
            f_scale = []
            for i in mj_filter:
                f_scale.append(scale[i])
            return f_scale
        triad = mfilter(dim_scale)
        triad[1] = flatten(triad[1])
        triad[2] = flatten(triad[2])

        return triad



    def sus2(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 1, 4]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale

            major_triads[key] = filter(scale)
        return major_triads[note]

    def sus4(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 5]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale

            major_triads[key] = filter(scale)
        return major_triads[note]


    def chords(note):
        scale = major_scale(note)
        scale.pop(7)
        x = dict(enumerate(scale))

        global scale_triads
        scale_triads = []
        for i in x.keys():
            if i == 0 or i == 3 or i == 4:
                print(x[i], "major", ":", maj_triads(x[i]))
                scale_triads.append(maj_triads(x[i]))
            elif i == 6:
                print(x[i], "diminished", diminished(x[i]))
                scale_triads.append(diminished(x[i]))
            else:
                print(x[i], "minor", ":", min_triads(x[i]))
                scale_triads.append(min_triads(x[i]))
        c = input("Need suspended chord triads?(y/n)").lower()
        if c == "y":
            for y in x.values():
                print(y,"sus2 : ", sus2(y))
                print(y, "sus4 : ", sus4(y))
        d = input("What about sevenths?(y/n)").lower()
        if d =="y":
            for y in x.values():
                print(y, "major7 : ", maj7_triads(y))
                print(y, "7 : ", sevenths(y))

    chords(note)


print(major("C"))
F = ScaleGtr(scale = scale,root="C")
F.customtuning(['E','A','D','G','B','E'])
F.theme(show_note_name=True)
F.set_color(root='red')
F.set_color(minorsecond='rgb(231, 0, 0)')
F.draw()
F.save(extension='JPEG')
print(" = = = = = = = = = = = = = ")


def minor(note):
    def major_scale(note):
        notess = notes*3
        scale = notess[note_dict[note]:note_dict[note]+13]

        def filter(scale):
            mj_filter = [0,2,4,5,7,9,11,12]
            f_scale=[]
            for i in mj_filter:
                f_scale.append(scale[i])
            return f_scale
        return filter(scale)


    def store_major_scales():
        major_scales = {}
        for note in notes:
            major_scales[note] = major_scale(note)
        return major_scales


    def maj_triads(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 4]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale
            major_triads[key] = filter(scale)
        return major_triads[note]


    def minor_scale(note):
        notess = notes * 3
        scale = notess[note_dict[note]:note_dict[note] + 13]

        def filter(scale):
            mj_filter = [0, 2, 3, 5, 7, 8, 10, 12]
            f_scale = []
            for i in mj_filter:
                f_scale.append(scale[i])
            return f_scale

        return filter(scale)

    print(note, "minor scale -->" ,minor_scale(note))

    def store_minor_scales():
        minor_scales = {}
        for note in notes:
            minor_scales[note] = minor_scale(note)
        return minor_scales

    def min_triads(note):
        minor_triads = {}
        for key, val in store_minor_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 4]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale

            minor_triads[key] = filter(scale)
        return minor_triads[note]

    def diminished(note):
        dim_note = note
        dim_scale = major_scale(dim_note)

        def mfilter(scale):
            mj_filter = [0, 2, 4]
            f_scale = []
            for i in mj_filter:
                f_scale.append(scale[i])
            return f_scale
        triad = mfilter(dim_scale)
        triad[1] = flatten(triad[1])
        triad[2] = flatten(triad[2])

        return triad

    def sus2(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 1, 4]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale

            major_triads[key] = filter(scale)
        return major_triads[note]

    def sus4(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 5]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale

            major_triads[key] = filter(scale)
        return major_triads[note]

    def maj7_triads(note):
        major_triads = {}
        for key, val in store_major_scales().items():
            scale = val

            def filter(scale):
                mj_filter = [0, 2, 4,6]
                f_scale = []
                for i in mj_filter:
                    f_scale.append(scale[i])
                return f_scale
            major_triads[key] = filter(scale)
        return major_triads[note]

    def sevenths(note):
        x = flatten(maj7_triads(note)[3])
        sev_triads = maj7_triads(note)
        sev_triads[3] = x
        return sev_triads

    def chords(note):
        scale = minor_scale(note)
        scale.pop(7)
        x = dict(enumerate(scale))
        for i in x.keys():
            if i == 0 or i == 1 or i== 3 or i == 4:
                print(x[i], "minor", ":", min_triads(x[i]))
            elif i == 6:
                print(x[i], "diminished", diminished(x[i]))
            else:
                print(x[i], "major", ":", maj_triads(x[i]))
        c = input("Need suspended chord triads?(y/n)").lower()
        if c == "y":
            for y in x.values():
                print(y, "sus2 : ", sus2(y))
                print(y, "sus4 : ", sus4(y))
        d = input("What about sevenths?(y/n)").lower()
        if d == "y":
            for y in x.values():
                print(y, "major7 : ", maj7_triads(y))
                print(y, "7 : ", sevenths(y))
    chords(note)

print(minor("C"))












