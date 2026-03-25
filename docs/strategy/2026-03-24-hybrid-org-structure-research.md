# Hybrid Nonprofit/For-Profit Organizational Structures Research
## For ORGANVM System Architecture Decision

**Date:** 2026-03-24
**Status:** Research Complete
**Context:** ORGANVM is an 8-organ creative-institutional system (117 repos) spanning academic research, generative art, governance tooling, and commercial products/SaaS. This research evaluates 12 hybrid organizational models for structuring the legal/financial entity.

---

## Table of Contents

1. [Mozilla Model (501(c)(3) + For-Profit Subsidiary)](#1-mozilla-model)
2. [Linux Foundation Model (501(c)(6) Trade Association)](#2-linux-foundation-model)
3. [Apache Software Foundation Model (501(c)(3) Pure Open Source)](#3-apache-software-foundation-model)
4. [NumFOCUS Model (Fiscal Sponsorship)](#4-numfocus-model)
5. [Creative Commons Model (Nonprofit Toolmaker)](#5-creative-commons-model)
6. [Blender Foundation Model (Foundation + Institute + Commercial)](#6-blender-foundation-model)
7. [Processing Foundation Model (Nonprofit Creative Coding)](#7-processing-foundation-model)
8. [L3C (Low-Profit Limited Liability Company)](#8-l3c-model)
9. [B-Corp / Benefit Corporation](#9-b-corp--benefit-corporation)
10. [Public Benefit Corporation (PBC)](#10-public-benefit-corporation)
11. [Cooperative Model](#11-cooperative-model)
12. [Fiscal Sponsorship + Separate LLC](#12-fiscal-sponsorship--separate-llc)
13. [Comparative Analysis for ORGANVM](#13-comparative-analysis-for-organvm)
14. [Recommended Path](#14-recommended-path)

---

## 1. Mozilla Model

### 501(c)(3) Foundation Owns 100% of For-Profit Corporation

#### Legal Structure

```
Mozilla Foundation [501(c)(3), California]
  |
  |-- 100% owns --> Mozilla Corporation [C-Corp, taxable]
  |                    |
  |                    |-- 100% owns --> Mozilla Online [China subsidiary]
  |
  |-- 100% owns --> MZLA Technologies Corporation [C-Corp, taxable]
```

- **Mozilla Foundation**: California nonprofit, IRS 501(c)(3). Established July 2003.
- **Mozilla Corporation**: Taxable for-profit subsidiary, created August 2005. No shareholders beyond the Foundation, no stock options issued, no dividends paid. All profits reinvested.
- **MZLA Technologies**: Separate subsidiary for Thunderbird and other products. Pays license fees to Foundation.

#### How Commercial Revenue Flows

- Mozilla Corporation earns ~$500-600M/year primarily from search engine royalties (Google pays to be default search in Firefox).
- Corporation pays Foundation ~$18-19M/year in trademark license fees (royalties for use of Mozilla trademarks).
- Foundation uses license fee income plus ~$7.8M in donations/grants for charitable programs.
- Corporation pays all its own expenses, salaries, and taxes as a regular C-Corp.

#### Tax Implications

- **Foundation**: Tax-exempt on charitable income. License fee royalties from subsidiary are generally exempt from UBIT (royalty exclusion). Donations to Foundation are tax-deductible for donors.
- **Corporation**: Fully taxable C-Corp. Pays corporate income tax on all profits. The license fees paid to Foundation are deductible business expenses.
- **Key risk**: If IRS determines Foundation's primary activity is operating the Corporation rather than charitable work, exemption could be challenged.

#### Grant Eligibility

- Foundation can receive foundation grants, government grants, and tax-deductible individual donations.
- Corporation cannot receive charitable grants but can receive commercial investment.

#### IP Handling

- Foundation owns all Mozilla trademarks and brand assets.
- Corporation licenses trademarks from Foundation via written license agreement.
- Copyright in Firefox code is held by contributors under Mozilla Public License (MPL 2.0).
- Foundation controls the licensing terms.

#### Setup Cost and Timeline

- Forming the 501(c)(3): ~$600 IRS filing fee (Form 1023) + $50-200 state filing + $2,000-10,000 legal counsel = ~$3,000-11,000.
- IRS approval: 6-10 months for Form 1023.
- Forming the C-Corp subsidiary: ~$300-1,000 state filing + legal drafting of intercompany agreements.
- Total realistic timeline: 8-14 months from start to fully operational.

#### Ongoing Compliance

- **High.** Two sets of books, two tax returns (990 for Foundation, 1120 for Corporation).
- Annual 990 filing (public document) for Foundation.
- Arm's-length transactions between entities must be documented.
- Board governance: some overlap OK but complete overlap is risky. Need independent directors on Foundation board.
- Foundation must demonstrate its primary purpose remains charitable, not merely holding a for-profit.

#### Examples Using This Model

- Mozilla Foundation / Mozilla Corporation
- Wikimedia Foundation (similar concept, though no for-profit sub)
- Khan Academy (501(c)(3) without for-profit sub, but comparable)

#### Pros for Solo Practitioner Building Toward Scale

- Maximum flexibility: charitable work gets donations/grants; commercial work generates revenue.
- Clear separation protects tax-exempt status.
- Foundation maintains mission control over for-profit activities.
- Well-understood model with extensive legal precedent.
- Can attract both philanthropic and commercial funding.

#### Cons for Solo Practitioner Building Toward Scale

- IRS requires minimum 3 unrelated board members for Foundation -- cannot be truly solo.
- High compliance burden: two entities, two sets of governance, annual filings.
- Intercompany transactions must be at arm's length and well-documented.
- Risk of IRS scrutiny if Foundation appears to exist primarily to shelter Corporation income.
- Significant ongoing legal/accounting costs ($5,000-15,000+/year for both entities).

---

## 2. Linux Foundation Model

### 501(c)(6) Trade Association / Business League

#### Legal Structure

```
Linux Foundation [501(c)(6), Delaware]
  |
  |-- Hosts --> 100+ collaborative projects (CNCF, Hyperledger, etc.)
  |-- Operates --> Training & Certification programs
  |-- Runs --> Events (Open Source Summit, KubeCon via CNCF, etc.)
  |
  Members: Corporate (tiered) + Individual supporters
```

- **Single entity**: 501(c)(6) business league / trade association.
- **No separate for-profit subsidiary** needed -- 501(c)(6) can conduct commercial activities directly.
- Members pay tiered dues; Platinum members pay $500K+/year.

#### How Commercial Revenue Flows

- **2025 projected revenue: ~$311M**
  - Membership dues & donations: $133M (43%)
  - Project services: $83M (27%)
  - Training & certification: $29M (9%)
  - Events: $58M (19%)
- All revenue flows through the single entity.
- Training, certification, and events are direct commercial activities -- this is legal for 501(c)(6).
- No UBIT issues because commercial activities serve members' business interests (the exempt purpose).

#### Tax Implications

- **Tax-exempt** on income related to exempt purpose (promoting common business interests of members).
- Donations/dues are **not** tax-deductible as charitable contributions (unlike 501(c)(3)).
- However, membership dues **are** deductible as ordinary business expenses for corporate members.
- UBIT applies to income from activities not related to exempt purpose (rare for LF since most activities qualify).
- No property tax exemption in most states (unlike 501(c)(3)).

#### Grant Eligibility

- **Cannot** receive most foundation grants (foundations can only grant to 501(c)(3)s or exercise expenditure responsibility).
- **Can** receive government contracts and corporate sponsorships.
- Corporate members often fund projects through their dues rather than separate grants.

#### IP Handling

- Linux Foundation typically does **not** own project IP.
- Projects use their own open-source licenses (Apache 2.0, MIT, GPL, etc.).
- LF provides neutral governance, infrastructure, and trademark management.
- Trademark ownership varies by project -- some held by LF, some by project-specific entities.

#### Setup Cost and Timeline

- Form 1024 filing fee: $600.
- State incorporation: $50-200.
- Legal counsel for bylaws and membership agreements: $5,000-15,000.
- IRS processing: 3-6 months (typically faster than 501(c)(3)).
- Total: ~$6,000-16,000 over 4-8 months.

#### Ongoing Compliance

- **Moderate.** Single entity, single tax return (Form 990).
- Must demonstrate activities serve members' common business interests.
- Membership structure and dues must be reasonable and non-discriminatory.
- Less public scrutiny than 501(c)(3) but still public 990 filing.
- Must avoid substantial lobbying (though more flexibility than 501(c)(3)).

#### Examples Using This Model

- Linux Foundation ($311M revenue)
- Rust Foundation
- OpenID Foundation
- OpenJS Foundation (jQuery, Node.js, etc.)
- Eclipse Foundation (originally, now international)

#### Pros for Solo Practitioner

- Can conduct commercial activities (training, certification, events, consulting) directly.
- No need for separate for-profit entity.
- Corporate members' dues are business-deductible (easy sell for sponsors).
- More operational flexibility than 501(c)(3).
- Single entity simplifies governance and compliance.

#### Cons for Solo Practitioner

- Need meaningful membership base -- hard to justify as a "business league" without members.
- Cannot receive tax-deductible charitable donations from individuals.
- Cannot receive most foundation/government grants.
- Less suited for academic/research activities (that's 501(c)(3) territory).
- Harder to attract individual donors (no tax deduction incentive).
- Must serve members' interests, not just the founder's vision.

---

## 3. Apache Software Foundation Model

### 501(c)(3) Producing Open Source for Public Good

#### Legal Structure

```
Apache Software Foundation [501(c)(3), Delaware membership corporation]
  |
  |-- Board of Directors (elected by Members)
  |       |
  |       |-- Appoints --> Officers (President, VP, Secretary, Treasurer)
  |       |-- Appoints --> Project Management Committees (PMCs)
  |
  |-- 320+ Apache projects
  |-- ~8,800 committers
  |-- ~850 individual Members (elected by existing Members)
```

- **Single entity**: 501(c)(3) charitable organization.
- **Membership corporation**: Members are individuals who have demonstrated merit (not companies).
- **No for-profit subsidiary**: All commercial exploitation happens externally by third parties using Apache-licensed software.
- **Vendor-neutral**: Corporations cannot directly participate in governance.

#### How Commercial Revenue Flows

- **Annual revenue: ~$2.4M** (tiny relative to software's commercial impact).
- Revenue comes from: corporate sponsorships (tiered), individual donations, and event income.
- ASF does **not** sell software or services.
- Companies like Cloudera, Databricks, Confluent build billion-dollar businesses on Apache projects (Hadoop, Spark, Kafka) -- ASF receives none of that revenue.
- The "value" to ASF is in volunteer contributions and sponsorship goodwill.

#### Tax Implications

- Fully tax-exempt as 501(c)(3).
- Donations are tax-deductible for donors.
- No UBIT because ASF does not engage in commercial activities.
- Sponsorship income structured as qualified sponsorship payments (not advertising), avoiding UBIT.

#### Grant Eligibility

- Fully eligible for foundation grants, government grants, and tax-deductible individual donations.
- In practice, ASF relies more on corporate sponsorships than grants.

#### IP Handling

- **Critical model**: All IP is assigned to ASF via Contributor License Agreements (ICLAs and CCLAs).
- Apache License 2.0 (permissive): allows anyone to use, modify, and distribute commercially without paying ASF.
- Explicit patent grant from contributors protects downstream users.
- ASF owns trademarks for project names.
- This IP model is why companies can build commercial products on Apache software freely.

#### Setup Cost and Timeline

- Same as any 501(c)(3): ~$3,000-11,000, 8-14 months.
- But reaching ASF-like scale requires years of community building.

#### Ongoing Compliance

- **Low to moderate** for the legal entity itself.
- Heavy governance overhead for managing 320+ projects, PMCs, and community processes.
- Annual 990 filing.
- Must maintain charitable purpose -- the "education" and "scientific" exemption categories are key.

#### Examples Using This Model

- Apache Software Foundation
- Python Software Foundation (501(c)(3) + some 501(c)(6) characteristics)
- FreeBSD Foundation
- GNOME Foundation
- Software Freedom Conservancy

#### Pros for Solo Practitioner

- Strong grant eligibility and donor appeal.
- Tax-deductible donations attract individual supporters.
- Clear charitable mission aligns with academic/research work.
- Minimal UBIT exposure (no commercial sales).
- High credibility in open-source community.

#### Cons for Solo Practitioner

- **Cannot sell commercial products or SaaS through the nonprofit.** All commercial value accrues to third parties.
- Revenue is limited to donations/sponsorships -- typically small.
- Does not solve the "how do I make money from my work" problem.
- Requires building a real community (cannot be solo).
- IRS has been increasingly skeptical of OSS 501(c)(3) applications -- must demonstrate clear educational/scientific purpose beyond "making software."
- Recent IRS denials of OSS 501(c)(3) applications (PLR 201717048, PLR 202530014) show this path is getting harder.

---

## 4. NumFOCUS Model

### Fiscal Sponsor for Scientific Open Source

#### Legal Structure

```
NumFOCUS [501(c)(3), Texas]
  |
  |-- Comprehensive Model (Model A) sponsored projects:
  |     NumPy, pandas, Matplotlib, Jupyter, Julia, etc.
  |     (Projects are legally part of NumFOCUS)
  |
  |-- Grantor-Grantee Model (Model C) sponsored projects:
  |     (Projects are separate legal entities receiving grants)
  |
  |-- Affiliated Projects:
  |     Conda, Dask, Xarray, etc.
  |     (Looser association, not fiscally sponsored)
```

- **NumFOCUS** is the 501(c)(3) umbrella organization.
- **Comprehensive Model** (Model A): Project is legally part of NumFOCUS. NumFOCUS handles all legal, financial, and fiduciary responsibilities. Contributors are effectively volunteers of NumFOCUS.
- **Grantor-Grantee Model** (Model C): Project is a separate legal entity. NumFOCUS provides a channel for tax-deductible donations and grant management. Project retains more independence.
- Each project has a 3-5 person "fiscal oversight team" that approves spending.

#### How Commercial Revenue Flows

- Donations to sponsored projects flow through NumFOCUS (tax-deductible).
- NumFOCUS takes a percentage (typically 10-15%) for administrative overhead.
- Commercial companies built on sponsored projects are **completely separate entities**:
  - Anaconda, Inc. (for-profit) uses NumPy/pandas but is not part of NumFOCUS.
  - Anaconda contributes back through its "Anaconda Dividend Program" (voluntary).
  - Two Sigma sponsors pandas/Jupyter development through NumFOCUS.
- **No revenue sharing** between commercial companies and NumFOCUS beyond voluntary sponsorship/donation.

#### Tax Implications

- Donations to NumFOCUS-sponsored projects are tax-deductible (501(c)(3) pass-through).
- Projects under Comprehensive Model cannot independently engage in commercial activities.
- NumFOCUS itself does not sell products.

#### Grant Eligibility

- Excellent. NumFOCUS can receive foundation grants, government grants (NSF, NIH, etc.), and tax-deductible individual donations on behalf of any sponsored project.
- This is the primary value proposition of fiscal sponsorship.

#### IP Handling

- Under Comprehensive Model: IP effectively belongs to NumFOCUS, though projects retain practical control.
- Open-source licenses (BSD, MIT, Apache 2.0) mean commercial use is unrestricted regardless of IP ownership.
- Trademarks for project names are typically held by NumFOCUS for comprehensive projects.

#### Setup Cost and Timeline

- Joining NumFOCUS as a sponsored project: application process, typically 1-3 months.
- No cost to join (NumFOCUS takes overhead from incoming donations/grants).
- NumFOCUS handles all tax/legal infrastructure.
- **But**: you don't own the legal entity. You're a project within someone else's nonprofit.

#### Ongoing Compliance

- **Low for the project.** NumFOCUS handles tax filings, financial reporting, and legal compliance.
- Project must comply with NumFOCUS policies and fiscal oversight team approval for spending.
- Annual reporting to NumFOCUS on activities and finances.

#### Examples Using This Model

- NumPy (via NumFOCUS, while Anaconda is separate for-profit)
- pandas (via NumFOCUS, while Two Sigma sponsors commercially)
- Jupyter (via NumFOCUS)
- Julia (via NumFOCUS)
- Matplotlib, SciPy, scikit-learn, etc.

#### Pros for Solo Practitioner

- **Fastest path to grant eligibility** -- no need to form your own 501(c)(3).
- Zero setup cost for tax-exempt infrastructure.
- Can receive tax-deductible donations immediately.
- Legitimacy through association with established nonprofit.
- Focus on work, not paperwork.

#### Cons for Solo Practitioner

- You do not control the legal entity.
- NumFOCUS takes an overhead cut (10-15%).
- Your commercial activities must be separate (need a separate LLC/Corp).
- NumFOCUS may not accept projects that don't fit their scientific computing focus.
- Limited autonomy -- subject to NumFOCUS governance decisions.
- **Does not solve the commercial revenue problem** -- you still need a separate entity for SaaS/products.

---

## 5. Creative Commons Model

### Nonprofit Creating Tools Used Commercially by Others

#### Legal Structure

```
Creative Commons Corporation [501(c)(3), Massachusetts]
  |
  |-- CC Global Network (100+ chapters/affiliates worldwide)
  |-- No for-profit subsidiary
  |-- No commercial products sold
```

- Single 501(c)(3) entity.
- International affiliate network (not subsidiaries -- independent organizations).
- Creates legal tools (licenses) provided entirely for free.

#### How Commercial Revenue Flows

- **2024 revenue: $2.4M** (down from $9.9M in 2021).
- Revenue breakdown:
  - Contributions/donations: 82% ($2.0M)
  - Program services: 12% ($291K)
  - Investment income: 6% ($138K)
- CC does not charge for its licenses or tools.
- Major funders include Google, Hewlett Foundation, and other large foundations/corporations.
- Revenue is volatile -- heavily dependent on large grants.
- Net assets: $9.2M (provides runway but shrinking from $12.3M peak).

#### Tax Implications

- Fully tax-exempt. Donations are tax-deductible.
- Program service revenue (training, consulting) is related to exempt purpose, so no UBIT.
- No commercial products = no UBIT concerns.

#### Grant Eligibility

- Full access to foundation grants, government grants, individual donations.

#### IP Handling

- CC licenses are the product -- they're legal instruments, not software.
- CC retains copyright on the license text itself.
- CC licenses, once applied by a creator, are irrevocable.
- CC does not own or control any content licensed under CC licenses.

#### Setup Cost and Timeline

- N/A (this model is just a standard 501(c)(3)).

#### Ongoing Compliance

- Standard 501(c)(3) compliance.

#### Pros for Solo Practitioner

- If your primary output is freely available tools/standards, this model works.
- Strong donor/grant appeal for "public good" framing.

#### Cons for Solo Practitioner

- **No commercial revenue generation.** Revenue comes entirely from donations and grants.
- Extremely volatile revenue (CC went from $940K to $9.9M to $2.4M in 4 years).
- Cannot sell SaaS, products, or commercial services through the nonprofit.
- Only works if your mission is creating free tools, not commercial products.
- **Not viable for ORGANVM's commercial SaaS needs.**

---

## 6. Blender Foundation Model

### Foundation + Working Company + Commercial Studio

#### Legal Structure

```
Blender Foundation [Dutch stichting (public benefit foundation)]
  |
  |-- Blender Institute BV [Dutch BV (private company)]
  |     |-- 24 employees working on Blender software
  |     |-- Acts as "working company" of Foundation
  |
  |-- Blender Studio BV [Dutch BV, split from Institute in 2020]
        |-- Subscription platform for training/production content
        |-- Creates open movies to test Blender in production
```

- **Stichting** (Dutch foundation): No shareholders, no members, no profit distribution. Governed by board.
- **BV** (Besloten Vennootschap): Dutch equivalent of LLC/Ltd. Can employ staff, enter contracts.
- Foundation owns the Institute; Institute acts as the Foundation's operational arm.
- Studio is a separate commercial entity producing content.

#### How Commercial Revenue Flows

- **Blender Development Fund (2024): EUR 2.14M** (+21% YoY)
  - Individual donations: EUR 612K (29%)
  - Corporate memberships: EUR 355K (17%)
  - Remainder from other corporate tiers
- **Corporate membership tiers**:
  - Titanium: custom (Epic Games, NVIDIA, AMD, Qualcomm)
  - Platinum: EUR 120K/year
  - Patron: EUR 30K/year
  - Corporate Gold/Silver/Bronze: lower tiers
- **Blender Studio**: Subscription revenue from training content, courses, add-ons.
- All Blender software remains GPL -- completely free. Revenue supports development, not restricts access.

#### Tax Implications

- Dutch stichting (foundation) has favorable tax treatment for public benefit activities.
- BV subsidiaries are taxable entities (Dutch corporate tax).
- Not directly comparable to US tax-exempt structures, but the concept translates.

#### Grant Eligibility

- Dutch foundations can receive grants from European funders, corporate sponsors, etc.
- Not eligible for US 501(c)(3) grants unless separately registered.

#### IP Handling

- Blender Foundation holds copyright and trademarks.
- All code is GPL-licensed (copyleft -- derivatives must also be open source).
- Blender Studio content is CC-BY licensed (free to use, including commercially).
- Contributors retain copyright but license to Foundation.

#### Pros for Solo Practitioner

- The Foundation + Working Company model allows employing staff while maintaining nonprofit mission.
- Subscription studio model generates recurring commercial revenue.
- Corporate sponsorship tiers provide scalable funding.
- Clean separation between free software (Foundation) and commercial content (Studio).

#### Cons for Solo Practitioner

- Dutch legal structure not directly applicable to US (would need adaptation).
- Need substantial corporate sponsor network to fund development.
- Requires established user base before corporate sponsors will pay.
- More complex multi-entity structure.

---

## 7. Processing Foundation Model

### Nonprofit for Creative Coding (Grant-Funded)

#### Legal Structure

```
Processing Foundation [501(c)(3), established 2012]
  |
  |-- Processing (Java-based creative coding tool)
  |-- p5.js (JavaScript library)
  |-- Processing.py, Processing for Android
  |-- Fellowship/grant programs
  |-- No for-profit subsidiary
```

#### How Commercial Revenue Flows

- **2024 revenue: $649K** (2021 spike to $10.9M was a one-time large gift).
- Revenue breakdown (2024):
  - Contributions: 72% ($464K)
  - Investment income: 28% ($184K)
- The Foundation does not sell products or services.
- Funded primarily by grants (Sovereign Tech Fund: EUR 200K in 2023) and donations.
- Offers paid fellowships ($10K stipend) and developer grants.
- **No commercial arm.** All tools are free.

#### Tax Implications

- Standard 501(c)(3). Donations tax-deductible.
- No UBIT (no commercial activity).
- Heavy reliance on investment income from endowment (built from 2021 gift).

#### Grant Eligibility

- Full access to foundation grants, government funding, individual donations.
- Successfully received Sovereign Tech Fund (European government) funding.

#### IP Handling

- Open-source licenses (LGPL for Processing, Apache 2.0 for p5.js).
- Foundation holds trademarks.
- Contributors grant licenses via contributor agreements.

#### Pros for Solo Practitioner

- Very relevant model for creative coding / generative art work.
- Fellowship and grant programs fund individuals directly.
- Small scale is viable ($50K-$650K annual budgets worked for years).
- Aligns well with ORGANVM's creative/educational mission.

#### Cons for Solo Practitioner

- **Zero commercial revenue.** Entirely grant/donation dependent.
- Revenue extremely volatile ($11M one year, $650K the next).
- Cannot sell SaaS or commercial products through this structure.
- Does not solve the Organ III (commercial products) funding need.

---

## 8. L3C Model

### Low-Profit Limited Liability Company

#### Legal Structure

```
L3C (Low-Profit Limited Liability Company)
  |
  |-- Single entity, LLC variant
  |-- Chartered in qualifying state
  |-- Must have charitable/educational purpose as PRIMARY goal
  |-- Profit permitted as SECONDARY goal
  |-- Cannot have significant purpose of income production
  |-- Cannot have political purposes
```

#### How Commercial Revenue Flows

- L3C can earn revenue from selling products/services.
- Revenue goes to the single entity.
- Can distribute profits to members, but profit cannot be the primary purpose.
- Uniquely designed to receive Program-Related Investments (PRIs) from private foundations.
- PRIs: Foundations invest in L3C (loans or equity) rather than making grants. Counts toward foundation's 5% annual distribution requirement.

#### Tax Implications

- **Not tax-exempt.** L3C is a for-profit entity.
- Taxed as a partnership (multi-member) or disregarded entity (single-member) by default.
- Can elect S-Corp or C-Corp taxation.
- Donations to L3C are **not** tax-deductible.
- However, PRI investments from foundations receive favorable treatment for the foundation.

#### Grant Eligibility

- **Cannot** receive traditional charitable grants (not a 501(c)(3)).
- **Can** receive PRIs from private foundations (this is the whole point of L3C).
- Can receive social enterprise grants and impact investment.
- Can apply for government contracts.

#### IP Handling

- Standard LLC IP ownership. Entity owns what it creates (or per operating agreement).
- No special IP regime.

#### Setup Cost and Timeline

- Formation fee: $50-200 (state filing, same as LLC).
- Operating agreement drafting: $1,000-5,000 with attorney.
- **Only available in ~12 states**: Vermont, Illinois, Louisiana, Maine, Michigan, Missouri, North Dakota, Rhode Island, Utah, Wyoming, Puerto Rico, plus Crow/Oglala Sioux tribal jurisdictions.
- Timeline: Days to weeks (no IRS application needed).

#### Ongoing Compliance

- **Low.** Same as any LLC -- annual state filings, partnership or corporate tax returns.
- No IRS annual information return (no 990).
- Must maintain charitable/educational primary purpose (self-enforced; no federal oversight).

#### Examples Using This Model

- Relatively few notable examples. The L3C form has not gained widespread adoption.
- Most social enterprises have gravitated toward B-Corps or PBCs instead.
- Some community development projects and social ventures use L3C.

#### Pros for Solo Practitioner

- **Fastest formation** -- no IRS approval needed.
- Can sell products AND pursue charitable mission.
- Can receive PRI investments from foundations.
- Low compliance burden.
- Single entity simplicity.

#### Cons for Solo Practitioner

- **Not tax-exempt.** Pays regular taxes.
- **No tax-deductible donations.** Donors get no benefit.
- Limited geographic availability (12 states).
- L3C status provides no actual legal enforcement of mission -- it is self-declared.
- IRS has never issued regulations specifically confirming L3C = automatic PRI qualification.
- Few examples of successful L3Cs at scale.
- May not be recognized or understood by funders.
- **Weak brand recognition** compared to B-Corp or nonprofit.

---

## 9. B-Corp / Benefit Corporation

### For-Profit with Certified Social Mission

#### Legal Structure

```
Two distinct (often confused) things:

1. Benefit Corporation [STATE LEGAL STRUCTURE]
   |-- For-profit corporation with statutory public benefit purpose
   |-- Formed under state benefit corporation statute
   |-- Available in 40+ states + DC

2. Certified B Corporation [PRIVATE CERTIFICATION by B Lab]
   |-- Any legal entity type
   |-- Must score 80+ on B Impact Assessment (out of 200)
   |-- Recertified every 3 years
   |-- Annual fee: $1,000-$50,000+ based on revenue
```

- These are **not the same thing.** One is a legal structure, the other is a certification.
- Delaware requires B Corp-certified companies to convert to Benefit Corporation (or amend operating agreement).
- A company can be both, either, or neither.

#### How Commercial Revenue Flows

- Standard for-profit revenue. No restrictions on commercial activity.
- Must balance profit with stated public benefit, but no revenue earmarking required.
- Can issue equity, pay dividends, attract venture capital.

#### Tax Implications

- **Fully taxable** as a regular corporation. No tax exemption.
- No special tax treatment for benefit corporations.
- Benefit Corporation status does not affect tax obligations at all.
- Donations to benefit corporations are **not** tax-deductible.

#### Grant Eligibility

- **Cannot** receive most foundation grants or tax-deductible donations.
- Some cities/governments offer incentive grants for B Corps.
- Can receive impact investment, social enterprise funding.
- Some foundations will make PRIs to Benefit Corporations.

#### IP Handling

- Standard corporate IP ownership. No special regime.

#### Setup Cost and Timeline

- **Benefit Corporation formation**: Same as regular corporation ($50-300 state filing) + benefit purpose in charter.
- **B Corp certification**: Application process (6-12 months), assessment, verification.
  - Annual fees: $1,000 (revenue <$150K) to $50,000+ (revenue >$1B).
  - Must score 80+ on B Impact Assessment.

#### Ongoing Compliance

- **Benefit Corporation**: Must publish periodic benefit report (biennial in Delaware, varies by state). Directors must balance stakeholder interests.
- **B Corp certification**: Recertify every 3 years. Annual fee. Updated standards from 2026 onward (mandatory baseline requirements replacing points-based system).

#### Examples Using This Model

- Patagonia (Benefit Corporation)
- Kickstarter (PBC)
- Ben & Jerry's (B Corp certified)
- Warby Parker (PBC, publicly traded)
- Allbirds (PBC, publicly traded)

#### Pros for Solo Practitioner

- Full commercial flexibility -- can sell anything.
- Can attract investors and issue equity.
- Mission protection: directors legally required to consider stakeholders beyond shareholders.
- Growing brand recognition and consumer/investor appeal.
- Can convert existing LLC or C-Corp to Benefit Corporation.
- Fast setup (days to weeks).

#### Cons for Solo Practitioner

- **No tax exemption.** Pays full corporate taxes.
- **No tax-deductible donations.** Cannot attract philanthropic funding effectively.
- B Corp certification has ongoing costs and compliance burden.
- Benefit Corporation reporting requirements (though light).
- Does not help with grant funding for research/academic work.
- Mission protection is legally weak -- directors have broad discretion under "balancing" standard.

---

## 10. Public Benefit Corporation (PBC)

### For-Profit with Statutory Public Benefit (Delaware Model)

#### Legal Structure

```
Public Benefit Corporation [Delaware DGCL Subchapter XV]
  |
  |-- For-profit corporation
  |-- Certificate of Incorporation must state specific public benefit(s)
  |-- Name may include "P.B.C." or "PBC"
  |-- Board balances: stockholder interests + affected parties + stated benefit
```

- Delaware PBC is the most established form (since 2013).
- Other states have similar statutes (often called "Benefit Corporation").
- PBC is a subset of Benefit Corporation -- specifically Delaware's version.

#### The OpenAI Case Study

- **Original structure (2015)**: OpenAI Inc. [501(c)(3) nonprofit] controlled OpenAI LP [capped-profit limited partnership].
- **2024 restructuring attempt**: Planned to convert for-profit arm to PBC and reduce nonprofit's control to minority stake. SoftBank invested $40B conditional on removing profit cap.
- **Backlash and reversal (May 2025)**: Abandoned plan to remove nonprofit control. Instead: for-profit became PBC but nonprofit retained controlling stake.
- **Final structure (October 2025)**: OpenAI PBC controlled by OpenAI Foundation (nonprofit), which holds $130B stake.

**Lesson for ORGANVM**: The OpenAI saga shows that nonprofit-controls-PBC can work, but pressure from investors to weaken mission control is intense. The structure only holds if the founder has genuine commitment to mission primacy.

#### How Commercial Revenue Flows

- Standard for-profit corporation. Full commercial activity.
- Can issue stock, attract VC, pay dividends (subject to fiduciary balancing).
- No revenue restrictions beyond standard corporate law.

#### Tax Implications

- **Fully taxable.** Same as regular C-Corp.
- No tax exemption. No tax-deductible donations.

#### Grant Eligibility

- Same as Benefit Corporation -- limited. Some PRIs possible.
- If controlled by a nonprofit (as in OpenAI model), the nonprofit can receive grants.

#### IP Handling

- Standard corporate IP ownership.

#### Setup Cost and Timeline

- Delaware incorporation: ~$90-300 filing fee.
- Must specify public benefit(s) in certificate.
- Legal counsel for charter drafting: $1,000-5,000.
- No IRS approval needed.
- Timeline: Days to a few weeks.

#### Ongoing Compliance

- Board must balance three interests (stockholders, affected parties, public benefit) in every decision.
- Biennial benefit report to stockholders (optional under 2020 amendment unless charter requires it).
- Stockholder derivative suits require 2%+ ownership.
- Otherwise same as regular C-Corp compliance.

#### Pros for Solo Practitioner

- Maximum commercial flexibility with mission protection.
- Can be controlled by a separate nonprofit (OpenAI model).
- Fast to set up.
- Well-understood by investors, especially in tech.
- Growing legal precedent in Delaware courts.

#### Cons for Solo Practitioner

- No tax benefits.
- "Mission protection" is legally soft -- directors have wide discretion.
- If using nonprofit-controls-PBC model (like OpenAI), you need both entities.
- Investor pressure to weaken mission over time (the OpenAI lesson).

---

## 11. Cooperative Model

### Worker or Platform Cooperative

#### Legal Structure

```
Worker Cooperative
  |
  |-- Can be formed as:
  |     |-- Cooperative Corporation (where statutes exist)
  |     |-- LLC with cooperative operating agreement
  |     |-- Standard corporation with cooperative bylaws
  |
  |-- One member, one vote (regardless of capital contribution)
  |-- Profits distributed based on patronage (work contributed), not investment
  |-- Democratic governance
```

#### How Commercial Revenue Flows

- Cooperative sells products/services like any business.
- Profits distributed to worker-owners based on patronage (hours worked, revenue generated).
- Can retain earnings for growth.
- Can accept outside investment (though this is structurally unusual for cooperatives).

#### Tax Implications

- Cooperatives get special tax treatment under **Subchapter T** of the Internal Revenue Code.
- Patronage dividends paid to members are deductible by the cooperative (like wages).
- This effectively means cooperatives are taxed at the member level, not entity level (similar to S-Corp pass-through), but only on patronage income.
- Non-patronage income is taxed at the entity level.

#### Grant Eligibility

- **Not** eligible for charitable grants (not a 501(c)(3)).
- **Can** receive USDA cooperative development grants.
- **Can** receive state/local economic development funding.
- Growing pool of cooperative-specific funding (The Working World, Seed Commons, etc.).
- 2025 declared UN International Year of Cooperatives -- may increase funding.

#### IP Handling

- Cooperative owns IP created by members (per operating agreement).
- Can use any licensing model (open source, proprietary, or hybrid).
- Members typically assign IP to cooperative.

#### Setup Cost and Timeline

- State filing: $50-200.
- Legal counsel for operating agreement/bylaws: $2,000-10,000.
- Cooperative development assistance available from organizations like DAWI, Democracy at Work Institute.
- Timeline: Weeks to months for formation.

#### Examples in Tech

- **Stocksy United**: Stock photography platform cooperative. $7.9M in 2015 sales.
- **The Drivers Cooperative**: NYC ride-hailing. 7,500 members, $4M+ revenue.
- **Resonate**: Music streaming cooperative.
- **CoTech**: UK federation of tech worker cooperatives.
- **FACTTIC**: Argentine tech worker cooperative federation.
- **Patio**: Global network of 80+ tech cooperatives, 1,500 cooperators in 24 countries.

#### Pros for Solo Practitioner

- Democratic governance aligns with ethical/empowerment mission.
- Subchapter T tax benefits.
- Growing ecosystem of cooperative support organizations.
- Strong community/solidarity appeal.
- Can sell products and services commercially.

#### Cons for Solo Practitioner

- **Requires multiple members** -- cannot be solo. One-person cooperative is an oxymoron.
- One-member-one-vote means founder loses control as membership grows.
- Difficult to attract venture capital (investors don't get voting control).
- Limited exit options (cannot sell equity in traditional sense).
- No tax-deductible donations. No grant eligibility for research.
- Not well-suited for academic/research activities.
- Scale is hard -- most tech cooperatives remain small.

---

## 12. Fiscal Sponsorship + Separate LLC

### Nonproft Project Under Fiscal Sponsor + Independent Commercial Entity

#### Legal Structure

```
Fiscal Sponsor (e.g., NumFOCUS, Open Collective Foundation, Hack Club)
  |                                              [501(c)(3)]
  |
  |-- Your Project (fiscally sponsored)
  |     |-- Receives tax-deductible donations
  |     |-- Can receive grants
  |     |-- Governed by sponsor's policies
  |
  |
You (Individual)
  |
  |-- Your LLC or C-Corp [separate for-profit entity]
        |-- Sells commercial products, SaaS
        |-- Pays taxes on profits
        |-- Arm's-length relationship with sponsored project
```

- Two completely separate relationships:
  1. Your charitable/research/educational project is a fiscally sponsored project of a 501(c)(3).
  2. Your commercial activities happen through a separate for-profit entity you own.

#### How Commercial Revenue Flows

- **Charitable donations** go to fiscal sponsor (tax-deductible to donors) and are disbursed for your project's approved activities.
- **Commercial revenue** goes to your LLC/Corp. You pay regular business taxes.
- **Key legal requirement**: Arms-length separation. The LLC cannot siphon nonprofit funds, and the nonprofit cannot primarily serve the LLC's commercial interests.
- LLC can pay for services from the project (at fair market value) or sponsor the project (like any corporate sponsor).
- LLC can license open-source software produced by the project and build commercial products on it.

#### Tax Implications

- **Sponsored project**: Tax-deductible donations, exempt from tax (through sponsor's exemption).
- **LLC/Corp**: Fully taxable. Standard business taxation.
- **Critical**: Must maintain genuine independence. IRS will scrutinize if the nonprofit project appears to exist primarily to benefit the for-profit entity. The charitable purpose must be real and independently justified.

#### Grant Eligibility

- Sponsored project can receive grants through the fiscal sponsor.
- LLC cannot receive charitable grants.
- This gives you access to both grant funding (for research/education) and commercial revenue (for products/SaaS).

#### IP Handling

- **Most flexible option.** Several approaches:
  1. Open-source code produced under sponsored project -- anyone (including your LLC) can use it.
  2. LLC creates proprietary extensions/services on top of open-source core.
  3. Trademarks can be held by either entity (or split).
  4. Research papers/educational materials produced under sponsorship -- public goods.
  5. Commercial products (SaaS, tools) produced by LLC -- proprietary if desired.

#### Setup Cost and Timeline

- **Fiscal sponsorship**: Apply to a fiscal sponsor (1-3 months), typically free to join (sponsor takes 5-15% of incoming funds).
- **LLC formation**: $50-200 state filing + operating agreement ($500-2,000 with attorney).
- **Total**: $550-2,200 + 1-3 months.
- **No IRS approval needed** for either piece (fiscal sponsor already has 501(c)(3) status).

#### Ongoing Compliance

- **Moderate.** Two relationships to maintain:
  1. Fiscal sponsorship: Comply with sponsor's policies, report on project activities, submit expense reports for approval.
  2. LLC: Standard business tax filings, annual state registration.
- Must maintain genuine separation between nonprofit and for-profit activities.
- Must not use sponsored project funds for commercial purposes.
- Documentation of arm's-length transactions is important.

#### Fiscal Sponsor Options (for ORGANVM's Profile)

| Sponsor | Focus | Overhead | Model |
|---------|-------|----------|-------|
| NumFOCUS | Scientific computing | 10-15% | A or C |
| Open Collective Foundation | General open source | 10% | A |
| Software Freedom Conservancy | Free software | negotiable | A |
| Hack Club | Youth/education | varies | varies |
| Fractured Atlas | Arts/creative | 7% | A |
| Code for Science & Society | Research software | varies | varies |
| Allied Media Projects | Social justice tech | varies | A |

**For ORGANVM**: Fractured Atlas (arts focus) or Code for Science & Society (research software) could be strong matches given the generative art + academic research profile.

#### Pros for Solo Practitioner

- **Best of both worlds**: Grant/donation access (via fiscal sponsor) AND commercial revenue (via LLC).
- **Fastest to implement**: No IRS application. Can be operational in weeks.
- **Lowest cost**: Minimal formation costs.
- **Maximum flexibility**: Research/education through sponsored project; SaaS/products through LLC.
- **Scales gracefully**: Can later convert to your own 501(c)(3) if project grows large enough.
- **Solo-friendly**: LLC can be single-member. Fiscal sponsor handles nonprofit governance.
- **IP flexibility**: Open-core model (open source base + commercial extensions) works naturally.

#### Cons for Solo Practitioner

- Fiscal sponsor takes a cut (5-15%).
- Less control over nonprofit activities (subject to sponsor's policies).
- Must maintain genuine separation -- cannot use nonprofit as a funnel for commercial profits.
- If relationship sours with fiscal sponsor, project migration can be disruptive.
- Less institutional credibility than having your own foundation.
- Some funders prefer granting directly to dedicated organizations, not fiscally sponsored projects.

---

## 13. Comparative Analysis for ORGANVM

### ORGANVM Requirements Matrix

ORGANVM needs a structure that supports:

1. **Academic research** (Organ I: Theoria) -- needs grant eligibility
2. **Generative art / creative coding** (Organ II: Poiesis) -- needs arts funding + commercial revenue
3. **Commercial SaaS / developer tools** (Organ III: Ergon) -- needs commercial revenue, possibly investor funding
4. **Governance tooling** (Organ IV: Taxis) -- could be either nonprofit or commercial
5. **Publishing / discourse** (Organ V: Logos) -- could be nonprofit
6. **Community / education** (Organ VI: Koinonia) -- strongly nonprofit
7. **Distribution** (Organ VII: Kerygma) -- operational/commercial
8. **Meta-governance** (Meta) -- institutional backbone

### Scoring Matrix

| Model | Grant Access | Commercial Revenue | Solo-Friendly | Setup Speed | IP Flexibility | Scale Path | Compliance Load | Total |
|-------|-------------|-------------------|---------------|-------------|----------------|------------|-----------------|-------|
| Mozilla (501c3+Corp) | 5 | 5 | 2 | 2 | 4 | 5 | 2 | 25 |
| Linux Foundation (501c6) | 2 | 5 | 1 | 3 | 4 | 4 | 3 | 22 |
| Apache (501c3 pure) | 5 | 1 | 2 | 2 | 3 | 3 | 3 | 19 |
| NumFOCUS (fiscal sponsor) | 5 | 1 | 4 | 5 | 3 | 3 | 5 | 26 |
| Creative Commons | 5 | 1 | 2 | 2 | 3 | 2 | 3 | 18 |
| Blender (Foundation+Co) | 4 | 4 | 2 | 2 | 4 | 4 | 2 | 22 |
| Processing Foundation | 5 | 1 | 2 | 2 | 3 | 2 | 3 | 18 |
| L3C | 2 | 4 | 5 | 5 | 5 | 3 | 5 | 29 |
| B-Corp/Benefit Corp | 1 | 5 | 5 | 5 | 5 | 4 | 4 | 29 |
| PBC (Delaware) | 1 | 5 | 5 | 5 | 5 | 5 | 4 | 30 |
| Cooperative | 1 | 4 | 1 | 4 | 4 | 2 | 3 | 19 |
| **Fiscal Sponsor + LLC** | **5** | **5** | **5** | **5** | **5** | **4** | **4** | **33** |

Scale: 1 (worst) to 5 (best) for ORGANVM's specific needs.

---

## 14. Recommended Path

### Phase 1: Immediate (Weeks 1-4) -- Fiscal Sponsorship + LLC

**This is the recommended starting structure for ORGANVM.**

```
Fiscal Sponsor (Fractured Atlas or Code for Science & Society)
  |
  |-- ORGANVM Research & Education Project
  |     |-- Organ I (Theoria): Academic research
  |     |-- Organ II (Poiesis): Generative art, creative coding tools
  |     |-- Organ VI (Koinonia): Community, education
  |     |-- Open-source governance tools (Organ IV, open-source portion)
  |     |-- Receives grants, donations (tax-deductible)
  |
You
  |
  |-- ORGANVM LLC (or ORGANVM PBC) [Delaware or home state]
        |-- Organ III (Ergon): Commercial SaaS, developer tools
        |-- Organ V (Logos): Publishing (if revenue-generating)
        |-- Organ VII (Kerygma): Distribution services
        |-- Commercial training, consulting, support
        |-- Pays taxes, can attract investment
```

**Why this works:**
- Operational in 2-4 weeks (no IRS approval needed).
- Total cost: under $2,000.
- Immediately eligible for grants and tax-deductible donations through fiscal sponsor.
- Immediately able to sell commercial products through LLC.
- Solo-friendly: LLC is single-member, fiscal sponsor handles nonprofit governance.
- IP clean: open-source core (sponsored project) + commercial extensions (LLC).

### Phase 2: Growth (Year 1-3) -- Consider PBC Conversion for LLC

If commercial revenue grows, convert LLC to **Delaware PBC** to embed mission permanently:

```
Fiscal Sponsor
  |
  |-- ORGANVM Research Project
  |
You
  |
  |-- ORGANVM PBC [Delaware]
        |-- All commercial activities
        |-- Public benefit: "advancing ethical automation and creative technology"
```

### Phase 3: Institutional Scale (Year 3+) -- Own 501(c)(3) Foundation

When the operation is large enough to justify the overhead:

```
ORGANVM Foundation [501(c)(3)]  <-- your own nonprofit
  |
  |-- Owns/controls --> ORGANVM PBC [Delaware, for-profit]
  |
  |-- Research programs (Organ I)
  |-- Arts programs (Organ II)
  |-- Education/community (Organ VI)
  |-- Governance standards (Organ IV, open-source)
  |
  ORGANVM PBC
  |-- Commercial SaaS (Organ III)
  |-- Publishing platform (Organ V)
  |-- Distribution services (Organ VII)
```

This is the full **Mozilla model** adapted for ORGANVM. The Foundation holds the mission; the PBC generates revenue.

### Key Actions Now

1. **Choose a fiscal sponsor.** Fractured Atlas (arts, 7% overhead) is strong for Organ II focus. Code for Science & Society is strong for Organ I focus. Apply to both and evaluate.
2. **Form an LLC** in your home state or Delaware. Cost: ~$200-500. Time: days.
3. **Separate your repos** into "open-source/research" (sponsored project) and "commercial" (LLC) categories. Most of the 117 repos are probably open-source/research.
4. **Draft an IP policy**: What's open source (Apache 2.0 or MIT) and what's proprietary? Open-core model: open-source base with commercial SaaS layer.
5. **Open a bank account** for the LLC. Fiscal sponsor handles nonprofit banking.

### What NOT to Do

- **Do not** try to form your own 501(c)(3) right now. IRS is scrutinizing OSS nonprofits, processing takes 6-10 months, and you need 3 unrelated board members.
- **Do not** use an L3C -- too obscure, limited recognition, no real tax benefits.
- **Do not** form a cooperative -- requires multiple worker-owners, contradicts solo practitioner needs.
- **Do not** try the Linux Foundation model (501(c)(6)) -- requires meaningful membership base and does not support grant funding.

---

## Sources

### Mozilla Model
- [Mozilla Foundation - Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Foundation)
- [Mozilla Corporation - Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Corporation)
- [Mozilla Organizations](https://www.mozilla.org/en-US/about/governance/organizations/)
- [Mozilla Foundation - ProPublica Nonprofit Explorer](https://projects.propublica.org/nonprofits/organizations/200097189)
- [State of Mozilla 2025](https://stateof.mozilla.org/)
- [Mozilla Foundation 2023 Financial Statements](https://assets.mozilla.net/annualreport/2024/mozilla-fdn-2023-fs-final-short-1209.pdf)

### Linux Foundation Model
- [Linux Foundation Bylaws](https://www.linuxfoundation.org/legal/bylaws)
- [Linux Foundation - ProPublica](https://projects.propublica.org/nonprofits/organizations/460503801)
- [About the Linux Foundation](https://www.linuxfoundation.org/about)
- [Linux Foundation expects $300M+ revenue - Phoronix](https://www.phoronix.com/news/Linux-Foundation-2025-Report)
- [501(c)(6) Guide - Foundation Group](https://www.501c3.org/what-is-a-501c6/)
- [501(c)(6) Tax Facts - Nonprofit Accounting Basics](https://www.nonprofitaccountingbasics.org/federal-tax-issues/tax-facts-section-501c6-trade-associations)

### Apache Software Foundation Model
- [Apache Licenses](https://www.apache.org/licenses/)
- [Apache Software Foundation - Wikipedia](https://en.wikipedia.org/wiki/The_Apache_Software_Foundation)
- [ASF Governance Primer](https://www.apache.org/foundation/governance/)
- [ASF - Choose A Foundation](http://chooseafoundation.com/foundations/apache)
- [ASF 2023 Annual Report](https://news.apache.org/foundation/entry/apache-software-foundation-releases-annual-report-for-2023-fiscal-year)

### NumFOCUS Model
- [NumFOCUS Fiscal Sponsorship - GitHub](https://github.com/numfocus/fiscal-sponsorship)
- [NumFOCUS Projects Overview](https://numfocus.org/projects-overview)
- [NumFOCUS Fiscal Sponsorship Background](https://github.com/numfocus/fiscal-sponsorship/blob/master/background.md)
- [Anaconda Partnership with NumFOCUS](https://numfocus.org/corporate-sponsors/anaconda-announces-multi-year-partnership-with-numfocus)
- [Working with a Fiscal Sponsor - Code for Science & Society](https://www.codeforsociety.org/resources/working-with-a-fiscal-sponsor)

### Creative Commons Model
- [Creative Commons - Wikipedia](https://en.wikipedia.org/wiki/Creative_Commons)
- [Creative Commons - What We Do](https://creativecommons.org/about/)
- [Creative Commons - ProPublica](https://projects.propublica.org/nonprofits/organizations/43585301)

### Blender Foundation Model
- [Blender Foundation](https://www.blender.org/about/foundation/)
- [Blender Institute](https://www.blender.org/about/institute/)
- [Blender Foundation - Wikipedia](https://en.wikipedia.org/wiki/Blender_Foundation)
- [Blender Development Fund](https://fund.blender.org/)
- [Blender 2023 Annual Report](https://download.blender.org/foundation/Blender-Foundation-Annual-Report-2023.pdf)

### Processing Foundation Model
- [Processing Foundation](https://processingfoundation.org/)
- [Processing Foundation Grants](https://processingfoundation.org/grants)
- [Processing Foundation Impact Report 2023](https://processingfoundation.report/)
- [Processing Foundation - ProPublica](https://projects.propublica.org/nonprofits/organizations/460830259)
- [Processing Foundation Funding Update - Medium](https://medium.com/processing-foundation/processing-foundation-funding-update-94cddb25a3d9)

### L3C Model
- [L3C - Legal Information Institute](https://www.law.cornell.edu/wex/low-profit_limited_liability_company_(l3c))
- [L3C - Wikipedia](https://en.wikipedia.org/wiki/Low-profit_limited_liability_company)
- [L3C - Wolters Kluwer](https://www.wolterskluwer.com/en/expert-insights/what-is-l3c-low-profit-limited-liability-company)
- [L3C States - Attorney Aaron Hall](https://aaronhall.com/states-that-recognize-and-regulate-l3cs/)
- [L3C - Charity Lawyer Blog](https://charitylawyerblog.com/2010/02/21/l3c-whats-all-the-excitement-about/)

### B-Corp / Benefit Corporation
- [B Corp Taxes - Harness](https://www.harness.co/articles/understanding-benefit-corporation-b-corp-taxes-an-overview/)
- [B Corps and Benefit Corporations - USDN](https://sustainableconsumption.usdn.org/initiatives-list/b-corps-and-benefit-corporations)
- [B Corp vs Nonprofit - PayBee](https://w.paybee.io/post/b-corporation-vs-nonprofit)
- [Benefits of Being a B Corp - US Chamber](https://www.uschamber.com/co/start/strategy/b-corp-advantages-and-requirements)

### Public Benefit Corporation
- [Delaware PBC Statute](https://delcode.delaware.gov/title8/c001/sc15/)
- [Delaware PBC Developments - Harvard Law](https://corpgov.law.harvard.edu/2020/08/31/delaware-public-benefit-corporations-recent-developments/)
- [PBC FAQ - Cooley GO](https://www.cooleygo.com/faq-delaware-public-benefit-corporations/)
- [OpenAI Restructuring - ProMarket](https://www.promarket.org/2025/05/06/openai-abandons-move-to-for-profit-status-after-backlash-now-what/)
- [OpenAI Structure - CNBC](https://www.cnbc.com/2025/05/05/openai-says-nonprofit-retain-control-of-company-bowing-to-pressure.html)
- [Evolving OpenAI's Structure](https://openai.com/index/evolving-our-structure/)

### Cooperative Model
- [Worker Cooperatives in Tech - Platform Cooperativism](https://platform.coop/blog/varieties-of-worker-cooperatives-in-tech/)
- [Platform Cooperative - Wikipedia](https://en.wikipedia.org/wiki/Platform_cooperative)
- [Forming a Worker Coop - SELC](https://www.theselc.org/llc_v_cooperative_corporation)
- [Platform Cooperatives - OECD](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/09/empowering-communities-with-platform-cooperatives_63d716b6/c2ddfc9f-en.pdf)

### Fiscal Sponsorship + Separate LLC
- [Fiscal Sponsorship - American Bar Association](https://www.americanbar.org/groups/business_law/resources/business-law-today/2015-may/fiscal-sponsorship-what-you-should-know/)
- [Fiscal Sponsorship Models Summary](https://fiscalsponsorship.com/the-models-summary/)
- [LLC in Fiscal Sponsorship - Adler & Colvin](https://www.adlercolvin.com/wp-content/uploads/2017/12/The-Use-of-LLCs-in-Fiscal-Sponsorship-A-New-Model-00337073xA3536.pdf)
- [Fiscal Sponsorship Overview - AICPA](https://www.aicpa-cima.com/resources/article/fiscal-sponsorships-an-overview-for-not-for-profits)
- [Model A vs Model C - Mission Edge](https://www.missionedge.org/news-and-resources/fiscal-sponsorship-model-a-vs-model-c)

### Cross-Cutting
- [Nonprofit For-Profit Subsidiary - ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2014-june/taking-care-of-business-use-of-a-for-profit-subsidiary/)
- [For-Profit Subsidiary Formation - Jeremy Chen Law](http://jeremychenlaw.com/for-profit-subsidiary-of-a-nonprofit/)
- [UBIT Overview - ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2021-november/unrelated-business-income-tax/)
- [UBIT - IRS](https://www.irs.gov/charities-non-profits/unrelated-business-income-tax)
- [501(c)(3) vs 501(c)(6) for OSS](https://www.unsungnovelty.org/posts/05/2023/open-source-projects-and-non-profit-501c3-vs-non-profit-501c6/)
- [IRS 501(c)(3) Rejections for OSS - Mill Law Center](https://www.mill.law/blog/more-501c3-rejections-open-source-software-edition)
- [501(c)(3) Setup Costs](https://charitableallies.org/how-much-does-it-cost-to-set-up-a-501c3/)
- [Hybrid Organizations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10242097/)
- [Nonprofit Board Requirements - Foundation Group](https://www.501c3.org/protecting-your-dream-starting-a-sole-member-nonprofit/)
