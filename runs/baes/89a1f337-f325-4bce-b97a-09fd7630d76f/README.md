# Run Summary

**Run ID**: 89a1f337-f325-4bce-b97a-09fd7630d76f
**Framework**: baes
**Started**: 2025-10-28T20:46:34.550818Z
**Completed**: 2025-10-28T20:50:00.196338Z
**Duration**: 205.65s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 20.10 |
| 2 | 2 | completed | 0/0 | 0 | 64.80 |
| 3 | 3 | completed | 0/0 | 0 | 32.00 |
| 4 | 4 | completed | 0/0 | 0 | 22.05 |
| 5 | 5 | completed | 0/0 | 0 | 31.47 |
| 6 | 6 | completed | 0/0 | 0 | 35.21 |

## Directory Structure

```
89a1f337-f325-4bce-b97a-09fd7630d76f/
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
