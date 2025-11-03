# Run Summary

**Run ID**: 6d1996e6-76d2-465d-9d0d-4cec2e1000de
**Framework**: ghspec
**Started**: 2025-10-29T18:50:30.332736Z
**Completed**: 2025-10-29T19:12:47.737112Z
**Duration**: 1337.40s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 331.35 |
| 2 | 2 | completed | 0/0 | 0 | 167.61 |
| 3 | 3 | completed | 0/0 | 0 | 164.76 |
| 4 | 4 | completed | 0/0 | 0 | 183.24 |
| 5 | 5 | completed | 0/0 | 0 | 166.22 |
| 6 | 6 | completed | 0/0 | 0 | 324.20 |

## Directory Structure

```
6d1996e6-76d2-465d-9d0d-4cec2e1000de/
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
