# Run Summary

**Run ID**: 152a053c-ded1-434e-960c-9b6b28797780
**Framework**: baes
**Started**: 2025-10-28T19:11:46.788142Z
**Completed**: 2025-10-28T19:16:17.538505Z
**Duration**: 270.75s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 34.14 |
| 2 | 2 | completed | 0/0 | 0 | 38.93 |
| 3 | 3 | completed | 0/0 | 0 | 50.46 |
| 4 | 4 | completed | 0/0 | 0 | 69.73 |
| 5 | 5 | completed | 0/0 | 0 | 39.01 |
| 6 | 6 | completed | 0/0 | 0 | 38.47 |

## Directory Structure

```
152a053c-ded1-434e-960c-9b6b28797780/
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
