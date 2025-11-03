# Run Summary

**Run ID**: de6112b7-1f9d-452e-8aed-d11847f2e06f
**Framework**: chatdev
**Started**: 2025-10-28T11:21:00.149772Z
**Completed**: 2025-10-28T11:38:31.774925Z
**Duration**: 1051.63s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 147.60 |
| 2 | 2 | completed | 0/0 | 0 | 139.75 |
| 3 | 3 | completed | 0/0 | 0 | 150.83 |
| 4 | 4 | completed | 0/0 | 0 | 178.36 |
| 5 | 5 | completed | 0/0 | 0 | 215.19 |
| 6 | 6 | completed | 0/0 | 0 | 219.89 |

## Directory Structure

```
de6112b7-1f9d-452e-8aed-d11847f2e06f/
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
