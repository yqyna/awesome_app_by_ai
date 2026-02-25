#!/usr/bin/env python3
"""Django-style management entrypoint for local development."""

import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
