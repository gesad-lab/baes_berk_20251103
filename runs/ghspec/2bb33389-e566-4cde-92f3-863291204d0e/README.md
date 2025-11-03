# Run Summary

**Run ID**: 2bb33389-e566-4cde-92f3-863291204d0e
**Framework**: ghspec
**Started**: 2025-10-29T22:57:27.436936Z
**Completed**: 2025-10-29T23:18:06.816536Z
**Duration**: 1239.38s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 282.07 |
| 2 | 2 | completed | 0/0 | 0 | 140.43 |
| 3 | 3 | completed | 0/0 | 0 | 154.60 |
| 4 | 4 | completed | 0/0 | 0 | 153.22 |
| 5 | 5 | completed | 0/0 | 0 | 217.00 |
| 6 | 6 | completed | 0/0 | 0 | 292.05 |

## Directory Structure

```
2bb33389-e566-4cde-92f3-863291204d0e/
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
