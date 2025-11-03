# Run Summary

**Run ID**: e620cd56-b254-4afe-9c91-b3d480cea3a8
**Framework**: baes
**Started**: 2025-10-31T00:47:46.516737Z
**Completed**: 2025-10-31T00:51:09.406764Z
**Duration**: 202.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.73 |
| 2 | 2 | completed | 0/0 | 0 | 35.45 |
| 3 | 3 | completed | 0/0 | 0 | 36.74 |
| 4 | 4 | completed | 0/0 | 0 | 34.29 |
| 5 | 5 | completed | 0/0 | 0 | 31.10 |
| 6 | 6 | completed | 0/0 | 0 | 31.58 |

## Directory Structure

```
e620cd56-b254-4afe-9c91-b3d480cea3a8/
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
