# Design System Specification

## Overview

This document defines the complete design system for the multi-faceted portfolio. All components, pages, and sections must adhere to these specifications to ensure visual consistency while allowing section-specific personality.

## Design Principles

1. **Consistency with Flexibility**: Unified brand with section-specific accents
2. **Clarity**: Information hierarchy must be immediately clear
3. **Accessibility First**: WCAG AA minimum, AAA where possible
4. **Performance**: Design decisions support fast load times
5. **Responsive**: Mobile-first, works beautifully at any size

## Brand Identity

### Logo/Personal Mark

**Primary Logo**: "JN" monogram or full name "Joshua Nizamudin"

**Usage:**
- Header navigation (left aligned)
- Footer
- Favicon
- Social media avatars

**Specifications:**
- Format: SVG for scalability
- Size: 40px height in header, scales proportionally
- Color: Adapts to current section theme

### Brand Voice

- **Professional**: Competent and credible
- **Approachable**: Friendly without being casual
- **Clear**: No jargon unless necessary
- **Confident**: Assertive about skills and achievements

## Color System

### Brand Colors (Global)

```css
/* Primary Brand */
--primary-50: #eff6ff;
--primary-100: #dbeafe;
--primary-200: #bfdbfe;
--primary-300: #93c5fd;
--primary-400: #60a5fa;
--primary-500: #3b82f6;    /* Main brand blue */
--primary-600: #2563eb;
--primary-700: #1d4ed8;
--primary-800: #1e40af;
--primary-900: #1e3a8a;

/* Secondary Accent */
--secondary-500: #8b5cf6;  /* Purple accent */
--secondary-600: #7c3aed;
```

### Section-Specific Palettes

**Landing Page:**
```css
--landing-primary: var(--primary-500);
--landing-accent: var(--secondary-500);
--landing-bg: #ffffff;
--landing-text: var(--gray-900);
```

**Business Section:**
```css
--business-primary: #1e40af;    /* Navy */
--business-accent: #3b82f6;     /* Professional blue */
--business-bg: #f8fafc;         /* Light gray-blue */
--business-text: #0f172a;       /* Dark slate */
```

**Developer Section:**
```css
--developer-primary: #7c3aed;   /* Purple */
--developer-accent: #a855f7;    /* Light purple */
--developer-bg: #1e1e1e;        /* Dark (optional dark mode) */
--developer-text: #e2e8f0;      /* Light text for dark bg */
```

**Projects Section:**
```css
--projects-primary: var(--primary-500);
--projects-accent: var(--secondary-500);
--projects-bg: #ffffff;
--projects-text: var(--gray-900);
```

### Neutral Palette

```css
/* Grays (Light Theme) */
--gray-50: #f9fafb;
--gray-100: #f3f4f6;
--gray-200: #e5e7eb;
--gray-300: #d1d5db;
--gray-400: #9ca3af;
--gray-500: #6b7280;
--gray-600: #4b5563;
--gray-700: #374151;
--gray-800: #1f2937;
--gray-900: #111827;

/* Semantic Colors */
--success-500: #10b981;
--success-700: #047857;
--warning-500: #f59e0b;
--warning-700: #b45309;
--error-500: #ef4444;
--error-700: #b91c1c;
--info-500: #3b82f6;
--info-700: #1d4ed8;
```

### Color Usage Guidelines

**Backgrounds:**
- Primary BG: `--gray-50` (light) or `--gray-900` (dark)
- Card BG: `#ffffff` (light) or `--gray-800` (dark)
- Section BG: Section-specific background colors

**Text:**
- Primary text: `--gray-900` (light) or `--gray-100` (dark)
- Secondary text: `--gray-600` (light) or `--gray-400` (dark)
- Muted text: `--gray-500`

**Interactive Elements:**
- Links: `--primary-600` with `--primary-700` on hover
- Buttons: Section-specific primary colors
- Focus rings: `--primary-500` with 2px offset

## Typography

### Font Families

```css
/* Headings */
--font-heading: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Body Text */
--font-body: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Code/Monospace */
--font-mono: 'Fira Code', 'Courier New', Consolas, monospace;
```

**Font Loading Strategy:**
- Variable fonts for Inter (one file, all weights)
- Preload critical fonts
- Font-display: swap for better performance

### Type Scale

```css
/* Font Sizes */
--text-xs: 0.75rem;      /* 12px - captions, labels */
--text-sm: 0.875rem;     /* 14px - small text */
--text-base: 1rem;       /* 16px - body text */
--text-lg: 1.125rem;     /* 18px - emphasized body */
--text-xl: 1.25rem;      /* 20px - small headings */
--text-2xl: 1.5rem;      /* 24px - subheadings */
--text-3xl: 1.875rem;    /* 30px - section headings */
--text-4xl: 2.25rem;     /* 36px - page headings */
--text-5xl: 3rem;        /* 48px - hero headings */
--text-6xl: 3.75rem;     /* 60px - landing page hero */

/* Line Heights */
--leading-none: 1;
--leading-tight: 1.25;
--leading-snug: 1.375;
--leading-normal: 1.5;
--leading-relaxed: 1.625;
--leading-loose: 2;

/* Font Weights */
--font-light: 300;
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
--font-extrabold: 800;
```

### Typography Styles

**Hero Heading (Landing Page):**
```css
.hero-heading {
  font-family: var(--font-heading);
  font-size: var(--text-6xl);
  font-weight: var(--font-extrabold);
  line-height: var(--leading-tight);
  letter-spacing: -0.025em;
}
```

**Section Heading (H2):**
```css
.section-heading {
  font-family: var(--font-heading);
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  margin-bottom: var(--space-4);
}
```

**Subsection Heading (H3):**
```css
.subsection-heading {
  font-family: var(--font-heading);
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  margin-bottom: var(--space-3);
}
```

**Body Text:**
```css
.body-text {
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--font-normal);
  line-height: var(--leading-relaxed);
  color: var(--gray-700);
}
```

**Code Text:**
```css
.code-text {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--font-normal);
  line-height: var(--leading-normal);
  background: var(--gray-100);
  padding: 0.125rem 0.375rem;
  border-radius: 0.25rem;
}
```

## Spacing System

### Base Unit: 8px

```css
--space-0: 0;
--space-px: 1px;
--space-0-5: 0.125rem;  /* 2px */
--space-1: 0.25rem;     /* 4px */
--space-2: 0.5rem;      /* 8px */
--space-3: 0.75rem;     /* 12px */
--space-4: 1rem;        /* 16px */
--space-5: 1.25rem;     /* 20px */
--space-6: 1.5rem;      /* 24px */
--space-8: 2rem;        /* 32px */
--space-10: 2.5rem;     /* 40px */
--space-12: 3rem;       /* 48px */
--space-16: 4rem;       /* 64px */
--space-20: 5rem;       /* 80px */
--space-24: 6rem;       /* 96px */
--space-32: 8rem;       /* 128px */
```

### Spacing Usage

**Component Internal Spacing:**
- Padding: `--space-4` to `--space-6`
- Gap between elements: `--space-2` to `--space-4`

**Section Spacing:**
- Section padding top/bottom: `--space-16` to `--space-24`
- Section padding left/right: `--space-4` (mobile) to `--space-8` (desktop)

**Layout Spacing:**
- Header height: `--space-16` (64px)
- Footer padding: `--space-12`
- Max content width: `1280px` (xl breakpoint)

## Layout System

### Container

```css
.container {
  width: 100%;
  max-width: 1280px;  /* xl breakpoint */
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

@media (min-width: 768px) {
  .container {
    padding-left: var(--space-6);
    padding-right: var(--space-6);
  }
}

@media (min-width: 1024px) {
  .container {
    padding-left: var(--space-8);
    padding-right: var(--space-8);
  }
}
```

### Grid System

```css
.grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--space-6); }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-6); }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-6); }

/* Responsive */
@media (max-width: 767px) {
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .grid-3, .grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

## Component Styles

### Buttons

**Primary Button:**
```css
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-3) var(--space-6);
  font-family: var(--font-heading);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  line-height: 1;
  border-radius: 0.5rem;
  background: var(--primary-600);
  color: #ffffff;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: var(--primary-700);
  transform: translateY(-1px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.btn-primary:focus {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}
```

**Secondary Button:**
```css
.btn-secondary {
  /* Same as primary but: */
  background: transparent;
  color: var(--primary-600);
  border: 2px solid var(--primary-600);
}

.btn-secondary:hover {
  background: var(--primary-50);
}
```

### Cards

```css
.card {
  background: #ffffff;
  border-radius: 0.75rem;
  padding: var(--space-6);
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.card-interactive:hover {
  cursor: pointer;
  border-color: var(--primary-500);
}
```

### Badges

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  border-radius: 9999px;
  background: var(--gray-100);
  color: var(--gray-700);
}

.badge-primary {
  background: var(--primary-100);
  color: var(--primary-700);
}
```

### Form Elements

**Input:**
```css
.input {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--gray-900);
  background: #ffffff;
  border: 1px solid var(--gray-300);
  border-radius: 0.5rem;
  transition: all 0.2s ease;
}

.input:focus {
  outline: none;
  border-color: var(--primary-500);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.input-error {
  border-color: var(--error-500);
}
```

## Iconography

### Icon Set: Heroicons or Lucide

**Size Scale:**
- Small: 16px (1rem)
- Medium: 20px (1.25rem)
- Large: 24px (1.5rem)
- XLarge: 32px (2rem)

**Usage:**
- Navigation icons: 20px
- Button icons: 20px
- Card icons: 24px
- Hero icons: 32px+

**Color:**
- Default: Inherit from parent
- Decorative: Section accent colors
- Interactive: Match text color with hover states

## Animations & Transitions

### Timing Functions

```css
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

### Duration Scale

```css
--duration-fast: 150ms;
--duration-base: 200ms;
--duration-slow: 300ms;
--duration-slower: 500ms;
```

### Common Animations

**Fade In:**
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: fadeIn var(--duration-base) var(--ease-out);
}
```

**Slide Up:**
```css
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.slide-up {
  animation: slideUp var(--duration-slow) var(--ease-out);
}
```

**Hover Scale:**
```css
.hover-scale {
  transition: transform var(--duration-base) var(--ease-out);
}

.hover-scale:hover {
  transform: scale(1.05);
}
```

## Responsive Design

### Breakpoints

```javascript
const breakpoints = {
  sm: '640px',   // Mobile landscape
  md: '768px',   // Tablet
  lg: '1024px',  // Desktop
  xl: '1280px',  // Large desktop
  '2xl': '1536px' // Extra large
};
```

### Mobile-First Approach

All styles written for mobile first, then enhanced for larger screens:

```css
/* Mobile (default) */
.element {
  font-size: var(--text-base);
  padding: var(--space-4);
}

/* Tablet and up */
@media (min-width: 768px) {
  .element {
    font-size: var(--text-lg);
    padding: var(--space-6);
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .element {
    font-size: var(--text-xl);
    padding: var(--space-8);
  }
}
```

## Dark Mode (Optional Phase 2)

### Color Variables (Dark Theme)

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: var(--gray-900);
    --bg-secondary: var(--gray-800);
    --text-primary: var(--gray-100);
    --text-secondary: var(--gray-400);
    --border-color: var(--gray-700);
  }
}
```

## Accessibility

### Focus States

```css
*:focus-visible {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}
```

### Screen Reader Only

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Implementation in Tailwind

All these specifications will be configured in `tailwind.config.js`:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { /* ... */ },
        business: { /* ... */ },
        developer: { /* ... */ },
      },
      fontFamily: {
        heading: ['Inter', 'sans-serif'],
        body: ['Open Sans', 'sans-serif'],
        mono: ['Fira Code', 'monospace'],
      },
      spacing: {
        /* 8px base scale */
      },
    },
  },
};
```

## Next Steps

1. Create Tailwind configuration file
2. Set up global CSS with design tokens
3. Build base component library
4. Create style guide page for reference
