# Run Summary

**Run ID**: 623f3c79-797c-4b7a-8518-2e84f2bee5c9
**Framework**: baes
**Started**: 2025-10-30T18:30:54.889562Z
**Completed**: 2025-10-30T18:33:55.700244Z
**Duration**: 180.81s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 27.66 |
| 2 | 2 | completed | 0/0 | 0 | 31.83 |
| 3 | 3 | completed | 0/0 | 0 | 31.29 |
| 4 | 4 | completed | 0/0 | 0 | 31.34 |
| 5 | 5 | completed | 0/0 | 0 | 27.90 |
| 6 | 6 | completed | 0/0 | 0 | 30.77 |

## Directory Structure

```
623f3c79-797c-4b7a-8518-2e84f2bee5c9/
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
