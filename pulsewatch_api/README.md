# Health Check Endpoints

PulseWatch provides two health check endpoints for monitoring system status:

## Endpoints

### Liveness Probe
```http
GET /live

Response:
{
    "live": true
}

uvicorn app.main:app --reload

# Test liveness
curl http://localhost:8000/live

# Test readiness
curl http://localhost:8000/ready