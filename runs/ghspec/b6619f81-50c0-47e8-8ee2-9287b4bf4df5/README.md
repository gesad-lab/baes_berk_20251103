# Run Summary

**Run ID**: b6619f81-50c0-47e8-8ee2-9287b4bf4df5
**Framework**: ghspec
**Started**: 2025-10-28T12:30:56.781221Z
**Completed**: 2025-10-28T12:54:46.710782Z
**Duration**: 1429.93s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 299.71 |
| 2 | 2 | completed | 0/0 | 0 | 223.19 |
| 3 | 3 | completed | 0/0 | 0 | 173.49 |
| 4 | 4 | completed | 0/0 | 0 | 338.98 |
| 5 | 5 | completed | 0/0 | 0 | 227.08 |
| 6 | 6 | completed | 0/0 | 0 | 167.47 |

## Directory Structure

```
b6619f81-50c0-47e8-8ee2-9287b4bf4df5/
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
