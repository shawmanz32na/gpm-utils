# gpm-utils

Google Play Music utilities to make your purchased music usable


- **DirectoryStructureNormalizer** - Converts the flat directory structure of your music files as downloaded from Google Play Music into a normalized directory structure of **[Artist]/[Album]/[Track].mp3**.


## Development

You can use a Docker container as your development and runtime environment:

Run unit tests with `docker run -it --rm -v ${PWD}:/usr/src/gpm-utils -w /usr/sr
c/gpm-utils python:latest python DirectoryStructureNormalizerTests.py`


## Usage (yes, this is painful at the moment)

Build the Docker image defined in the **docker** directory:

`docker build -t gpm-utils ./docker/Dockerfile`

Launch the docker image with the gpm-utils and your music mounted as a directory:

`docker run -it --rm -v ${PWD}:/usr/src/gpm-utils -v /path/to/your/music:/tmp/music -w /usr/src/gpm-utils gpm-utils python`

Execute the DirectoryStructureNormalizer (that's the only working feature so far :( ))

```
import DirectoryStructureNormalizer
dsn = DirectoryStructureNormalizer.DirectoryStructureNormalizer('/tmp/music')
dsn.normalizeDirectoryStructure()
```


## Features to come later

- A command line interface (CLI)
- Escape illegal characters (like '/' and '\') when creating directories
- Use the album artist before falling back on the track artist when creating directories
- Automatically populate ID3 tags based on the filename for files without existing ID3 tags
- Copy files instead of moving them
