# Run Summary

**Run ID**: 5fb8d53b-b352-4b00-b694-c57ca06cafca
**Framework**: chatdev
**Started**: 2025-10-30T06:54:20.657633Z
**Completed**: 2025-10-30T07:10:18.482999Z
**Duration**: 957.83s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 130.50 |
| 2 | 2 | completed | 0/0 | 0 | 116.93 |
| 3 | 3 | completed | 0/0 | 0 | 158.11 |
| 4 | 4 | completed | 0/0 | 0 | 192.54 |
| 5 | 5 | completed | 0/0 | 0 | 166.07 |
| 6 | 6 | completed | 0/0 | 0 | 193.67 |

## Directory Structure

```
5fb8d53b-b352-4b00-b694-c57ca06cafca/
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
