FROM python:3.13-slim-trixie

LABEL maintainer="@jay_townsend1 & @NotoriousRebel1"

# Add our src and install
COPY . /src
RUN python3 -m pip install --no-cache-dir /src

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/restfulHarvest"]
CMD ["-H", "0.0.0.0", "-p", "80"]
