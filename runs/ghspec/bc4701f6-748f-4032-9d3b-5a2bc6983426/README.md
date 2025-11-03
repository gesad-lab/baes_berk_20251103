# Run Summary

**Run ID**: bc4701f6-748f-4032-9d3b-5a2bc6983426
**Framework**: ghspec
**Started**: 2025-10-28T14:17:23.122907Z
**Completed**: 2025-10-28T14:39:46.712425Z
**Duration**: 1343.59s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 263.67 |
| 2 | 2 | completed | 0/0 | 0 | 142.68 |
| 3 | 3 | completed | 0/0 | 0 | 252.07 |
| 4 | 4 | completed | 0/0 | 0 | 194.76 |
| 5 | 5 | completed | 0/0 | 0 | 229.16 |
| 6 | 6 | completed | 0/0 | 0 | 261.25 |

## Directory Structure

```
bc4701f6-748f-4032-9d3b-5a2bc6983426/
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
