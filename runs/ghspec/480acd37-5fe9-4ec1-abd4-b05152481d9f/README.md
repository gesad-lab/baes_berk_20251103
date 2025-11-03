# Run Summary

**Run ID**: 480acd37-5fe9-4ec1-abd4-b05152481d9f
**Framework**: ghspec
**Started**: 2025-10-30T03:01:40.259645Z
**Completed**: 2025-10-30T03:18:03.504632Z
**Duration**: 983.24s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 132.38 |
| 2 | 2 | completed | 0/0 | 0 | 161.38 |
| 3 | 3 | completed | 0/0 | 0 | 138.61 |
| 4 | 4 | completed | 0/0 | 0 | 265.37 |
| 5 | 5 | completed | 0/0 | 0 | 131.04 |
| 6 | 6 | completed | 0/0 | 0 | 154.45 |

## Directory Structure

```
480acd37-5fe9-4ec1-abd4-b05152481d9f/
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
