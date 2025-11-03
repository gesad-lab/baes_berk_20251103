# Run Summary

**Run ID**: af5949d0-8b82-4a3e-86b0-22b0213f069c
**Framework**: chatdev
**Started**: 2025-10-28T16:16:42.831751Z
**Completed**: 2025-10-28T16:47:31.576169Z
**Duration**: 1848.74s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 313.27 |
| 2 | 2 | completed | 0/0 | 0 | 250.65 |
| 3 | 3 | completed | 0/0 | 0 | 320.31 |
| 4 | 4 | completed | 0/0 | 0 | 306.23 |
| 5 | 5 | completed | 0/0 | 0 | 341.53 |
| 6 | 6 | completed | 0/0 | 0 | 316.74 |

## Directory Structure

```
af5949d0-8b82-4a3e-86b0-22b0213f069c/
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
