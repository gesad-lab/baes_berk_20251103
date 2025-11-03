# Run Summary

**Run ID**: 209491e8-b9ba-45c1-bad9-41c35ef337f1
**Framework**: ghspec
**Started**: 2025-10-30T00:25:50.083663Z
**Completed**: 2025-10-30T00:41:59.243927Z
**Duration**: 969.16s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 292.76 |
| 2 | 2 | completed | 0/0 | 0 | 103.63 |
| 3 | 3 | completed | 0/0 | 0 | 123.63 |
| 4 | 4 | completed | 0/0 | 0 | 119.07 |
| 5 | 5 | completed | 0/0 | 0 | 116.25 |
| 6 | 6 | completed | 0/0 | 0 | 213.80 |

## Directory Structure

```
209491e8-b9ba-45c1-bad9-41c35ef337f1/
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
