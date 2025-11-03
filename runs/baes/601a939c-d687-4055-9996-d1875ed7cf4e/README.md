# Run Summary

**Run ID**: 601a939c-d687-4055-9996-d1875ed7cf4e
**Framework**: baes
**Started**: 2025-10-28T22:26:37.054586Z
**Completed**: 2025-10-28T22:29:23.132225Z
**Duration**: 166.08s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.01 |
| 2 | 2 | completed | 0/0 | 0 | 29.73 |
| 3 | 3 | completed | 0/0 | 0 | 33.35 |
| 4 | 4 | completed | 0/0 | 0 | 23.59 |
| 5 | 5 | completed | 0/0 | 0 | 30.32 |
| 6 | 6 | completed | 0/0 | 0 | 30.06 |

## Directory Structure

```
601a939c-d687-4055-9996-d1875ed7cf4e/
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
