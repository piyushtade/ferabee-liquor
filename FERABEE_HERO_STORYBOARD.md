# FERABEE LIQUOR — MASTER HERO VIEWPORT & FIRST 10 SECONDS STORYBOARD
**Document Title:** Deep Hero Viewport Specification & Temporal Motion Choreography  
**Brand:** FERABEE LIQUOR PRIVATE LIMITED (*FERABEE — The Royal Bee*)  
**Role:** Principal Creative Technologist, Lead Motion Director & Art Director  
**Project Scope:** `https://github.com/piyushtade/ferabee-liquor`  
**Date:** August 14, 2026  
**Document Status:** Master Hero Storyboard Specification (Pre-Implementation Phase 4)

---

## 1. HERO VIEWPORT ARCHITECTURAL BLUEPRINT (100dvh)

The hero screen is the single most critical spatial zone on the website. It must establish brand authority, sensory luxury, and commercial disruption within **3 seconds**, without overwhelming the visitor with a wall of text.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                             12-COLUMN DESKTOP HERO MATRIX                                               │
├───────────────────┬───────────────────┬───────────────────┬───────────────────┬───────────────────┬─────────────────────┤
│ COL 1 - 2         │ COL 3 - 4         │ COL 5 - 6         │ COL 7 - 8         │ COL 9 - 10        │ COL 11 - 12         │
├───────────────────┴───────────────────┴───────────────────┴───────────────────┴───────────────────┴─────────────────────┤
│ [ STICKY HEADER: 👑 ROYAL EMBLEM ]          [ CENTER NAVIGATION ]                 [ 🎵 AMBIANCE ]  [ 💼 ACCESS DOSSIER ]│
├───────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────┤
│                                                   │                                                                     │
│  [EYEBROW] SERIES-A CAPITAL OFFERING (₹18 CR)     │                  [ THREE.JS 3D WEBGL DECANTER ]                     │
│                                                   │                  • PBR Flint Glass (IOR 1.52)                       │
│  INDIA'S FIRST DIRECT-TO-CONSUMER                 │                  • Amber Single Malt Volume Absorption              │
│  CRAFT SPIRITS ECOSYSTEM                          │                  • Real-Time Mouse Parallax Tilt                    │
│                                                   │                  • 320 Ambient Honeycomb Stardust Points            │
│  "Bypassing legacy retail monopolies through      │                                                                     │
│  367 captive Bee Lounges across Maharashtra       │                                                                     │
│  and Goa."                                        │                                                                     │
│                                                   │                                                                     │
│  [ ⚡ SIMULATE RETURNS ]   [ 💼 ACCESS DOSSIER ]  │                                                                     │
│                                                   │                                                                     │
├───────────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────┤
│ [ TRI-METRIC BAR: 367 Outlets (MH & Goa) │ ₹9.95L Monthly Store Profit │ 12.6-Mo Capex Payback │ SCROLL TO EXPLORE ↓ ]  │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. SPATIAL COORDINATES & CSS GRID LAYOUT BINDINGS

```css
/* Hero Container & Viewport Binding */
.hero-stage {
    position: relative;
    width: 100vw;
    min-height: 100dvh;
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: auto 1fr auto;
    column-gap: 32px;
    padding: 0 min(6vw, 80px);
    background-color: var(--color-void);
    overflow: hidden;
    z-index: var(--z-content-base);
}

/* Left Typographic Column (Cols 1–7) */
.hero-typography-cluster {
    grid-column: 1 / span 7;
    align-self: center;
    display: flex;
    flex-direction: column;
    gap: var(--space-24);
    z-index: var(--z-content-elevated);
}

/* Right 3D Viewport Column (Cols 7–12) */
.hero-bottle-viewport {
    grid-column: 7 / span 6;
    position: relative;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: var(--z-canvas-3d);
}

/* Bottom Tri-Metric Bar (Cols 1–12) */
.hero-metric-bar {
    grid-column: 1 / -1;
    display: grid;
    grid-template-columns: repeat(3, 1fr) auto;
    gap: var(--space-32);
    padding: var(--space-24) 0;
    border-top: 1px solid rgba(197, 160, 89, 0.18);
    align-self: end;
}
```

---

## 3. VISUAL READING ORDER & COGNITIVE HIERARCHY

```
                       [ 1. THE 3D AMBER DECANTER ]
                       Catches peripheral vision instantly via
                       internal amber refraction and motion.
                                  │
                                  ▼
                   [ 2. THE GRAND DISPLAY HEADLINE ]
                   "INDIA'S FIRST DIRECT-TO-CONSUMER SPIRITS ECOSYSTEM"
                   Establishes category leadership in 1.5 seconds.
                                  │
                                  ▼
                   [ 3. THE COMMERCIAL PROPOSITION ]
                   "Bypassing retail cartels through 367 captive Bee Lounges."
                   Provides immediate intellectual clarity.
                                  │
                                  ▼
                   [ 4. THE TRI-METRIC CREDIBILITY STRIP ]
                   367 Outlets · ₹9.95L Monthly Profit · 12.6-Month Payback
                   Validates institutional viability.
                                  │
                                  ▼
                   [ 5. THE DUAL PRIMARY CTAs ]
                   [ Simulate Returns ] or [ Access Master Dossier ]
                   Direct frictionless next action.
```

---

## 4. THE FIRST 10 SECONDS — SECOND-BY-SECOND CHOREOGRAPHY

```
┌──────────────┬───────────────────────────────┬─────────────────────────────────┬──────────────────────────────────────────┐
│ TIME         │ VISUAL & 3D PHENOMENA         │ MOTION & TYPOGRAPHY             │ SENSORY & ATTENTION REASONING            │
├──────────────┼───────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 0.0s – 1.0s  │ Deep obsidian canvas. Royal   │ 0% → 45% counter acceleration.  │ Silence and minimalism command instant   │
│              │ Gold Crest pulses at center.  │ Scale pulses: `1.00x → 1.04x`.  │ respect, clearing mental noise.          │
├──────────────┼───────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 1.0s – 2.0s  │ WebGL context initializes;    │ Shutter curtain splits          │ Anticipation resolves into astonishment  │
│              │ 320 golden points ignite.     │ vertically (`1.2s` luxury ease).│ as the 3D space opens.                   │
├──────────────┼───────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 2.0s – 3.5s  │ 3D hexagonal bottle emerges   │ Sinusoidal levitation starts    │ Visual lust: user is captivated by the   │
│              │ with amber volume glow.       │ (6.0s period, ±14px drift).     │ internal golden light in the decanter.   │
├──────────────┼───────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 3.5s – 5.5s  │ Ambient gold stardust drifts; │ Grand Cinzel headline staggers  │ Intellectual alignment: visitor learns   │
│              │ key lighting catches facets.  │ upward through line masks.      │ what FeraBee is in under 2 seconds.      │
├──────────────┼───────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 5.5s – 7.5s  │ Tri-metric cells illuminate;  │ Numbers roll up dynamically:    │ Financial credibility: hard figures      │
│              │ bottom hairline unrolls.      │ `0 → 367`, `0 → ₹9.95L`.        │ prove this is a commercial powerhouse.   │
├──────────────┼───────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 7.5s – 10.0s │ CTA buttons ignite with soft  │ Micro-magnetic attraction pulls │ Compulsion to interact: user clicks CTA  │
│              │ gold specular glow.           │ buttons toward cursor position. │ or initiates first scroll down.          │
└──────────────┴───────────────────────────────┴─────────────────────────────────┴──────────────────────────────────────────┘
```

---

## 5. MICRO-INTERACTIONS & PHYSICS IN THE HERO VIEWPORT

1. **3D Mouse Parallax:**
   * Mouse movement dynamically calculates normalized delta vectors (`dx`, `dy`).
   * The 3D decanter rotates smoothly on the Y-axis (`rotation.y = dx * 0.35`) and X-axis (`rotation.x = -dy * 0.25`) with a 0.08s lerp dampener.
2. **Magnetic CTA Snap:**
   * Primary action buttons calculate cursor proximity within a 120px bounding box, smoothly shifting up to 12px toward the pointer.
3. **Specular Glass Flare:**
   * Hovering over the bottle triggers a subtle increase in Three.js directional light intensity (`energy: 450 → 650`), causing the glass bevels to flash with golden radiance.

---

## 6. RESPONSIVE HERO ADAPTATIONS ACROSS BREAKPOINTS

```
┌─────────────────┬─────────────────────────┬───────────────────────────────┬───────────────────────────────────────────┐
│ VIEWPORT        │ TYPOGRAPHY SCALE        │ 3D DECANTER POSITION          │ LAYOUT & METRIC BAR ADAPTATION            │
├─────────────────┼─────────────────────────┼───────────────────────────────┼───────────────────────────────────────────┤
│ 1440px+         │ Display XL (4.8rem)     │ Positioned at Col 7–12        │ Full 12-col grid with 3-cell metric bar   │
│ (Desktop Master)│ (Line-height: 1.05)     │ Full WebGL + 320 particles    │ and persistent scroll-down indicator      │
├─────────────────┼─────────────────────────┼───────────────────────────────┼───────────────────────────────────────────┤
│ 1024px – 1439px │ Display L (3.6rem)      │ Positioned at Col 8–12        │ 12-col grid with compact metric cells     │
│ (Laptop / iPad) │ (Line-height: 1.10)     │ Full WebGL + 250 particles    │ and inline CTA group                      │
├─────────────────┼─────────────────────────┼───────────────────────────────┼───────────────────────────────────────────┤
│ 768px – 1023px  │ Display M (2.8rem)      │ Centered behind text with     │ 8-col grid; metric bar stacks into a      │
│ (Tablet)        │ (Line-height: 1.15)     │ 45% background opacity        │ 2×2 grid layout                           │
├─────────────────┼─────────────────────────┼───────────────────────────────┼───────────────────────────────────────────┤
│ 375px – 767px   │ Fluid clamp (2.2rem)    │ Positioned above headline or  │ 4-col stacked layout; bottom metric strip │
│ (Mobile)        │ (Line-height: 1.20)     │ rendered as high-res 3D card  │ converts into swipe pill carousel         │
└─────────────────┴─────────────────────────┴───────────────────────────────┴───────────────────────────────────────────┘
```

---

## 7. CRITICAL PERFORMANCE CONSTRAINTS & FALLBACKS

* **Zero Layout Shift (CLS = 0.00):** The hero canvas container explicitly reserves `100dvh` in CSS before WebGL initialization.
* **Instant Fallback Rendering:** If WebGL context creation fails or device memory is restricted, `assets/blender_render_showcase.png` immediately renders behind the headline with zero visual disruption.
* **GPU Render Loop Throttling:** When the user scrolls past the hero (`scrollY > window.innerHeight`), the Three.js hero animation loop automatically drops to 0 FPS to conserve device battery and CPU bandwidth.

---
*FERABEE Master Hero Viewport & First 10 Seconds Storyboard Completed and Approved.*
