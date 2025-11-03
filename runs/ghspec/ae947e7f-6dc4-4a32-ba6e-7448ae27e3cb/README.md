# Run Summary

**Run ID**: ae947e7f-6dc4-4a32-ba6e-7448ae27e3cb
**Framework**: ghspec
**Started**: 2025-10-29T04:38:04.128041Z
**Completed**: 2025-10-29T04:55:59.018330Z
**Duration**: 1074.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 236.01 |
| 2 | 2 | completed | 0/0 | 0 | 139.05 |
| 3 | 3 | completed | 0/0 | 0 | 153.73 |
| 4 | 4 | completed | 0/0 | 0 | 156.13 |
| 5 | 5 | completed | 0/0 | 0 | 219.67 |
| 6 | 6 | completed | 0/0 | 0 | 170.28 |

## Directory Structure

```
ae947e7f-6dc4-4a32-ba6e-7448ae27e3cb/
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
