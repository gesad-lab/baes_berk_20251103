# Run Summary

**Run ID**: 0ec2f5c7-7667-4339-bbb0-5896b046d20b
**Framework**: chatdev
**Started**: 2025-10-29T11:15:16.837610Z
**Completed**: 2025-10-29T11:35:11.649186Z
**Duration**: 1194.81s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 267.42 |
| 2 | 2 | completed | 0/0 | 0 | 249.13 |
| 3 | 3 | completed | 0/0 | 0 | 137.63 |
| 4 | 4 | completed | 0/0 | 0 | 178.56 |
| 5 | 5 | completed | 0/0 | 0 | 181.53 |
| 6 | 6 | completed | 0/0 | 0 | 180.54 |

## Directory Structure

```
0ec2f5c7-7667-4339-bbb0-5896b046d20b/
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
