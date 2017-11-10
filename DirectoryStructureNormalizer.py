import eyed3
import pathlib

class DirectoryStructureNormalizer:

    def __init__(self, path=None):
        if path is not None:
            self.path = path
        else:
            self.__path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = pathlib.Path(path)

    def normalizeDirectoryStructure(self):
        # TODO: Can we break this sanity checking into its own method? How?
        if not isinstance(self.path, pathlib.Path):
            raise IOError("directory path to normalize not set")

        for mp3File in self.path.glob('*.mp3'):
            print('Processing ' + str(mp3File))
            audioFile = eyed3.load(mp3File)
            targetDirectory = self.path / audioFile.tag.artist / audioFile.tag.album
            targetDirectory.mkdir(parents=True, exist_ok=True)
            mp3File.rename(targetDirectory / mp3File.name)


# if __name__ == '__main__':
#     import sys
#     dsn = DirectoryStructureNormalizer(sys.argv[1])
#     dsn.normalizeDirectoryStructure()
