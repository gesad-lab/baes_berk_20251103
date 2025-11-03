# Run Summary

**Run ID**: dcb08c31-167b-4262-94f3-d9a33afeafbf
**Framework**: ghspec
**Started**: 2025-10-30T18:11:04.487986Z
**Completed**: 2025-10-30T18:30:51.441380Z
**Duration**: 1186.95s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 173.41 |
| 2 | 2 | completed | 0/0 | 0 | 146.12 |
| 3 | 3 | completed | 0/0 | 0 | 153.66 |
| 4 | 4 | completed | 0/0 | 0 | 248.23 |
| 5 | 5 | completed | 0/0 | 0 | 229.85 |
| 6 | 6 | completed | 0/0 | 0 | 235.67 |

## Directory Structure

```
dcb08c31-167b-4262-94f3-d9a33afeafbf/
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
