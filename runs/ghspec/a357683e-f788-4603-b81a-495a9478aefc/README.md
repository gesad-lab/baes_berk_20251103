# Run Summary

**Run ID**: a357683e-f788-4603-b81a-495a9478aefc
**Framework**: ghspec
**Started**: 2025-10-30T09:45:30.350786Z
**Completed**: 2025-10-30T10:05:13.153061Z
**Duration**: 1182.80s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 192.28 |
| 2 | 2 | completed | 0/0 | 0 | 195.65 |
| 3 | 3 | completed | 0/0 | 0 | 194.59 |
| 4 | 4 | completed | 0/0 | 0 | 180.06 |
| 5 | 5 | completed | 0/0 | 0 | 175.37 |
| 6 | 6 | completed | 0/0 | 0 | 244.84 |

## Directory Structure

```
a357683e-f788-4603-b81a-495a9478aefc/
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
