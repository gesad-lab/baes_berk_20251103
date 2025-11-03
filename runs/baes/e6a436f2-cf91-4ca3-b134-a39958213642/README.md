# Run Summary

**Run ID**: e6a436f2-cf91-4ca3-b134-a39958213642
**Framework**: baes
**Started**: 2025-10-30T02:30:39.247023Z
**Completed**: 2025-10-30T02:33:52.358793Z
**Duration**: 193.11s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 39.49 |
| 2 | 2 | completed | 0/0 | 0 | 21.92 |
| 3 | 3 | completed | 0/0 | 0 | 31.10 |
| 4 | 4 | completed | 0/0 | 0 | 24.00 |
| 5 | 5 | completed | 0/0 | 0 | 37.74 |
| 6 | 6 | completed | 0/0 | 0 | 38.85 |

## Directory Structure

```
e6a436f2-cf91-4ca3-b134-a39958213642/
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
