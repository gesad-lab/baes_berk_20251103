# Run Summary

**Run ID**: ee7e1812-6509-4bbb-8133-b9ed038ffa1b
**Framework**: chatdev
**Started**: 2025-10-29T20:38:08.195104Z
**Completed**: 2025-10-29T20:56:33.224109Z
**Duration**: 1105.03s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 224.18 |
| 2 | 2 | completed | 0/0 | 0 | 152.19 |
| 3 | 3 | completed | 0/0 | 0 | 161.53 |
| 4 | 4 | completed | 0/0 | 0 | 163.55 |
| 5 | 5 | completed | 0/0 | 0 | 174.30 |
| 6 | 6 | completed | 0/0 | 0 | 229.28 |

## Directory Structure

```
ee7e1812-6509-4bbb-8133-b9ed038ffa1b/
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
