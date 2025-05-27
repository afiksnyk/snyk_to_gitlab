import json
from datetime import datetime

def map_severity(level):
    return {"error": "High", "warning": "Medium", "note": "Low"}.get(level.lower(), "Unknown")

def convert(sarif_path, output_path):
    with open(sarif_path, "r") as f:
        sarif_data = json.load(f)
    results = sarif_data.get("runs", [{}])[0].get("results", [])

    report = {
        "version": "15.0.4",
        "vulnerabilities": [],
        "remediations": []
    }

    for result in results:
        rule_id = result.get("ruleId", "unknown")
        msg = result.get("message", {}).get("text", "")
        locs = result.get("locations", [])
        if not locs: continue
        file_path = locs[0].get("physicalLocation", {}).get("artifactLocation", {}).get("uri", "")
        line = locs[0].get("physicalLocation", {}).get("region", {}).get("startLine", 1)
        severity = map_severity(result.get("level", "note"))
        now = datetime.utcnow().isoformat() + "Z"

        report["vulnerabilities"].append({
            "id": f"snyk-{rule_id}-{line}",
            "category": "sast",
            "name": rule_id,
            "message": msg,
            "severity": severity,
            "confidence": "High",
            "scanner": {"id": "snykcode", "name": "SnykCode"},
            "location": {"file": file_path, "start_line": line},
            "identifiers": [{"type": "sast", "name": rule_id, "value": rule_id}],
            "created_at": now,
            "updated_at": now
        })

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
