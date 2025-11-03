# Run Summary

**Run ID**: a1854742-b8f6-46cd-a952-a0af0eafb96b
**Framework**: chatdev
**Started**: 2025-10-30T00:46:05.667682Z
**Completed**: 2025-10-30T01:03:53.192576Z
**Duration**: 1067.52s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 141.32 |
| 2 | 2 | completed | 0/0 | 0 | 152.30 |
| 3 | 3 | completed | 0/0 | 0 | 167.31 |
| 4 | 4 | completed | 0/0 | 0 | 195.64 |
| 5 | 5 | completed | 0/0 | 0 | 168.82 |
| 6 | 6 | completed | 0/0 | 0 | 242.13 |

## Directory Structure

```
a1854742-b8f6-46cd-a952-a0af0eafb96b/
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
