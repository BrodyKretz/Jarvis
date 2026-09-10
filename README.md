# Jarvis

Centralized information layer for emergency response.

## Problem

First responders work off disjointed information architecture. The data that
matters during an incident — population density, department locations, traffic,
geospatial layers — exists, but it's split across agencies (fire, EMS, public
health) with no shared way to consolidate it or coordinate between them. Cities
end up underprepared, especially for natural disasters where the risk is
deferred and therefore under-funded.

## Goal

Pull existing public data sources into one place and make them queryable for
incident response and preparedness planning.

## Status

Scaffold only.

## Setup

```bash
conda activate py312
pip install -e ".[dev]"
cp .env.example .env
```

## Layout

```
src/jarvis/      package code
  config.py      env-backed settings
  ingest.py      data source loaders
  cli.py         entry point
tests/           pytest
data/raw/        source data (gitignored)
data/processed/  derived data (gitignored)
```
