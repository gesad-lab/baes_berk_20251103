# Run Summary

**Run ID**: 98d05b7f-4529-40db-b980-08a7dd16b584
**Framework**: chatdev
**Started**: 2025-10-29T04:09:13.232127Z
**Completed**: 2025-10-29T04:38:02.455542Z
**Duration**: 1729.22s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 217.68 |
| 2 | 2 | completed | 0/0 | 0 | 211.87 |
| 3 | 3 | completed | 0/0 | 0 | 237.52 |
| 4 | 4 | completed | 0/0 | 0 | 290.90 |
| 5 | 5 | completed | 0/0 | 0 | 365.13 |
| 6 | 6 | completed | 0/0 | 0 | 406.12 |

## Directory Structure

```
98d05b7f-4529-40db-b980-08a7dd16b584/
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
