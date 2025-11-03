# Run Summary

**Run ID**: b3bca5fc-8564-4340-b283-a50b101e97ee
**Framework**: ghspec
**Started**: 2025-10-31T17:42:18.139263Z
**Completed**: 2025-10-31T17:58:22.676659Z
**Duration**: 964.54s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 155.18 |
| 2 | 2 | completed | 0/0 | 0 | 117.01 |
| 3 | 3 | completed | 0/0 | 0 | 149.95 |
| 4 | 4 | completed | 0/0 | 0 | 228.48 |
| 5 | 5 | completed | 0/0 | 0 | 159.55 |
| 6 | 6 | completed | 0/0 | 0 | 154.35 |

## Directory Structure

```
b3bca5fc-8564-4340-b283-a50b101e97ee/
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
