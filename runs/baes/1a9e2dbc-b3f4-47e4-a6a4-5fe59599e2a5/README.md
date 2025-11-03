# Run Summary

**Run ID**: 1a9e2dbc-b3f4-47e4-a6a4-5fe59599e2a5
**Framework**: baes
**Started**: 2025-10-28T13:51:27.419008Z
**Completed**: 2025-10-28T13:55:01.022834Z
**Duration**: 213.60s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.68 |
| 2 | 2 | completed | 0/0 | 0 | 31.50 |
| 3 | 3 | completed | 0/0 | 0 | 40.19 |
| 4 | 4 | completed | 0/0 | 0 | 32.76 |
| 5 | 5 | completed | 0/0 | 0 | 36.59 |
| 6 | 6 | completed | 0/0 | 0 | 38.88 |

## Directory Structure

```
1a9e2dbc-b3f4-47e4-a6a4-5fe59599e2a5/
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
