# Run Summary

**Run ID**: 55242f62-5fb5-4b5b-9340-46ad281e0406
**Framework**: chatdev
**Started**: 2025-10-30T17:55:19.023131Z
**Completed**: 2025-10-30T18:11:00.539221Z
**Duration**: 941.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 160.75 |
| 2 | 2 | completed | 0/0 | 0 | 128.32 |
| 3 | 3 | completed | 0/0 | 0 | 125.22 |
| 4 | 4 | completed | 0/0 | 0 | 195.50 |
| 5 | 5 | completed | 0/0 | 0 | 148.51 |
| 6 | 6 | completed | 0/0 | 0 | 183.21 |

## Directory Structure

```
55242f62-5fb5-4b5b-9340-46ad281e0406/
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
