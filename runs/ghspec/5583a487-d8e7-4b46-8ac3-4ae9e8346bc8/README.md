# Run Summary

**Run ID**: 5583a487-d8e7-4b46-8ac3-4ae9e8346bc8
**Framework**: ghspec
**Started**: 2025-10-29T11:35:12.396462Z
**Completed**: 2025-10-29T11:55:00.485160Z
**Duration**: 1188.09s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 267.81 |
| 2 | 2 | completed | 0/0 | 0 | 170.43 |
| 3 | 3 | completed | 0/0 | 0 | 153.21 |
| 4 | 4 | completed | 0/0 | 0 | 246.69 |
| 5 | 5 | completed | 0/0 | 0 | 158.79 |
| 6 | 6 | completed | 0/0 | 0 | 191.16 |

## Directory Structure

```
5583a487-d8e7-4b46-8ac3-4ae9e8346bc8/
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
