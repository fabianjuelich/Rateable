from mutagen.easyid3 import EasyID3

class ID3:

    def __init__(self):
        EasyID3.RegisterTextKey('comment', 'COMM')
        # print(EasyID3.valid_keys.keys())

    def read(self, audiofile, tag_names):
        if type(tag_names) != list:
            tag_names = [tag_names]
        file = EasyID3(audiofile)
        tag_values = []
        for tag in tag_names:
            if tag in file:
                tag_values.append(file[tag][0])
            else:
                tag_values.append(None)
        return tag_values
