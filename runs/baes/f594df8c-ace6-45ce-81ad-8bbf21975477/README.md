# Run Summary

**Run ID**: f594df8c-ace6-45ce-81ad-8bbf21975477
**Framework**: baes
**Started**: 2025-10-30T21:09:44.556910Z
**Completed**: 2025-10-30T21:13:05.460937Z
**Duration**: 200.90s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.51 |
| 2 | 2 | completed | 0/0 | 0 | 27.94 |
| 3 | 3 | completed | 0/0 | 0 | 34.76 |
| 4 | 4 | completed | 0/0 | 0 | 44.33 |
| 5 | 5 | completed | 0/0 | 0 | 27.34 |
| 6 | 6 | completed | 0/0 | 0 | 33.02 |

## Directory Structure

```
f594df8c-ace6-45ce-81ad-8bbf21975477/
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
