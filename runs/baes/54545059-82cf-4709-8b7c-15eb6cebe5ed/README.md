# Run Summary

**Run ID**: 54545059-82cf-4709-8b7c-15eb6cebe5ed
**Framework**: baes
**Started**: 2025-10-30T23:28:13.963737Z
**Completed**: 2025-10-30T23:31:49.855114Z
**Duration**: 215.89s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 28.51 |
| 2 | 2 | completed | 0/0 | 0 | 44.21 |
| 3 | 3 | completed | 0/0 | 0 | 32.64 |
| 4 | 4 | completed | 0/0 | 0 | 38.37 |
| 5 | 5 | completed | 0/0 | 0 | 38.60 |
| 6 | 6 | completed | 0/0 | 0 | 33.55 |

## Directory Structure

```
54545059-82cf-4709-8b7c-15eb6cebe5ed/
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
