# Run Summary

**Run ID**: cbe8ae19-e1ec-4619-8a1e-99f34bd017b1
**Framework**: ghspec
**Started**: 2025-10-31T00:28:45.993803Z
**Completed**: 2025-10-31T00:47:44.359418Z
**Duration**: 1138.37s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 184.72 |
| 2 | 2 | completed | 0/0 | 0 | 227.63 |
| 3 | 3 | completed | 0/0 | 0 | 165.56 |
| 4 | 4 | completed | 0/0 | 0 | 246.99 |
| 5 | 5 | completed | 0/0 | 0 | 139.37 |
| 6 | 6 | completed | 0/0 | 0 | 174.10 |

## Directory Structure

```
cbe8ae19-e1ec-4619-8a1e-99f34bd017b1/
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
