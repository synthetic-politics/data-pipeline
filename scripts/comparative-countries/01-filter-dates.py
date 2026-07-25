import os
import re
import shutil
from datetime import datetime, date

PARTY_RANGES = {
    "onenationoz":              (date(2025,  1,  3), date(2025,  5,  3)),
    "peoplespca":               (date(2024, 12, 29), date(2025,  4, 28)),
    "thereformpartyuk":         (date(2024,  3,  6), date(2024,  7,  4)),
    "rassemblementnational_fr": (date(2024,  3,  2), date(2024,  7,  7)),
    "partijvoordevrijheidnl":   (date(2025,  7,  1), date(2025, 10, 29)),
    "fremskrittspartiet":       (date(2025,  5, 11), date(2025,  9,  8)),
    "vlaamsbelang":             (date(2024,  2, 10), date(2024,  6,  9)),
    "afd.bund":                 (date(2024, 10, 26), date(2025,  2, 23)),
    "patriotsep":               (date(2024,  2,  7), date(2024,  6,  9)),
}

LEADER_RANGES = {
    "senatorpaulinehanson":     (date(2025,  1,  3), date(2025,  5,  3)),
    "hon.maximebernier":        (date(2024, 12, 29), date(2025,  4, 28)),
    "nigel_farage":             (date(2024,  3,  6), date(2024,  7,  4)),
    "jordanbardella":           (date(2024,  2,  7), date(2024,  7,  7)),  # both FR + EU rows; widest range
    "geertwilders":             (date(2025,  7,  1), date(2025, 10, 29)),
    "sylvi_listhaug":           (date(2025,  5, 11), date(2025,  9,  8)),
    "vangriekentom":            (date(2024,  2, 10), date(2024,  6,  9)),
    "alice.weidel":             (date(2024, 10, 26), date(2025,  2, 23)),
}

DATE_RE = re.compile(r"^\d+_(\d{2})-(\d{2})-(\d{4})")

def parse_folder_date(name):
    m = DATE_RE.match(name)
    if not m:
        return None
    month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return date(year, month, day)

def delete_outside_range(root, username_map):
    for username, (start, end) in username_map.items():
        user_dir = os.path.join(root, username)
        if not os.path.isdir(user_dir):
            continue
        for entry in os.listdir(user_dir):
            entry_path = os.path.join(user_dir, entry)
            if not os.path.isdir(entry_path):
                continue
            d = parse_folder_date(entry)
            if d is None:
                continue
            if d < start or d > end:
                print(f"Deleting: {entry_path}")
                shutil.rmtree(entry_path)

PARTY_ROOT  = "party"
LEADER_ROOT = "leader"

delete_outside_range(PARTY_ROOT,  PARTY_RANGES)
delete_outside_range(LEADER_ROOT, LEADER_RANGES)
