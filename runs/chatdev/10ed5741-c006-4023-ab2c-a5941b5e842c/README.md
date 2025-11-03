# Run Summary

**Run ID**: 10ed5741-c006-4023-ab2c-a5941b5e842c
**Framework**: chatdev
**Started**: 2025-10-28T23:05:38.386550Z
**Completed**: 2025-10-28T23:25:45.548936Z
**Duration**: 1207.16s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 165.55 |
| 2 | 2 | completed | 0/0 | 0 | 263.89 |
| 3 | 3 | completed | 0/0 | 0 | 197.66 |
| 4 | 4 | completed | 0/0 | 0 | 172.60 |
| 5 | 5 | completed | 0/0 | 0 | 206.08 |
| 6 | 6 | completed | 0/0 | 0 | 201.39 |

## Directory Structure

```
10ed5741-c006-4023-ab2c-a5941b5e842c/
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
