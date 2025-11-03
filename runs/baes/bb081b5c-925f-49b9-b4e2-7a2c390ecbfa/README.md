# Run Summary

**Run ID**: bb081b5c-925f-49b9-b4e2-7a2c390ecbfa
**Framework**: baes
**Started**: 2025-10-29T08:40:42.514074Z
**Completed**: 2025-10-29T08:44:23.016602Z
**Duration**: 220.50s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.11 |
| 2 | 2 | completed | 0/0 | 0 | 32.73 |
| 3 | 3 | completed | 0/0 | 0 | 36.56 |
| 4 | 4 | completed | 0/0 | 0 | 40.36 |
| 5 | 5 | completed | 0/0 | 0 | 35.85 |
| 6 | 6 | completed | 0/0 | 0 | 41.88 |

## Directory Structure

```
bb081b5c-925f-49b9-b4e2-7a2c390ecbfa/
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
