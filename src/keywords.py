import os

class Keywords():

    def get(self, path):

        keywords = {}

        def traverse(path):
            if os.path.isdir(path):
                elements = os.listdir(path)
                for elem in elements:
                    traverse(os.path.join(path, elem))
            else:
                keywords.update({os.path.basename(os.path.dirname(path)): {'path': os.path.normpath(os.path.dirname(path)).replace('\\', '/')}})

        traverse(path)
        return keywords
