# Run Summary

**Run ID**: f1de7e5a-9108-4f66-a188-f938e05182cd
**Framework**: ghspec
**Started**: 2025-10-30T21:45:50.695962Z
**Completed**: 2025-10-30T22:04:21.896520Z
**Duration**: 1111.20s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 225.85 |
| 2 | 2 | completed | 0/0 | 0 | 164.91 |
| 3 | 3 | completed | 0/0 | 0 | 111.98 |
| 4 | 4 | completed | 0/0 | 0 | 172.97 |
| 5 | 5 | completed | 0/0 | 0 | 131.02 |
| 6 | 6 | completed | 0/0 | 0 | 304.47 |

## Directory Structure

```
f1de7e5a-9108-4f66-a188-f938e05182cd/
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
