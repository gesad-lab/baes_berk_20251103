# Run Summary

**Run ID**: 3c5a3770-c1ef-4448-a517-6ef1c9394ed7
**Framework**: baes
**Started**: 2025-10-28T10:18:08.523777Z
**Completed**: 2025-10-28T10:21:52.823738Z
**Duration**: 224.30s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 24.05 |
| 2 | 2 | completed | 0/0 | 0 | 52.46 |
| 3 | 3 | completed | 0/0 | 0 | 33.25 |
| 4 | 4 | completed | 0/0 | 0 | 45.54 |
| 5 | 5 | completed | 0/0 | 0 | 34.70 |
| 6 | 6 | completed | 0/0 | 0 | 34.27 |

## Directory Structure

```
3c5a3770-c1ef-4448-a517-6ef1c9394ed7/
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
