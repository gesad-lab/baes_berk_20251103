# Run Summary

**Run ID**: bbcaad50-7295-4472-b21a-d6bc8214004a
**Framework**: baes
**Started**: 2025-10-29T11:11:36.688522Z
**Completed**: 2025-10-29T11:15:15.804149Z
**Duration**: 219.12s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 20.90 |
| 2 | 2 | completed | 0/0 | 0 | 63.01 |
| 3 | 3 | completed | 0/0 | 0 | 31.58 |
| 4 | 4 | completed | 0/0 | 0 | 33.84 |
| 5 | 5 | completed | 0/0 | 0 | 35.73 |
| 6 | 6 | completed | 0/0 | 0 | 34.04 |

## Directory Structure

```
bbcaad50-7295-4472-b21a-d6bc8214004a/
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
