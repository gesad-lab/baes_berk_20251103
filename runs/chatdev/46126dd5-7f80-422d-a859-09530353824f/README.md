# Run Summary

**Run ID**: 46126dd5-7f80-422d-a859-09530353824f
**Framework**: chatdev
**Started**: 2025-10-30T14:24:12.968663Z
**Completed**: 2025-10-30T14:45:08.729110Z
**Duration**: 1255.76s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 201.74 |
| 2 | 2 | completed | 0/0 | 0 | 206.26 |
| 3 | 3 | completed | 0/0 | 0 | 176.50 |
| 4 | 4 | completed | 0/0 | 0 | 160.90 |
| 5 | 5 | completed | 0/0 | 0 | 280.08 |
| 6 | 6 | completed | 0/0 | 0 | 230.27 |

## Directory Structure

```
46126dd5-7f80-422d-a859-09530353824f/
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
