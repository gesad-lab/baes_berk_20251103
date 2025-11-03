# Run Summary

**Run ID**: 101c4026-aca9-4269-aee8-a38a37faa0fd
**Framework**: chatdev
**Started**: 2025-10-29T01:06:36.970156Z
**Completed**: 2025-10-29T01:20:00.977348Z
**Duration**: 804.01s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 105.60 |
| 2 | 2 | completed | 0/0 | 0 | 114.41 |
| 3 | 3 | completed | 0/0 | 0 | 129.29 |
| 4 | 4 | completed | 0/0 | 0 | 163.28 |
| 5 | 5 | completed | 0/0 | 0 | 151.78 |
| 6 | 6 | completed | 0/0 | 0 | 139.64 |

## Directory Structure

```
101c4026-aca9-4269-aee8-a38a37faa0fd/
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
