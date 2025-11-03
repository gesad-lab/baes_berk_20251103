# Run Summary

**Run ID**: db7774a9-a8d9-4f16-ae75-7e17f62b201f
**Framework**: ghspec
**Started**: 2025-10-31T01:12:27.404027Z
**Completed**: 2025-10-31T01:34:51.485671Z
**Duration**: 1344.08s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 270.34 |
| 2 | 2 | completed | 0/0 | 0 | 131.61 |
| 3 | 3 | completed | 0/0 | 0 | 149.09 |
| 4 | 4 | completed | 0/0 | 0 | 416.73 |
| 5 | 5 | completed | 0/0 | 0 | 148.35 |
| 6 | 6 | completed | 0/0 | 0 | 227.95 |

## Directory Structure

```
db7774a9-a8d9-4f16-ae75-7e17f62b201f/
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
