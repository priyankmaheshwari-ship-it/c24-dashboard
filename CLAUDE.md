# Marketing Intelligence — Unified Ads Configuration

---

## 🤖 Automated Pipeline — System Config

### Pipeline File
`/Users/a38986/Desktop/Marketing C24/pipeline.py`

### Schedule
Daily at **9:00 AM IST** (3:30 AM UTC)

### What it does
1. Pulls Google Ads data (Search NB Buyer + UAC C2C) for all cities
2. Pulls Meta data (Cars24 India Buyer only)
3. Matches campaigns via `Campaign Mapping.xlsx` (Google + FB tabs)
4. Outputs **315 pre-aggregated rows** — city × platform × campaign_type × sub_metric × all time periods
5. Writes to Google Sheets → notifies BI team via Slack + Email

### Output Schema
`run_date | city | platform | campaign_type | sub_metric | D1 | LMTD | LM | MTD | MTD_vs_LMTD | PROJECTED | L7D | LL7D`

### ⚙️ Pending Config (fill to activate full pipeline)
| Item | Status | Where to update |
|---|---|---|
| Meta Access Token | ❌ Needs refresh | `pipeline.py` → `meta_access_token` |
| Google Sheet ID | ❌ Pending | `pipeline.py` → `sheet_id` |
| Service Account JSON | ❌ Pending | `pipeline.py` → `service_account_json` |
| Slack Webhook URL | ❌ Pending | `pipeline.py` → `slack_webhook` |
| Slack Channel | ❌ Pending | `pipeline.py` → `slack_channel` |
| Email Recipients | ❌ Pending | `pipeline.py` → `email_recipients` |
| Email Sender | ❌ Pending | `pipeline.py` → `email_sender` |

---

## 🧠 Saved Memory / Business Context

### Retail Business — Primary Google Ads Accounts
All retail business is currently mapped to these two accounts:

| Account Name | Customer ID |
|---|---|
| Search - NB Buyer Car | 5786527301 |
| UAC - C2C Buy Car App | 1365519291 |

> When the user refers to "retail", "retail campaigns", or "retail business" — always scope queries to these two accounts by default.

This file is automatically read by Claude Code. All credentials and account mappings are pre-configured. Team members can query Meta and Google Ads data directly — no additional setup required.

---

## Meta (Facebook) Ads

### Credentials
```
META_ACCESS_TOKEN = [REDACTED — stored in pipeline.py only, do not commit to git]
META_API_VERSION    = v19.0
```

> **Note:** Meta access tokens expire periodically. If you get an auth error, get a fresh token from [Meta Graph API Explorer](https://developers.facebook.com/tools/explorer/) and update the token above.

### Ad Accounts

| Account Name | Account ID | Currency |
|---|---|---|
| Cars24 India Buyer | act_613322046057641 | INR |
| Cars24 India Seller | act_773517116104203 | INR |
| Vehicleinfo | act_598945339294515 | INR |
| CARS24 New Car | act_863075695418028 | INR |
| CARS24 Challan | act_1113861233844848 | INR |
| Car Truth by CARS24 | act_1308533890312552 | INR |
| Cars24 Dealership | act_732607398480449 | INR |
| Cars24 Select | act_3285435364904854 | INR |
| CARS24 Autopilot | act_1391824934871515 | INR |
| Cars24_Aadhaar | act_1394013047911869 | INR |
| CARS24 Aadhaar Buyer | act_468132812270229 | INR |
| CARS24 Dealer Mall | act_1922353498291007 | INR |
| CARS24 Driving School | act_954694433422245 | INR |
| CARS24 Partners | act_585097047706924 | INR |
| CARS24 Orbit | act_2040946449752926 | INR |
| LOANS24 by CARS24 | act_475507992317333 | INR |
| Bikes24 Buyer | act_2065723820226777 | INR |
| Bikes24 Seller | act_1044063102666906 | INR |
| bikes24 brand boost | act_2071407599664697 | INR |
| Cars24 Buy Bike | act_8907948801 | INR |
| FourDoor by Cars24 | act_859814815885007 | INR |
| Cars24 Dubai | act_1800738986773542 | AED |
| Cars24 Dubai INR | act_748010345854739 | INR |
| Cars24 LAC | act_713184945902948 | INR |
| udaan - ad account | act_294475351486156 | INR |
| VehicleInfo (Read-Only) | act_1235223435251890 | INR |
| Cars24 (Read-Only) | act_4296009567353307 | INR |
| Car Info (Read-Only) | act_1219037069863326 | INR |

### How Claude Should Query Meta

Use the Graph API with `curl` — no Python library needed:

```bash
# Spend for a single account (last 30 days)
curl "https://graph.facebook.com/v19.0/{ACCOUNT_ID}/insights?fields=spend&date_preset=last_30d&access_token={META_ACCESS_TOKEN}"

# Custom date range
curl "https://graph.facebook.com/v19.0/{ACCOUNT_ID}/insights?fields=spend,impressions,clicks&time_range={'since':'2026-03-01','until':'2026-04-09'}&access_token={META_ACCESS_TOKEN}"
```

---

## Google Ads

### Credentials
```
GOOGLE_DEVELOPER_TOKEN = [REDACTED — stored in pipeline.py only, do not commit to git]
GOOGLE_CLIENT_ID       = [REDACTED — stored in pipeline.py only, do not commit to git]
GOOGLE_CLIENT_SECRET   = [REDACTED — stored in pipeline.py only, do not commit to git]
GOOGLE_REFRESH_TOKEN   = [REDACTED — stored in pipeline.py only, do not commit to git]
GOOGLE_MCC_ID          = 6392027424
```

> The refresh token does not expire. Google access tokens are auto-generated from the refresh token — no manual renewal needed.

### Ad Accounts (under MCC 6392027424)

| Account Name | Customer ID |
|---|---|
| Search - NB Buyer Car | 5786527301 |
| UAC - C2C Buy Car App | 1365519291 |
| Search - NB Seller Car | 7393657612 |
| VEHICLE INFO | 2071730146 |
| UAC Display App Seller Car | 5702104861 |
| Cars24 Brand | 5657819352 |
| CARS24 - Challan | 3792262964 |
| Appflix Studio | 3653203847 |
| CARS24 CAR TRUTH | 1525860450 |
| Australia Buy Car | 1832347197 |
| C2C Buy Bike App | 1304493101 |
| CARS24 - FourDoor | 4937657609 |
| CARS24 Autopilot | 3966245370 |
| CARS24 Bharat RTO | 2026071731 |
| CARS24 Fast Tag | 4050147780 |
| CARS24 New Cars | 5030437350 |
| CARS24_Insurance24 | 3521142723 |
| Car Service | 5550610042 |
| Cars24 Bike Seller | 8282323550 |
| Cars24 Branding YouTube | 8784673952 |
| Cars24 Buy Bike | 8907948801 |
| Google Alpha Zapar | 6004688007 |
| LOANS24 | 7659867635 |

### How Claude Should Query Google Ads

Use the Python `google-ads` library (already installed). Always use the MCC ID as `login_customer_id`.

```python
from google.ads.googleads.client import GoogleAdsClient
import warnings
warnings.filterwarnings('ignore')

config = {
    'developer_token': 'YOUR_DEVELOPER_TOKEN',      # stored in pipeline.py — do not commit
    'client_id': 'YOUR_CLIENT_ID',                  # stored in pipeline.py — do not commit
    'client_secret': 'YOUR_CLIENT_SECRET',          # stored in pipeline.py — do not commit
    'refresh_token': 'YOUR_REFRESH_TOKEN',          # stored in pipeline.py — do not commit
    'login_customer_id': '6392027424',
    'use_proto_plus': True
}

client = GoogleAdsClient.load_from_dict(config)
ga_service = client.get_service('GoogleAdsService')

# Query spend for a specific account and date range
query = """
    SELECT
        campaign.name,
        metrics.cost_micros,
        metrics.impressions,
        metrics.clicks
    FROM campaign
    WHERE segments.date BETWEEN '2026-03-31' AND '2026-04-09'
      AND metrics.cost_micros > 0
    ORDER BY metrics.cost_micros DESC
"""

response = ga_service.search(customer_id='5786527301', query=query)
for row in response:
    print(f"{row.campaign.name}: INR {row.metrics.cost_micros / 1_000_000:,.2f}")
```

> **Dependency:** Run `pip3 install google-ads` if not already installed.

---

## Infrastructure Notes

- **Google Cloud Project:** `marketing-crm-232411`
- **APIs Enabled:** Google Ads API (`googleads.googleapis.com`), Google Ad Manager API
- **OAuth Client Name:** `Unified Marketing AI - Apr26`
- **Meta App:** Graph API v19.0
- **Google Ads Library Version:** google-ads (v23+, Python 3.9+)
