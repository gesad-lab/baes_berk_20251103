# Run Summary

**Run ID**: f8de9e75-e173-442d-bb34-0c250421cc4b
**Framework**: chatdev
**Started**: 2025-10-31T05:32:40.270151Z
**Completed**: 2025-10-31T05:38:05.198502Z
**Duration**: 324.93s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 321.45 |
| 2 | 2 | completed | 0/0 | 0 | 0.70 |
| 3 | 3 | completed | 0/0 | 0 | 0.70 |
| 4 | 4 | completed | 0/0 | 0 | 0.69 |
| 5 | 5 | completed | 0/0 | 0 | 0.70 |
| 6 | 6 | completed | 0/0 | 0 | 0.69 |

## Directory Structure

```
f8de9e75-e173-442d-bb34-0c250421cc4b/
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
