# Run Summary

**Run ID**: d9538a75-6203-41f6-87c4-f47b10e5f41c
**Framework**: ghspec
**Started**: 2025-10-30T12:34:00.336927Z
**Completed**: 2025-10-30T12:52:36.305592Z
**Duration**: 1115.97s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 114.55 |
| 2 | 2 | completed | 0/0 | 0 | 146.90 |
| 3 | 3 | completed | 0/0 | 0 | 142.86 |
| 4 | 4 | completed | 0/0 | 0 | 246.06 |
| 5 | 5 | completed | 0/0 | 0 | 171.32 |
| 6 | 6 | completed | 0/0 | 0 | 294.26 |

## Directory Structure

```
d9538a75-6203-41f6-87c4-f47b10e5f41c/
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
