# Distroless image for Python app with UV

1. Use the debian slim package as base image so that everything is in venv.
1. Use `uv` to create a new venv with desired Python version and install 
dependencies in there.
1. Use the `base-debian` distroless image for the final image.
   * Using `python-debian` includes python 3.11 which I don't want.
   * The `base-debian` image doesn't have shell installed, which apparently 
   caused issues before (soemthing about `os.environ` needing access to shell?),
   but seems to be working now. If needed, shell and other primitive commands
   can be copied from the `busybox` image like
   `COPY --from=busybox:1.37.0-uclibc /bin/sh /bin/sh`.
1. Copy the app's contents, it's venv, and `uv`'s Python install which is
   located in `/root/.local/share/uv/python`.


# Build

```shell
docker build -t distroless-test:local .
docker run -it distroless-test:local
```

# Size comparisons

Moving contents to distroless saves about 100MB.
Once contents are moved to distroless, it is smaller than the starting debian
image.

* `gcr.io/distroless/base-debian12`: `31.2MB`
* `debian:bookworm-slim`: `97.2MB`
* `python:3.12-slim-bookworm`: `149MB`
* `distroless-test:local` (after moving contents to distroless): `86.4MB`
* `distroless-test:local` (before moving contents to distroless): `180MB`
