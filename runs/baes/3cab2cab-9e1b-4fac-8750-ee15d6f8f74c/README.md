# Run Summary

**Run ID**: 3cab2cab-9e1b-4fac-8750-ee15d6f8f74c
**Framework**: baes
**Started**: 2025-10-30T00:42:00.505197Z
**Completed**: 2025-10-30T00:46:05.398732Z
**Duration**: 244.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 30.06 |
| 2 | 2 | completed | 0/0 | 0 | 54.45 |
| 3 | 3 | completed | 0/0 | 0 | 38.42 |
| 4 | 4 | completed | 0/0 | 0 | 34.69 |
| 5 | 5 | completed | 0/0 | 0 | 46.48 |
| 6 | 6 | completed | 0/0 | 0 | 40.79 |

## Directory Structure

```
3cab2cab-9e1b-4fac-8750-ee15d6f8f74c/
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
