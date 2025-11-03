# Run Summary

**Run ID**: ed87f947-f444-4b0a-b8bd-2c1aed7ceab8
**Framework**: ghspec
**Started**: 2025-10-28T21:09:10.191837Z
**Completed**: 2025-10-28T21:40:45.534795Z
**Duration**: 1895.34s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 392.06 |
| 2 | 2 | completed | 0/0 | 0 | 204.87 |
| 3 | 3 | completed | 0/0 | 0 | 330.82 |
| 4 | 4 | completed | 0/0 | 0 | 244.63 |
| 5 | 5 | completed | 0/0 | 0 | 400.61 |
| 6 | 6 | completed | 0/0 | 0 | 322.35 |

## Directory Structure

```
ed87f947-f444-4b0a-b8bd-2c1aed7ceab8/
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
