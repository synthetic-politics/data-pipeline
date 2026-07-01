# data-pipeline

HOW TO USE:
good quesiton

Note: Videos are too large to be stored within the repo, hence this is images only

```text
project/
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── docs/
│   └── README.md
└── tests/
```
Data processing flow chart:
```mermaid
flowchart TD
    A[Data Collection] --> B[One Nation]
    A --> C[Comparative Countries]

    %% One Nation branch
    B --> B1[Collect Social Media Data]
    B1 --> B1a["1. Instagram
2. Facebook
3. Twitter
4. TikTok
5. YouTube"]
    B1a --> B1b["Using gallery-dl,
IG-Grab Firefox addon
(addons.mozilla.org/en-US/firefox/addon/ig-grab), etc."]

    B --> B2[Collect Other Data]
    B2 --> B2a["Party website via
Internet Archive's Wayback Machine
& physical advertisements via Trove"]

    B --> B3[Deduplicate Data]
    B3 --> B3a["Using GitHub software
idealo/imagededup"]

    %% Comparative Countries branch
    C --> C1[Collect Social Media Data]
    C1 --> C1a["Using Firefox extension
IG-Grab (addons.mozilla.org/en-US/firefox/addon/ig-grab)"]

    C --> C2[Extract & Translate Non-English Text]
    C2 --> C2a["Using GitHub software
PaddlePaddle/PaddleOCR"]

    C --> C3[Translate & Transcribe Non-English Audio]
    C3 --> C3a["Using GitHub software
openai/whisper"]
```
