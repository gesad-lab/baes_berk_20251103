# Run Summary

**Run ID**: ae72f532-01be-4803-8dcb-2a99eba3db6e
**Framework**: ghspec
**Started**: 2025-10-30T02:11:28.767802Z
**Completed**: 2025-10-30T02:30:35.573098Z
**Duration**: 1146.81s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 196.95 |
| 2 | 2 | completed | 0/0 | 0 | 155.82 |
| 3 | 3 | completed | 0/0 | 0 | 135.13 |
| 4 | 4 | completed | 0/0 | 0 | 310.76 |
| 5 | 5 | completed | 0/0 | 0 | 207.51 |
| 6 | 6 | completed | 0/0 | 0 | 140.64 |

## Directory Structure

```
ae72f532-01be-4803-8dcb-2a99eba3db6e/
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
