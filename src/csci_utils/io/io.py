import os
from contextlib import contextmanager

from atomicwrites import AtomicWriter
from atomicwrites import atomic_write as _backend_writer


# You probably need to inspect and override some internals of the package
class SuffixWriter(AtomicWriter):
    def get_fileobject(self, dir=None, **kwargs):
        # Override functions like this

        # check if file exist
        if os.path.isfile(self._path):
            raise FileExistsError
        file_path, file_name = os.path.split(self._path)
        file_name, file_extension = os.path.splitext(file_name)

        # use NamedTemporaryFile to create random temp file with same directory and suffix
        return open(file_name, self._mode)


@contextmanager
def atomic_write(file, mode="w", as_file=True, new_default="asdf", **kwargs):

    # You can override things just fine...

    # get file info: name, extensions, directory

    with _backend_writer(file, writer_cls=SuffixWriter, **kwargs) as f:
        # Don't forget to handle the as_file logic!

        if as_file:
            yield f
        else:
            yield f.name
