# HTML3 Layout Patterns

This document defines complex layout patterns for the HTML3 ecosystem, combining atomic BECSS components into functional interfaces.

## 1. Combo Sidebar (Authoritative)
Used for primary navigation with integrated widget zones.

```html
<aside class="c-sidebar c-sidebar--combo" role="navigation">
    <div class="c-sidebar__top">
        <div class="c-sidebar__section-title">Navigation</div>
        <nav class="c-sidebar__links">
            <a href="#" class="c-sidebar__link c-sidebar__link--active">Overview</a>
            <a href="#" class="c-sidebar__link">Architecture</a>
        </nav>
    </div>
    <div class="c-sidebar__widget-zone">
        <!-- Atomic c-widget components go here -->
        <div class="c-widget c-widget--small">...</div>
    </div>
</aside>
```

## 2. Tabbed Dashboard
A standard layout featuring a stats bar, sub-navigation, and dynamic content cards.

```html
<main class="l-dashboard">
    <!-- Section 1: Stats -->
    <section class="u-mb-24">
        <div class="c-stats-bar">
            <div class="c-stats-bar__item">
                <div class="c-stats-bar__label">RECORDS</div>
                <div class="c-stats-bar__value">1,240</div>
            </div>
            <!-- ... -->
        </div>
    </section>

    <!-- Section 2: Navigation -->
    <section class="u-mb-24">
        <div class="c-subtabs">
            <button class="c-subtabs__btn c-subtabs__btn--active">General</button>
            <button class="c-subtabs__btn">Security</button>
        </div>
    </section>

    <!-- Section 3: Content -->
    <section class="c-card-grid">
        <div class="c-card">
            <h2 class="c-card__title">System Status</h2>
            <div class="c-card__body">All systems operational.</div>
        </div>
    </section>
</main>
```

## 3. Standard Header
Authoritative header structure with logo and mobile hamburger control.

```html
<header class="c-header" role="banner">
    <button class="c-hamburger" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
    </button>
    <div class="c-header__logo">APP_NAME</div>
</header>
```

---
*Relational ID: html3-layout-patterns*
