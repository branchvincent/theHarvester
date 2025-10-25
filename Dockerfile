FROM python:3.13-slim-trixie

LABEL maintainer="@jay_townsend1 & @NotoriousRebel1"

# Add our src and install
COPY . /src
RUN python3 -m pip install --no-cache-dir /src
# COPY --from=astral/uv:latest /uv /uvx /bin/
# RUN uv tool install /src

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/restfulHarvest"]
CMD ["-H", "0.0.0.0", "-p", "80"]
