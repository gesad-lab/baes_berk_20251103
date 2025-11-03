# Run Summary

**Run ID**: c1f1388a-daa9-4f67-a6bf-2eac6281375e
**Framework**: ghspec
**Started**: 2025-10-31T09:54:38.910420Z
**Completed**: 2025-10-31T10:12:43.136886Z
**Duration**: 1084.23s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 253.65 |
| 2 | 2 | completed | 0/0 | 0 | 166.71 |
| 3 | 3 | completed | 0/0 | 0 | 167.27 |
| 4 | 4 | completed | 0/0 | 0 | 178.60 |
| 5 | 5 | completed | 0/0 | 0 | 144.46 |
| 6 | 6 | completed | 0/0 | 0 | 173.53 |

## Directory Structure

```
c1f1388a-daa9-4f67-a6bf-2eac6281375e/
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
