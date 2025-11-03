# Run Summary

**Run ID**: 3786d26d-4a70-482f-b15a-b9485749a81c
**Framework**: chatdev
**Started**: 2025-10-30T19:54:02.414036Z
**Completed**: 2025-10-30T20:12:28.839219Z
**Duration**: 1106.43s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 128.05 |
| 2 | 2 | completed | 0/0 | 0 | 178.98 |
| 3 | 3 | completed | 0/0 | 0 | 220.14 |
| 4 | 4 | completed | 0/0 | 0 | 202.44 |
| 5 | 5 | completed | 0/0 | 0 | 220.11 |
| 6 | 6 | completed | 0/0 | 0 | 156.69 |

## Directory Structure

```
3786d26d-4a70-482f-b15a-b9485749a81c/
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
