# Run Summary

**Run ID**: 9ff4e871-ac06-4df2-bf50-9f8ac61929c6
**Framework**: baes
**Started**: 2025-10-30T14:20:37.827348Z
**Completed**: 2025-10-30T14:24:11.275065Z
**Duration**: 213.45s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 36.84 |
| 2 | 2 | completed | 0/0 | 0 | 32.84 |
| 3 | 3 | completed | 0/0 | 0 | 35.47 |
| 4 | 4 | completed | 0/0 | 0 | 37.62 |
| 5 | 5 | completed | 0/0 | 0 | 33.93 |
| 6 | 6 | completed | 0/0 | 0 | 36.75 |

## Directory Structure

```
9ff4e871-ac06-4df2-bf50-9f8ac61929c6/
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
