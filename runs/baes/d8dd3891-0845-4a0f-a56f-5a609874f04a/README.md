# Run Summary

**Run ID**: d8dd3891-0845-4a0f-a56f-5a609874f04a
**Framework**: baes
**Started**: 2025-10-29T11:55:02.825977Z
**Completed**: 2025-10-29T11:58:57.659656Z
**Duration**: 234.83s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 40.24 |
| 2 | 2 | completed | 0/0 | 0 | 36.91 |
| 3 | 3 | completed | 0/0 | 0 | 36.43 |
| 4 | 4 | completed | 0/0 | 0 | 47.78 |
| 5 | 5 | completed | 0/0 | 0 | 33.50 |
| 6 | 6 | completed | 0/0 | 0 | 39.97 |

## Directory Structure

```
d8dd3891-0845-4a0f-a56f-5a609874f04a/
├── sprint_001/          # First sprint artifacts
│   ├── generated_artifacts/
│   ├── logs/
│   ├── metadata.json
│   └── validation.json
├── sprint_002/          # Second sprint artifacts
│   └── ...
├── final/               # Symlink to last successful sprint
└── metrics.json         # Run-level metrics (single source of truth)
```

## Accessing Results

### View final artifacts
```bash
cd final/generated_artifacts/managed_system/
```

### Compare sprints
```bash
diff -r sprint_001/generated_artifacts sprint_002/generated_artifacts
```

### View metrics (single source of truth)
```bash
cat metrics.json | jq
```

### Check specific sprint
```bash
cat sprint_001/metadata.json
```
