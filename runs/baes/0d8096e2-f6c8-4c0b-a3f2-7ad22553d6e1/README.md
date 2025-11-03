# Run Summary

**Run ID**: 0d8096e2-f6c8-4c0b-a3f2-7ad22553d6e1
**Framework**: baes
**Started**: 2025-10-30T07:18:05.995288Z
**Completed**: 2025-10-30T07:22:03.803430Z
**Duration**: 237.81s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 38.81 |
| 2 | 2 | completed | 0/0 | 0 | 55.40 |
| 3 | 3 | completed | 0/0 | 0 | 30.42 |
| 4 | 4 | completed | 0/0 | 0 | 35.76 |
| 5 | 5 | completed | 0/0 | 0 | 42.30 |
| 6 | 6 | completed | 0/0 | 0 | 35.10 |

## Directory Structure

```
0d8096e2-f6c8-4c0b-a3f2-7ad22553d6e1/
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
