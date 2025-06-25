# Bluetooth Testing Pipeline

This repository contains a minimal Jenkins based workflow for running Bluetooth
tests inside Docker containers.  Three different test suites are provided:
A2DP, HFP and connectivity/disconnect.  Each suite can run either in a mock mode
(using simulated devices) or against real hardware.

## Quick start

1. Build the test images and start Jenkins along with the test containers:

```bash
docker-compose up --build
```

2. Browse to `http://localhost:8080` and configure Jenkins.  The pipeline file
is located at `jenkins/pipelines/ble_pipline.groovy`.

3. Trigger the pipeline to build the images, execute unit tests via `pytest` and
finally run the integration tests.  Result logs are written to the `results/`
directory.

## Directory layout

- `a2dp_test/`, `hfp_test/`, `connect_disconnect_test/` – Individual test
  suites with Dockerfiles and test scripts.
- `android_os/` – Placeholder scripts for setting up an Android environment.
- `jenkins/` – Dockerfile for a Jenkins image and pipeline definition.
- `docker-compose.yml` – Brings all containers up for local testing.

The project serves as a starting point for further Bluetooth automation.  The
mock tests can be expanded with real device logic and the Android installation
script can be replaced with a full emulator setup as needed.
