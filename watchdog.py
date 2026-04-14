"""
CARS24 Pipeline Watchdog
========================
Runs daily at 10:00 AM IST (4:30 AM UTC) — one hour after the pipeline.
Checks whether today's pipeline completed successfully.
If not, sends an alert email to the team.

Usage (cron):
  30 4 * * * /usr/bin/python3 '/Users/a38986/Desktop/Marketing C24/watchdog.py'
"""

import os
import logging
import smtplib
from datetime import date, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── Config ────────────────────────────────────────────────────────────
LOG_DIR        = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
PIPELINE_LOG   = os.path.join(LOG_DIR, 'pipeline.log')
WATCHDOG_LOG   = os.path.join(LOG_DIR, 'watchdog.log')

EMAIL_SENDER   = 'priyank.maheshwari@cars24.com'
APP_PASSWORD   = 'mukq fgfh jdhw ycpb'
RECIPIENTS     = [
    'priyank.maheshwari@cars24.com',
    'tanishka.tanwar@cars24.com',
    'tejaswi.kumawat@cars24.com',
]

# ── Logging ───────────────────────────────────────────────────────────
os.makedirs(LOG_DIR, exist_ok=True)
fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
fh  = logging.FileHandler(WATCHDOG_LOG)
fh.setFormatter(fmt)
sh  = logging.StreamHandler()
sh.setFormatter(fmt)
logging.basicConfig(level=logging.INFO, handlers=[fh, sh])
log = logging.getLogger('watchdog')


def expected_run_date():
    """Pipeline runs at 9 AM IST and reports yesterday's data."""
    return str(date.today() - timedelta(days=1))


def check_sentinel(run_date):
    """Return True if pipeline wrote a success sentinel for run_date."""
    sentinel = os.path.join(LOG_DIR, f'success_{run_date}.ok')
    return os.path.exists(sentinel)


def tail_log(path, lines=40):
    """Return last N lines of a file."""
    try:
        with open(path) as f:
            all_lines = f.readlines()
        return ''.join(all_lines[-lines:])
    except Exception:
        return '(log file not found or unreadable)'


def send_alert(run_date, log_tail):
    msg = MIMEMultipart()
    msg['Subject'] = f'🚨 CARS24 Pipeline MISSED — {run_date}'
    msg['From']    = EMAIL_SENDER
    msg['To']      = ', '.join(RECIPIENTS)

    body = f"""Hi Team,

⚠️  The CARS24 Marketing Pipeline DID NOT complete successfully today.

Expected run date : {run_date}
Checked at        : 10:00 AM IST

No success sentinel was found in:
  {LOG_DIR}/success_{run_date}.ok

This means the dashboard data was NOT updated and no email was sent.

ACTION REQUIRED:
  1. Check the pipeline log below for errors.
  2. Re-run manually:
       /usr/bin/python3 '/Users/a38986/Desktop/Marketing C24/pipeline.py'
  3. Verify Full Disk Access is still granted to /usr/sbin/cron in
     System Settings → Privacy & Security → Full Disk Access.

── Last 40 lines of pipeline.log ──────────────────────────────────────
{log_tail}
────────────────────────────────────────────────────────────────────────

— CARS24 Marketing Watchdog
"""
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(EMAIL_SENDER, APP_PASSWORD)
            s.sendmail(EMAIL_SENDER, RECIPIENTS, msg.as_string())
        log.info(f'Alert email sent to {RECIPIENTS}')
    except Exception as ex:
        log.error(f'Failed to send alert email: {ex}')


def send_ok(run_date):
    """Optional: log a confirmation that everything is fine."""
    log.info(f'✅  Pipeline sentinel found for {run_date} — all good.')


def main():
    log.info('── Watchdog starting ──')
    run_date = expected_run_date()
    log.info(f'Checking pipeline completion for run_date={run_date}')

    if check_sentinel(run_date):
        send_ok(run_date)
    else:
        log.warning(f'❌  No sentinel for {run_date} — pipeline appears to have missed!')
        log_tail = tail_log(PIPELINE_LOG)
        send_alert(run_date, log_tail)

    log.info('── Watchdog done ──')


if __name__ == '__main__':
    main()
