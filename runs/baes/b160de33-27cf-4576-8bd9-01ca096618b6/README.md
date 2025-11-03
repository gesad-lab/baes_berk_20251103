# Run Summary

**Run ID**: b160de33-27cf-4576-8bd9-01ca096618b6
**Framework**: baes
**Started**: 2025-10-30T10:05:15.746278Z
**Completed**: 2025-10-30T10:09:00.207309Z
**Duration**: 224.46s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 36.47 |
| 2 | 2 | completed | 0/0 | 0 | 37.42 |
| 3 | 3 | completed | 0/0 | 0 | 29.19 |
| 4 | 4 | completed | 0/0 | 0 | 34.54 |
| 5 | 5 | completed | 0/0 | 0 | 33.53 |
| 6 | 6 | completed | 0/0 | 0 | 53.30 |

## Directory Structure

```
b160de33-27cf-4576-8bd9-01ca096618b6/
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
