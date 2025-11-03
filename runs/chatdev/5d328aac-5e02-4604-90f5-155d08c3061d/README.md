# Run Summary

**Run ID**: 5d328aac-5e02-4604-90f5-155d08c3061d
**Framework**: chatdev
**Started**: 2025-10-29T16:12:47.723626Z
**Completed**: 2025-10-29T16:29:44.519138Z
**Duration**: 1016.80s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 177.35 |
| 2 | 2 | completed | 0/0 | 0 | 133.69 |
| 3 | 3 | completed | 0/0 | 0 | 143.59 |
| 4 | 4 | completed | 0/0 | 0 | 172.79 |
| 5 | 5 | completed | 0/0 | 0 | 185.02 |
| 6 | 6 | completed | 0/0 | 0 | 204.35 |

## Directory Structure

```
5d328aac-5e02-4604-90f5-155d08c3061d/
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
