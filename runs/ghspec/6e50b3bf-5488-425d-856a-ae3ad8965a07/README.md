# Run Summary

**Run ID**: 6e50b3bf-5488-425d-856a-ae3ad8965a07
**Framework**: ghspec
**Started**: 2025-10-30T05:53:39.051309Z
**Completed**: 2025-10-30T06:10:23.068451Z
**Duration**: 1004.02s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 143.81 |
| 2 | 2 | completed | 0/0 | 0 | 140.44 |
| 3 | 3 | completed | 0/0 | 0 | 185.04 |
| 4 | 4 | completed | 0/0 | 0 | 197.93 |
| 5 | 5 | completed | 0/0 | 0 | 176.59 |
| 6 | 6 | completed | 0/0 | 0 | 160.19 |

## Directory Structure

```
6e50b3bf-5488-425d-856a-ae3ad8965a07/
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
