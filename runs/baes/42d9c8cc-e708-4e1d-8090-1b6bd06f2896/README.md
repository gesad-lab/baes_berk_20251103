# Run Summary

**Run ID**: 42d9c8cc-e708-4e1d-8090-1b6bd06f2896
**Framework**: baes
**Started**: 2025-10-29T01:35:07.858045Z
**Completed**: 2025-10-29T01:37:49.636764Z
**Duration**: 161.78s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 30.03 |
| 2 | 2 | completed | 0/0 | 0 | 23.72 |
| 3 | 3 | completed | 0/0 | 0 | 29.79 |
| 4 | 4 | completed | 0/0 | 0 | 25.99 |
| 5 | 5 | completed | 0/0 | 0 | 26.07 |
| 6 | 6 | completed | 0/0 | 0 | 26.17 |

## Directory Structure

```
42d9c8cc-e708-4e1d-8090-1b6bd06f2896/
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
