# Run Summary

**Run ID**: 01335fc4-0951-423b-b2e1-90f637d0f53f
**Framework**: baes
**Started**: 2025-10-30T10:44:36.880409Z
**Completed**: 2025-10-30T10:51:26.344970Z
**Duration**: 409.46s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 44.99 |
| 2 | 2 | completed | 0/0 | 0 | 31.45 |
| 3 | 3 | completed | 0/0 | 0 | 34.96 |
| 4 | 4 | completed | 0/0 | 0 | 31.54 |
| 5 | 5 | completed | 0/0 | 0 | 32.59 |
| 6 | 6 | completed | 0/0 | 0 | 233.92 |

## Directory Structure

```
01335fc4-0951-423b-b2e1-90f637d0f53f/
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
