import os
from pathlib import Path
from typing import List, Union


from my_app import wsgi


PathLike = Union[str, os.PathLike]


class Linker:

    def __init__(self, dst_dir: PathLike, src_dir: PathLike):
        self._dst_dir = Path(dst_dir).resolve()
        self._src_dir = Path(src_dir).resolve()
        self._symlinks: List[Path] = []

    def link(self):
        for target in self._src_dir.iterdir():
            path = self._dst_dir / target.name
            print(f'source: {path}')
            print(f'target: {target}')
            path.symlink_to(target, target_is_directory=target.is_dir())
            self._symlinks.append(path)
            print('---')

    def unlink(self):
        for symlink in self._symlinks:
            symlink.unlink()

    def __enter__(self):
        self.link()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.unlink()


target_dir = Path('my_app/artifacts')
source_dir = 'data'

with Linker(target_dir, source_dir):
    wsgi.app.run()
