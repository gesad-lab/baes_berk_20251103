# Run Summary

**Run ID**: fab9a0a2-9ceb-4ab4-bf28-adce3d9e7333
**Framework**: chatdev
**Started**: 2025-10-30T10:51:27.108129Z
**Completed**: 2025-10-30T11:09:58.937147Z
**Duration**: 1111.83s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 141.61 |
| 2 | 2 | completed | 0/0 | 0 | 123.85 |
| 3 | 3 | completed | 0/0 | 0 | 155.58 |
| 4 | 4 | completed | 0/0 | 0 | 202.07 |
| 5 | 5 | completed | 0/0 | 0 | 220.80 |
| 6 | 6 | completed | 0/0 | 0 | 267.91 |

## Directory Structure

```
fab9a0a2-9ceb-4ab4-bf28-adce3d9e7333/
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
