#!/usr/bin/env python3
"""Standardise the 'All guides' navigation block across the
rights-after-death section. Replaces the <nav class="rad-guides"> block in
each guide page (except index.html, which has its own richer version)."""

import re
import pathlib

STD_NAV = '''      <nav class="rad-guides" aria-label="All guides">
        <h2>All guides</h2>
        <div class="rad-group">
          <h3>Getting the records</h3>
          <ul class="rad-guide-list">
            <li><a href="medical-records.html">Request a deceased relative's medical records</a></li>
            <li><a href="when-refused.html">What to do when the hospital refuses</a></li>
            <li><a href="subject-access-request.html">Request your own data from the hospital</a></li>
            <li><a href="nhs-board-contacts.html">Scottish NHS board records contacts</a></li>
          </ul>
        </div>
        <div class="rad-group">
          <h3>Making a complaint</h3>
          <ul class="rad-guide-list">
            <li><a href="regulators.html">Which regulator handles what</a></li>
            <li><a href="complain-gmc.html">Complain about a doctor (GMC)</a></li>
            <li><a href="complain-nmc.html">Complain about a nurse or midwife (NMC)</a></li>
            <li><a href="complain-sssc.html">Complain about a social care worker (SSSC)</a></li>
            <li><a href="complain-spso.html">Complain about the NHS board (SPSO)</a></li>
            <li><a href="complain-ico.html">Complain about data or records (ICO)</a></li>
            <li><a href="complain-slcc.html">Complain about a solicitor (SLCC)</a></li>
          </ul>
        </div>
        <div class="rad-group">
          <h3>Your rights and support</h3>
          <ul class="rad-guide-list">
            <li><a href="childs-rights.html">Your rights as a child of the deceased</a></li>
            <li><a href="help.html">Free and low-cost help</a></li>
          </ul>
        </div>
      </nav>'''

NAV_RE = re.compile(
    r'      <nav class="rad-guides" aria-label="All guides">.*?</nav>',
    re.DOTALL,
)

base = pathlib.Path(__file__).resolve().parent.parent / "rights-after-death"
skip = {"index.html"}

for path in sorted(base.glob("*.html")):
    if path.name in skip:
        continue
    text = path.read_text(encoding="utf-8")
    new_text, n = NAV_RE.subn(STD_NAV, text)
    if n:
        path.write_text(new_text, encoding="utf-8")
        print(f"updated {path.name} ({n} nav block)")
    else:
        print(f"no nav block found in {path.name}")
