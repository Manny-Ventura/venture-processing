# Venture Processing | A Factory Workflow Simulator

A small backend/platform project that digitizes a simple factory inspection workflow for fun.

Operators submit machine inspection data through an API. The system stores the inspection in Postgres, creates a background processing job, and later processes the inspection asynchronously through a worker.

This project is intentionally small. The goal is not to build a polished SaaS app, but to practice backend architecture, queues, persistence, service boundaries, Docker, debugging, and production-oriented engineering decisions.

## What this project demonstrates

- API design with FastAPI
- Structured data modeling with Postgres
- Background processing with Celery
- Redis as a message broker
- Local multi-service development with Docker Compose
- Job status tracking
- Failure handling and debugging workflows
- Documentation for architecture, operations, and interview articulation

## Problem

A factory currently tracks machine inspections on paper. Operators fill out inspection data manually, and supervisors review the results later.

This system digitizes a narrow slice of that workflow:

1. An operator submits an inspection.
2. The inspection is stored durably.
3. A processing job is created.
4. A background worker evaluates the inspection.
5. A supervisor or client can check the job status and result.

## Initial workflow

```text
Operator
  -> FastAPI API
  -> Postgres stores inspection
  -> Postgres stores processing job
  -> Celery task is queued through Redis
  -> Worker processes inspection
  -> Worker updates job status/result
  -> API exposes inspection and job status

## Current status

The API currently shows a health endpoint.

```http
GET /health