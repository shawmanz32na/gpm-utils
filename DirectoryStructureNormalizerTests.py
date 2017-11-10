import unittest

import pathlib

from DirectoryStructureNormalizer import DirectoryStructureNormalizer


class DirectoryStructureNormalizerTests(unittest.TestCase):

    def testInitShouldCreateDirectoryStructureNormalizer(self):
        directoryStructureNormalizer = DirectoryStructureNormalizer()
        self.assertIsInstance(directoryStructureNormalizer, DirectoryStructureNormalizer)

    def testSetterShouldSetPathToPathlibPath(self):
        directoryStructureNormalizer = DirectoryStructureNormalizer('.')
        self.assertIsInstance(directoryStructureNormalizer.path, Path)

    def testNormalizeDirectoryStructureShouldRaiseError(self):
        directoryStructureNormalizer = DirectoryStructureNormalizer('.')
        # TODO: Actually verify something?

    def testNormalizeDirectoryStructureShouldRaiseErrorAndExitIfPathNotProvided(self):
        directoryStructureNormalizer = DirectoryStructureNormalizer()
        self.assertRaises(IOError, directoryStructureNormalizer.normalizeDirectoryStructure)

    # def testNormalizeDirectoryStructureShouldRaiseErrorAndExitIfPathIsNotADirectory

    # def testNormalizeDirectoryStructureShouldUseAlbumArtistToCreateNormalizedDirectoryPath(self):
    # def testNormalizeDirectoryStructureShouldConvertSlashesToUnderscoresWhenUsingAlbumArtistToCreateNormalizedDirectoryPath(self):
    # def testNormalizeDirectoryStructureShouldFallBackOnArtistIfNoAlbumArtistSpecifiedToCreateNormalizedDirectoryPath(self):
    # def testNormalizeDirectoryStructureShouldConvertSlashesToUnderscoresWhenUsingArtistToCreateNormalizedDirectoryPath(self):
    # def testNormalizeDirectoryStructureShouldConvertSlashesToUnderscoresWhenUsingAlbumToCreateNormalizedDirectoryPath(self):

def main():
        unittest.main()

if __name__ == '__main__':
    main()
