# Run Summary

**Run ID**: 53293593-2569-48d5-8dd6-f90855390722
**Framework**: chatdev
**Started**: 2025-10-30T10:09:00.886893Z
**Completed**: 2025-10-30T10:26:13.703516Z
**Duration**: 1032.82s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 163.73 |
| 2 | 2 | completed | 0/0 | 0 | 193.82 |
| 3 | 3 | completed | 0/0 | 0 | 178.11 |
| 4 | 4 | completed | 0/0 | 0 | 162.78 |
| 5 | 5 | completed | 0/0 | 0 | 162.60 |
| 6 | 6 | completed | 0/0 | 0 | 171.77 |

## Directory Structure

```
53293593-2569-48d5-8dd6-f90855390722/
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
