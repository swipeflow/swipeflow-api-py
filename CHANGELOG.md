# Changelog

All notable changes to the SwipeFlow Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.6] - 2026-09-21

### Added
- Initial release of the SwipeFlow Python SDK, generated from the public SwipeFlow OpenAPI spec (https://api.swipeflow.io/v1/openapi.json) with openapi-python-client: sync and async endpoint functions and typed models under `swipeflow.api` and `swipeflow.models`.
- `SwipeFlowClient`, a thin wrapper that authenticates with an API key (`X-API-Key`, or the `SWIPEFLOW_API_KEY` environment variable) or a bearer token, sets a 30s default timeout, and raises `SwipeFlowError` on HTTP errors.
- `scripts/generate.py` to download the spec and regenerate the client.
- Offline tests and an opt-in live smoke test.
- Requires Python 3.11+; depends on `httpx` and `attrs`.
