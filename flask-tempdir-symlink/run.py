import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory

from my_app import wsgi


target_dir = Path('my_app/artifacts')


with TemporaryDirectory() as tmp_dir:
    cwd = Path().absolute()
    target_dir = cwd / target_dir
    print(cwd)
    print(target_dir)
    print('---')
    print(tmp_dir)

    data = {
        'hello': 'world'
    }
    f = Path(tmp_dir) / 'test.json'
    f.write_text(json.dumps(data, indent=2))

    os.symlink(tmp_dir, target_dir / 'foo', target_is_directory=True)

    wsgi.app.run()

    os.unlink(target_dir / 'foo')
