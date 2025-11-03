# Run Summary

**Run ID**: 09d8a3a8-2269-4483-a424-7f6507019236
**Framework**: baes
**Started**: 2025-10-28T12:54:47.241778Z
**Completed**: 2025-10-28T12:58:07.349240Z
**Duration**: 200.11s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 34.11 |
| 2 | 2 | completed | 0/0 | 0 | 31.45 |
| 3 | 3 | completed | 0/0 | 0 | 37.05 |
| 4 | 4 | completed | 0/0 | 0 | 22.84 |
| 5 | 5 | completed | 0/0 | 0 | 37.01 |
| 6 | 6 | completed | 0/0 | 0 | 37.64 |

## Directory Structure

```
09d8a3a8-2269-4483-a424-7f6507019236/
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
