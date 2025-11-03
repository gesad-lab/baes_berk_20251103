# Run Summary

**Run ID**: a88ad569-1c53-4f73-abf6-b3b5488f8aff
**Framework**: chatdev
**Started**: 2025-10-30T12:56:20.867690Z
**Completed**: 2025-10-30T13:12:21.733468Z
**Duration**: 960.87s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 156.65 |
| 2 | 2 | completed | 0/0 | 0 | 135.77 |
| 3 | 3 | completed | 0/0 | 0 | 159.37 |
| 4 | 4 | completed | 0/0 | 0 | 153.32 |
| 5 | 5 | completed | 0/0 | 0 | 176.39 |
| 6 | 6 | completed | 0/0 | 0 | 179.37 |

## Directory Structure

```
a88ad569-1c53-4f73-abf6-b3b5488f8aff/
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
