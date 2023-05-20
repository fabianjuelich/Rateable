import eyed3
from mutagen.easyid3 import EasyID3
import mutagen
from mutagen import id3
import music_tag

class ID3:
    
    def modify(self, files, rating, count):
        # writing
        for file in files:
            # # eyed3
            # audiofile = eyed3.load(file)#, tag_version=(2,3,0))
            # if audiofile:
            #     # print(audiofile.tag.version)
            #     # print(audiofile.tag.title)
            #     audiofile.tag.popularities.set('-', rating, 0)
            #     audiofile.tag.comments.set(count)
            #     print(audiofile.tag.comments[0].text)
            #     audiofile.tag.save(file)#, version=(2,3,0))
            # # mutagen 1
            # EasyID3.RegisterTextKey('rating', 'POPM')
            # audiofile = EasyID3(file)
            # print(audiofile)
            # audiofile.save(file, v1=2)
            # # mutagen 2
            # try:
            #     audiofile = EasyID3(file)
            # except mutagen.id3.ID3NoHeaderError:
            #     audiofile = mutagen.File(file, easy=True)
            #     audiofile.add_tags()
            # audiofile['title'] = "asdf"
            # audiofile.save(file, v1=2)
            # # mutagen 3
            # audiofile = id3.ID3(file)
            # audiofile.add(id3.COMM(encoding=3, lang='XXX', desc=u'', text=[u'Comment!']))
            # music-tag
            f = music_tag.load_file(file)
            f.remove_tag('title')
            f['comment'] = 'This is a comment'
