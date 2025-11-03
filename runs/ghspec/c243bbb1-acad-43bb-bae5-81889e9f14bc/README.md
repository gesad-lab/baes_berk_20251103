# Run Summary

**Run ID**: c243bbb1-acad-43bb-bae5-81889e9f14bc
**Framework**: ghspec
**Started**: 2025-10-29T23:47:43.919986Z
**Completed**: 2025-10-30T00:04:09.369722Z
**Duration**: 985.45s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 200.27 |
| 2 | 2 | completed | 0/0 | 0 | 141.33 |
| 3 | 3 | completed | 0/0 | 0 | 130.76 |
| 4 | 4 | completed | 0/0 | 0 | 212.78 |
| 5 | 5 | completed | 0/0 | 0 | 143.28 |
| 6 | 6 | completed | 0/0 | 0 | 157.02 |

## Directory Structure

```
c243bbb1-acad-43bb-bae5-81889e9f14bc/
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
