# Run Summary

**Run ID**: 7bc72e06-642b-4f62-a87f-87c2282d26ae
**Framework**: chatdev
**Started**: 2025-10-29T13:53:08.763644Z
**Completed**: 2025-10-29T14:14:12.766918Z
**Duration**: 1264.00s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 171.46 |
| 2 | 2 | completed | 0/0 | 0 | 138.50 |
| 3 | 3 | completed | 0/0 | 0 | 199.84 |
| 4 | 4 | completed | 0/0 | 0 | 292.53 |
| 5 | 5 | completed | 0/0 | 0 | 240.01 |
| 6 | 6 | completed | 0/0 | 0 | 221.65 |

## Directory Structure

```
7bc72e06-642b-4f62-a87f-87c2282d26ae/
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
