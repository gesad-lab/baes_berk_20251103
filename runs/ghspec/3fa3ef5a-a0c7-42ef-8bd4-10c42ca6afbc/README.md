# Run Summary

**Run ID**: 3fa3ef5a-a0c7-42ef-8bd4-10c42ca6afbc
**Framework**: ghspec
**Started**: 2025-10-31T19:16:40.042311Z
**Completed**: 2025-10-31T19:33:45.797553Z
**Duration**: 1025.76s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 161.21 |
| 2 | 2 | completed | 0/0 | 0 | 128.58 |
| 3 | 3 | completed | 0/0 | 0 | 196.70 |
| 4 | 4 | completed | 0/0 | 0 | 258.26 |
| 5 | 5 | completed | 0/0 | 0 | 101.94 |
| 6 | 6 | completed | 0/0 | 0 | 179.05 |

## Directory Structure

```
3fa3ef5a-a0c7-42ef-8bd4-10c42ca6afbc/
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
