A quick demo on inheriting a venv from a base image that uses poetry.
It relies on the `VIRTUAL_ENV` and the `PATH` env vars to be set in the base
image (this is what activating a venv does behind the scenes. Check out
https://pythonspeed.com/articles/activate-virtualenv-dockerfile/ for more).

If venv is unknown, use `poetry env info --path` to get the path.


<!-- Using ruby syntax highlighting because it looks the prettiest -->
```ruby
> bash run.sh
[+] Building 0.2s (11/11) FINISHED
...
 => => naming to docker.io/library/local:base

environ({'PATH': '/usr/src/my_venv/bin:/usr/src/my_venv/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'HOSTNAME': '7377f8b646d5', 'LANG': 'C.UTF-8', 'GPG_KEY': '7169605F62C751356D054A26A821E680E5FA6305', 'PYTHON_VERSION': '3.12.5', 'PYTHON_PIP_VERSION': '24.2', 'PYTHON_GET_PIP_URL': 'https://github.com/pypa/get-pip/raw/66d8a0f637083e2c3ddffc0cb1e65ce126afb856/public/get-pip.py', 'PYTHON_GET_PIP_SHA256': '6fb7b781206356f45ad79efbb19322caa6c2a5ad39092d0d44d0fec94117e118', 'VIRTUAL_ENV': '/usr/src/my_venv', 'HOME': '/root'})

[+] Building 0.0s (10/10) FINISHED
...
 => => naming to docker.io/library/local:override

(resolved python: /usr/src/my_venv/bin/python)
Flask==3.0.3
├── blinker [required: >=1.6.2, installed: 1.8.2]
├── click [required: >=8.1.3, installed: 8.1.7]
├── itsdangerous [required: >=2.1.2, installed: 2.2.0]
├── Jinja2 [required: >=3.1.2, installed: 3.1.4]
│   └── MarkupSafe [required: >=2.0, installed: 2.1.5]
└── Werkzeug [required: >=3.0.0, installed: 3.0.4]
    └── MarkupSafe [required: >=2.1.1, installed: 2.1.5]
gunicorn==23.0.0
└── packaging [required: Any, installed: 24.1]
pipdeptree==2.23.1
├── packaging [required: >=23.1, installed: 24.1]
└── pip [required: >=23.1.2, installed: 24.2]
```