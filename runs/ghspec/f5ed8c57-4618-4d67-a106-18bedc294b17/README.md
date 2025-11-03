# Run Summary

**Run ID**: f5ed8c57-4618-4d67-a106-18bedc294b17
**Framework**: ghspec
**Started**: 2025-10-29T03:48:22.590438Z
**Completed**: 2025-10-29T04:05:43.731207Z
**Duration**: 1041.14s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 158.93 |
| 2 | 2 | completed | 0/0 | 0 | 128.96 |
| 3 | 3 | completed | 0/0 | 0 | 217.56 |
| 4 | 4 | completed | 0/0 | 0 | 176.75 |
| 5 | 5 | completed | 0/0 | 0 | 159.20 |
| 6 | 6 | completed | 0/0 | 0 | 199.73 |

## Directory Structure

```
f5ed8c57-4618-4d67-a106-18bedc294b17/
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
