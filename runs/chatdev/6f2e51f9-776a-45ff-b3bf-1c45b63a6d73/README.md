# Run Summary

**Run ID**: 6f2e51f9-776a-45ff-b3bf-1c45b63a6d73
**Framework**: chatdev
**Started**: 2025-10-31T18:57:09.600022Z
**Completed**: 2025-10-31T19:13:37.872496Z
**Duration**: 988.27s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 177.56 |
| 2 | 2 | completed | 0/0 | 0 | 185.88 |
| 3 | 3 | completed | 0/0 | 0 | 146.58 |
| 4 | 4 | completed | 0/0 | 0 | 164.38 |
| 5 | 5 | completed | 0/0 | 0 | 166.15 |
| 6 | 6 | completed | 0/0 | 0 | 147.72 |

## Directory Structure

```
6f2e51f9-776a-45ff-b3bf-1c45b63a6d73/
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
