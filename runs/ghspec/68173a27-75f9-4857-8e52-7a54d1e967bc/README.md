# Run Summary

**Run ID**: 68173a27-75f9-4857-8e52-7a54d1e967bc
**Framework**: ghspec
**Started**: 2025-10-30T01:30:27.480138Z
**Completed**: 2025-10-30T01:49:22.616295Z
**Duration**: 1135.14s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 218.26 |
| 2 | 2 | completed | 0/0 | 0 | 153.51 |
| 3 | 3 | completed | 0/0 | 0 | 240.69 |
| 4 | 4 | completed | 0/0 | 0 | 205.08 |
| 5 | 5 | completed | 0/0 | 0 | 165.81 |
| 6 | 6 | completed | 0/0 | 0 | 151.78 |

## Directory Structure

```
68173a27-75f9-4857-8e52-7a54d1e967bc/
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
