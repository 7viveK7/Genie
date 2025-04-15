
---

### 🟩 `run.sh` (for quick dev run)

```bash
#!/bin/bash
echo "✅ Starting FastAPI Server on http://127.0.0.1:8000 ..."
uvicorn app.main:app --reload
