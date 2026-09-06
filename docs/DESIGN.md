# 🎬 AI Script Analyzer - Frontend Master Design

## Page Structure

### **Page 1: Landing/Home**
```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│  Logo | AI Script Analyzer | Login  │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  HERO SECTION                       │
│  "Upload Your Script. Let AI Analyze"
│                                     │
│  Headline: "Professional Script     │
│  Analysis in Minutes"               │
│                                     │
│  Subtext: "Analyze character arcs,  │
│  dialogue quality, pacing, and more │
│  using Google Gemini AI"            │
│                                     │
│  [Primary CTA] Upload Script Now    │
│  [Secondary] Learn More             │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  FEATURES SECTION                   │
│                                     │
│  ✅ Batch Analysis    ✅ AI Rewrites│
│  ✅ Budget Impact     ✅ Comparison │
│  ✅ Timeline Optimization           │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  USE CASE: Pradeep Ranganathan      │
│                                     │
│  "Love Today (2022) Script Analysis"│
│  Budget: ₹5 Crore → ₹3.8 Crore     │
│  Savings: ₹1.2 Crore (24%)         │
│  Timeline: 45 days → 38 days       │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  FOOTER                             │
│  GitHub | LinkedIn | Contact       │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 2: Upload & Analyze**

```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│  Logo | Dashboard | Sign Out        │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  LEFT SIDEBAR (30%)                 │
│                                     │
│  📂 Recent Analyses                 │
│  ├─ Love Today (2h ago)             │
│  ├─ Comali (1d ago)                 │
│  └─ Dragon (3d ago)                 │
│                                     │
│  📊 Stats                           │
│  ├─ Scripts Analyzed: 12            │
│  ├─ Avg Analysis Time: 2.5 min      │
│  └─ Budget Saved: ₹4.2 Cr           │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  CENTER (70%)                       │
│                                     │
│  ┌──────────────────────────────┐   │
│  │  UPLOAD SECTION              │   │
│  │                              │   │
│  │  📤 Drag & Drop Scripts      │   │
│  │  OR                          │   │
│  │  [Browse Files]              │   │
│  │                              │   │
│  │  Supported: PDF, DOCX, TXT   │   │
│  │  Max: 50 MB per file         │   │
│  │                              │   │
│  └──────────────────────────────┘   │
│                                     │
│  Selected Files:                    │
│  ☑️ Love_Today.pdf (120 pages)      │
│  ☑️ Comali.docx (115 pages)         │
│  ☑️ Dragon.pdf (130 pages)          │
│                                     │
│  [Remove] [Add More]                │
│                                     │
│  Analysis Options:                  │
│  ☑️ Character Analysis              │
│  ☑️ Dialogue Quality                │
│  ☑️ Pacing & Structure              │
│  ☑️ Budget Impact                   │
│  ☑️ AI Rewrites Suggestions         │
│  ☑️ Comparative Analysis            │
│                                     │
│  [Cancel] [Start Analysis]          │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 3: Analysis In Progress**

```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  PROGRESS TRACKER                   │
│                                     │
│  📄 Love_Today.pdf                  │
│  ████████░░░░░░░░░░ 45% Complete    │
│  Status: Extracting text...         │
│  Time: 1 min 23 sec elapsed         │
│                                     │
│  📄 Comali.docx                     │
│  ██████░░░░░░░░░░░░░ 30% Complete   │
│  Status: Analyzing characters...    │
│  Time: Queued                       │
│                                     │
│  📄 Dragon.pdf                      │
│  ░░░░░░░░░░░░░░░░░░░ 0% Complete    │
│  Status: Waiting...                 │
│  Time: Queued                       │
│                                     │
│  Overall Progress: 25/100           │
│  ███████░░░░░░░░░░░░░░░░░░░░░░ 25%  │
│                                     │
│  Estimated Time: 4 mins remaining   │
│                                     │
│  [Cancel Analysis]                  │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 4: Analysis Results - Individual Report**

```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│  Logo | Love_Today.pdf | Export PDF │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  TABS                               │
│  Individual | Comparison | Rewrites │
│  Budget | Timeline                  │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  📊 OVERALL SCORE: 88/100           │
│  ████████░░░ Excellent              │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  📋 CHARACTER ANALYSIS              │
│                                     │
│  Characters Found: 12               │
│                                     │
│  ✅ Pradeep (Lead)                  │
│     Arc: Weak → Strong              │
│     Score: 92/100                   │
│     Pages: 1-154                    │
│     Consistency: Excellent          │
│                                     │
│  ✅ Ivana (Lead)                    │
│     Arc: Mystery → Revealed         │
│     Score: 85/100                   │
│     Pages: 5-154                    │
│     Consistency: Good               │
│                                     │
│  ⚠️ Yogi Babu (Supporting)          │
│     Arc: Flat                       │
│     Score: 72/100                   │
│     Pages: 23-140                   │
│     Consistency: Needs improvement  │
│     Suggestion: Add character goals │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  🎭 DIALOGUE QUALITY: 88/100        │
│                                     │
│  Authenticity: 90/100               │
│  Humor Level: 92/100                │
│  Emotional Impact: 84/100           │
│  Pacing: 85/100                     │
│                                     │
│  🔴 Weak Dialogue Scenes:           │
│  ├─ Scene 45 (Page 67)              │
│  │  "Hey, I love you"               │
│  │  Score: 62/100                   │
│  │  Issue: Cliché, no personality   │
│  │                                  │
│  ├─ Scene 78 (Page 110)             │
│  │  "This is complicated"           │
│  │  Score: 65/100                   │
│  │  Issue: Generic                  │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  ⏱️ PACING & STRUCTURE: 85/100      │
│                                     │
│  Act 1: 28 pages - Good (5%)        │
│  Act 2: 96 pages - Good (62%)       │
│  Act 3: 30 pages - Good (19%)       │
│                                     │
│  🔴 Pacing Issues:                  │
│  ├─ Pages 45-67: Slow buildup       │
│  │  Suggestion: Cut 5-7 pages       │
│  │                                  │
│  ├─ Pages 98-110: Dragging climax   │
│  │  Suggestion: Tighten scenes      │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  💡 KEY SUGGESTIONS                 │
│                                     │
│  1. Strengthen Yogi Babu's character│
│     Pages: 23-140                   │
│     Difficulty: Medium              │
│                                     │
│  2. Improve weak dialogue (2 scenes)│
│     Pages: 67, 110                  │
│     Difficulty: Easy                │
│                                     │
│  3. Tighten pacing (Act 2)          │
│     Pages: 45-67, 98-110            │
│     Difficulty: Hard                │
│                                     │
│  [View Rewrite Suggestions]         │
│  [Download Full Report]             │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 5: Comparison Analysis (Multi-Script)**

```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│  Scripts: Love Today | Comali |     │
│  Dragon | [Add More]                │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  📊 COMPARISON TABLE                │
│                                     │
│  Metric          | Love Today|Comali│Dragon│
│  ──────────────────────────────────│
│  Overall Score   |    88    |  92   | 88   │
│  Character Arc   |    85    |  95   | 92   │
│  Dialogue        |    88    |  89   | 90   │
│  Pacing          |    85    |  88   | 82   │
│  Production Ease |    92    |  85   | 78   │
│                                     │
│  🏆 Best Script: COMALI (92/100)    │
│  🥈 2nd: Dragon (88/100)            │
│  🥉 3rd: Love Today (88/100)        │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  💡 INSIGHTS                        │
│                                     │
│  Comali has strongest character     │
│  development (95/100)               │
│                                     │
│  Dragon has best dialogue quality   │
│  (90/100) but weakest pacing        │
│                                     │
│  Love Today most production-ready   │
│  (92/100 ease score)                │
│                                     │
│  Recommendation: Make Comali next   │
│  (highest creative potential)       │
│                                     │
│  [View Detailed Comparison]         │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 6: AI Rewrite Suggestions**

```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│  AI Rewrites | Love Today           │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  🔴 WEAK SCENES (Auto-Rewritten)    │
│                                     │
│  Scene 45 - Page 67                 │
│  ──────────────────────────────────│
│                                     │
│  ❌ ORIGINAL:                       │
│  "Hey, I love you"                  │
│  "I love you too"                   │
│                                     │
│  ✅ REWRITE OPTION 1:               │
│  "You drive me absolutely crazy"    │
│  "Good crazy or bad crazy?"         │
│  "The kind that makes me want to    │
│   spend forever with you"           │
│                                     │
│  ✅ REWRITE OPTION 2:               │
│  "I never thought I'd feel this way"│
│  "About me?"                        │
│  "About life. About us."            │
│                                     │
│  ✅ REWRITE OPTION 3:               │
│  "You're my favorite chaos"         │
│  "Is that good?"                    │
│  "It's perfect"                     │
│                                     │
│  [Accept Option 1] [Accept 2]       │
│  [Accept 3] [Keep Original]         │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  Scene 78 - Page 110                │
│  ──────────────────────────────────│
│                                     │
│  ❌ ORIGINAL:                       │
│  "This is complicated"              │
│                                     │
│  ✅ REWRITTEN AS:                   │
│  "I don't know how to untangle this"│
│                                     │
│  Score improved: 65/100 → 82/100    │
│                                     │
│  [Accept] [Reject]                  │
│                                     │
│  Total Rewrites Available: 7        │
│  Accepted So Far: 2                 │
│                                     │
│  [Export Updated Script]            │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 7: Budget & Timeline Analysis**

```
┌─────────────────────────────────────┐
│                                     │
│  HEADER                             │
│  Budget Analysis | Love Today       │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  💰 BUDGET BREAKDOWN                │
│                                     │
│  Original Budget: ₹5,00,00,000      │
│  Optimized Budget: ₹3,80,00,000     │
│  SAVINGS: ₹1,20,00,000 (24%)        │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  🔴 EXPENSIVE SCENES (High Cost)    │
│                                     │
│  Scene: Beach Wedding (Pages 23-28) │
│  Cost: ₹80,00,000                   │
│  Shooting Days: 5                   │
│  Resources: Location + 100+ crew    │
│                                     │
│  Keep? ✅ YES                       │
│  Reason: Critical to story          │
│  ROI: High audience appeal          │
│                                     │
│  ──────────────────────────────────│
│                                     │
│  Scene: Car Chase (Pages 98-102)    │
│  Cost: ₹1,50,00,000                 │
│  Shooting Days: 3                   │
│  Resources: 5 cars, stunt crew      │
│                                     │
│  Keep? ❌ NO (Suggested Cut)        │
│  Reason: Not essential to plot      │
│  Savings: ₹1,50,00,000              │
│                                     │
│  ──────────────────────────────────│
│                                     │
│  Scene: Temple Scene (Pages 45-50)  │
│  Cost: ₹20,00,000                   │
│  Shooting Days: 2                   │
│  Resources: Location, extras        │
│                                     │
│  Keep? ⚠️ DOWNGRADE                 │
│  Alternative: Studio set            │
│  New Cost: ₹8,00,000 (60% savings)  │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  ⏱️ TIMELINE OPTIMIZATION           │
│                                     │
│  Original: 45 shooting days         │
│  Optimized: 38 shooting days        │
│  Saved: 7 days (15% reduction)      │
│                                     │
│  Cost per day: ₹15,00,000           │
│  Timeline Savings: ₹1,05,00,000     │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  📊 FINAL ANALYSIS                  │
│                                     │
│  Original: ₹5,00,00,000 / 45 days   │
│  Optimized: ₹3,80,00,000 / 38 days  │
│                                     │
│  Budget Saved: ₹1,20,00,000 (24%)   │
│  Timeline Reduced: 7 days (15%)     │
│                                     │
│  ✅ Quality Impact: Minimal         │
│  ✅ Story Impact: None              │
│  ✅ Audience Appeal: Same           │
│                                     │
│  [Accept Recommendations]           │
│  [Download Budget Report]           │
│                                     │
└─────────────────────────────────────┘
```

---

### **Page 8: Export & Download**

```
┌─────────────────────────────────────┐
│                                     │
│  EXPORT OPTIONS                     │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  📥 DOWNLOAD REPORT                 │
│                                     │
│  ☑️ Full Analysis Report (PDF)      │
│     Size: 2.3 MB                    │
│     Pages: 24                       │
│                                     │
│  ☑️ Executive Summary (PDF)         │
│     Size: 0.8 MB                    │
│     Pages: 3                        │
│                                     │
│  ☑️ Detailed JSON Data              │
│     Size: 1.2 MB                    │
│     Format: Machine-readable        │
│                                     │
│  ☑️ Updated Script (DOCX)           │
│     Size: 2.1 MB                    │
│     Includes: Rewrites + suggestions│
│                                     │
│  ☑️ Budget Breakdown (Excel)        │
│     Size: 0.5 MB                    │
│     Format: Editable                │
│                                     │
├─────────────────────────────────────┤
│                                     │
│  [Select All] [Download Selected]   │
│                                     │
│  OR                                 │
│                                     │
│  [Email Report to Team]             │
│  Email: ________@example.com        │
│  [Send]                             │
│                                     │
│  OR                                 │
│                                     │
│  [Share Link]                       │
│  Link: https://ai-script.../abc123  │
│  Expires: In 30 days                │
│  [Copy Link]                        │
│                                     │
└─────────────────────────────────────┘
```

---

## Component Details

### **Upload Area**
- Drag & drop zone
- File browser button
- Accepted formats: PDF, DOCX, TXT
- Max file size: 50 MB
- Visual feedback on hover
- Progress bar during upload

### **Results Cards**
- Score gauge (0-100)
- Color coding: Green (90+), Yellow (70-89), Red (<70)
- Expandable sections
- Icons for each metric
- Action buttons

### **Navigation**
- Sidebar (desktop)
- Bottom nav (mobile)
- Breadcrumb trail
- Back button
- Download/Export always visible

### **Colors**
- Primary: Gemini Gold (#F9AB00)
- Secondary: Google Blue (#4285F4)
- Success: Green (#34A853)
- Warning: Yellow (#FBBC04)
- Error: Red (#EA4335)
- Text: Dark (#202124)
- Background: Light gray (#F8F9FA)

### **Typography**
- Heading: 32px bold
- Subheading: 24px semi-bold
- Body: 16px regular
- Small: 14px regular
- Mono (code): 12px monospace

---

## Mobile Responsive

**Breakpoints:**
- Mobile: < 640px
- Tablet: 641-1024px
- Desktop: > 1024px

**Mobile Changes:**
- Single column layout
- Bottom sheet for modals
- Swipe navigation for tabs
- Larger touch targets (48px minimum)
- Simplified sidebars

---

## User Flows

### **Happy Path (Multi-Script Analysis)**
1. Login
2. Upload 3 scripts
3. Select analysis options
4. Click "Start Analysis"
5. Monitor progress
6. View individual reports
7. View comparison
8. View rewrites
9. View budget impact
10. Download reports
11. Share with team

### **Alternative: Single Script**
1. Upload script
2. Auto-start analysis
3. View results
4. Accept/reject rewrites
5. Download report

---

## Key Features to Build

✅ File upload (drag & drop)
✅ Progress tracking
✅ Tabbed results view
✅ Comparison table
✅ Rewrite suggestions with accept/reject
✅ Budget breakdown visualization
✅ Export to PDF/JSON/DOCX
✅ Share links
✅ Email delivery
✅ Responsive design
✅ Dark mode toggle
✅ User authentication
✅ History/recent analyses
✅ Team collaboration (comments)

---

## API Endpoints Needed

```
POST /api/auth/login
POST /api/auth/logout
POST /api/scripts/upload
POST /api/scripts/analyze
GET /api/scripts/{id}/results
GET /api/scripts/{id}/results/individual
GET /api/scripts/comparison
GET /api/scripts/{id}/rewrites
GET /api/scripts/{id}/budget
POST /api/scripts/{id}/rewrites/accept
POST /api/scripts/{id}/export
POST /api/scripts/share
GET /api/user/history
```

---

**NOW BUILD THIS IN CURSOR!** 🚀
