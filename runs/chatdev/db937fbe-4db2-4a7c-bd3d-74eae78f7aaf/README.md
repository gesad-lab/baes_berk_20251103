# Run Summary

**Run ID**: db937fbe-4db2-4a7c-bd3d-74eae78f7aaf
**Framework**: chatdev
**Started**: 2025-10-31T12:55:03.904760Z
**Completed**: 2025-10-31T13:15:25.794013Z
**Duration**: 1221.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 229.00 |
| 2 | 2 | completed | 0/0 | 0 | 250.49 |
| 3 | 3 | completed | 0/0 | 0 | 164.18 |
| 4 | 4 | completed | 0/0 | 0 | 160.91 |
| 5 | 5 | completed | 0/0 | 0 | 168.43 |
| 6 | 6 | completed | 0/0 | 0 | 248.88 |

## Directory Structure

```
db937fbe-4db2-4a7c-bd3d-74eae78f7aaf/
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
