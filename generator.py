r"""
HTML Documentation Generator for AnnaLis Gadea (paparazzi.li/annalis-gadea)
Generates complete, searchable, offline HTML documentation with whole image viewer.
Output directory: D:\Annalis_Gadea\html
"""

import os
import json
import shutil
import html

OUTPUT_DIR = r"D:\Annalis_Gadea\html"
DATA_SOURCE = r"D:\Annalis_Gadea\htmlold\data.json"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")

# CSS Content
CSS_CONTENT = """/* AnnaLis Gadea - Documentation & Gallery Stylesheet */
:root {
  --bg-primary: #0b0f19;
  --bg-surface: #131b2e;
  --bg-card: #1a243b;
  --bg-card-hover: #22304e;
  --bg-sidebar: #0e1526;
  --border-color: #23314f;
  --border-subtle: #1e2b45;
  --accent: #38bdf8;
  --accent-hover: #7dd3fc;
  --accent-gold: #f59e0b;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
  --shadow-md: 0 6px 20px rgba(0,0,0,0.4);
  --shadow-lg: 0 12px 36px rgba(0,0,0,0.6);
  --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-family);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  display: flex;
  min-height: 100vh;
  overflow-x: hidden;
}

/* Sidebar */
.app-sidebar {
  width: 290px;
  background-color: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--border-color) transparent;
}

.sidebar-header {
  padding: 24px 20px 18px;
  border-bottom: 1px solid var(--border-color);
  background: linear-gradient(180deg, rgba(56, 189, 248, 0.06) 0%, transparent 100%);
}

.sidebar-logo {
  text-decoration: none;
  display: block;
}

.sidebar-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: -0.02em;
  margin-bottom: 3px;
}

.sidebar-subtitle {
  font-size: 0.8rem;
  color: var(--accent-gold);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
}

.sidebar-meta {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 4px;
}

.sidebar-nav {
  padding: 16px 12px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  flex: 1;
}

.nav-section-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  padding: 14px 10px 6px;
}

.nav-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.875rem;
  transition: all 0.15s ease-in-out;
}

.nav-link:hover {
  background-color: var(--bg-card);
  color: var(--text-primary);
}

.nav-link.active {
  background-color: rgba(56, 189, 248, 0.12);
  color: var(--accent);
  font-weight: 600;
  border-left: 3px solid var(--accent);
}

.nav-link-title {
  display: flex;
  align-items: center;
  gap: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.nav-badge {
  font-size: 0.72rem;
  padding: 2px 7px;
  background-color: var(--bg-card);
  color: var(--text-muted);
  border-radius: 9999px;
  border: 1px solid var(--border-color);
  font-weight: 500;
}

.nav-link.active .nav-badge {
  background-color: var(--accent);
  color: #0b0f19;
  border-color: var(--accent);
  font-weight: 700;
}

.sidebar-footer {
  padding: 16px 20px;
  border-top: 1px solid var(--border-color);
  font-size: 0.75rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Main Content Area */
.app-main {
  margin-left: 290px;
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Header */
.top-header {
  position: sticky;
  top: 0;
  z-index: 90;
  background-color: rgba(11, 15, 25, 0.88);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
  padding: 12px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.header-search-wrapper {
  position: relative;
  flex: 1;
  max-width: 640px;
}

.search-input-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  pointer-events: none;
}

.header-search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-size: 0.9rem;
  outline: none;
  transition: all 0.2s ease;
}

.header-search-input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
  background-color: var(--bg-card);
}

.header-search-input::placeholder {
  color: var(--text-muted);
}

/* Live Search Dropdown */
.search-dropdown {
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  right: 0;
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  max-height: 480px;
  overflow-y: auto;
  display: none;
  z-index: 1000;
}

.search-dropdown.open {
  display: block;
}

.search-result-group {
  padding: 8px 0;
  border-bottom: 1px solid var(--border-color);
}

.search-group-title {
  padding: 6px 16px;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}

.search-result-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 16px;
  text-decoration: none;
  color: var(--text-primary);
  transition: background-color 0.15s ease;
}

.search-result-item:hover {
  background-color: var(--bg-card);
}

.search-result-thumb {
  width: 44px;
  height: 44px;
  object-fit: cover;
  border-radius: 4px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-card);
}

.search-result-info {
  flex: 1;
  min-width: 0;
}

.search-result-name {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.search-result-desc {
  font-size: 0.76rem;
  color: var(--text-secondary);
}

.search-see-all {
  display: block;
  text-align: center;
  padding: 12px;
  font-size: 0.84rem;
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
  background-color: rgba(56, 189, 248, 0.05);
  border-top: 1px solid var(--border-color);
}

.search-see-all:hover {
  text-decoration: underline;
}

.header-quick-links {
  display: flex;
  align-items: center;
  gap: 12px;
}

.quick-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  font-size: 0.85rem;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.15s ease;
}

.quick-link-btn:hover {
  background-color: var(--bg-card);
  color: var(--text-primary);
  border-color: var(--accent);
}

/* Page Container */
.page-container {
  padding: 32px;
  max-width: 1440px;
  margin: 0 auto;
  width: 100%;
  flex: 1;
}

/* Hero Section */
.page-hero {
  margin-bottom: 28px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 16px;
}

.page-title {
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
}

.page-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.page-meta-badge {
  background-color: rgba(56, 189, 248, 0.12);
  color: var(--accent);
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
}

/* Artwork Grid */
.artwork-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 22px;
}

/* Artwork Card */
.artwork-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  position: relative;
}

.artwork-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5);
  background-color: var(--bg-card-hover);
}

.artwork-thumb-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 1 / 1;
  background-color: #0d1322;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.artwork-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
  display: block;
}

.artwork-card:hover .artwork-thumb {
  transform: scale(1.05);
}

.artwork-zoom-overlay {
  position: absolute;
  inset: 0;
  background: rgba(11, 15, 25, 0.65);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  opacity: 0;
  transition: opacity 0.2s ease;
  color: #ffffff;
}

.artwork-card:hover .artwork-zoom-overlay {
  opacity: 1;
}

.zoom-overlay-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background-color: rgba(56, 189, 248, 0.9);
  color: #0b0f19;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 9999px;
  box-shadow: var(--shadow-sm);
}

.artwork-info {
  padding: 12px 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--border-subtle);
}

.artwork-title {
  font-weight: 700;
  font-size: 0.95rem;
  color: #ffffff;
  font-family: monospace;
}

.artwork-category {
  font-size: 0.75rem;
  color: var(--text-secondary);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 130px;
}

/* Lightbox Modal - Full Image Viewer */
.lightbox-modal {
  position: fixed;
  inset: 0;
  background-color: rgba(6, 9, 15, 0.96);
  z-index: 2000;
  display: none;
  flex-direction: column;
  backdrop-filter: blur(10px);
  user-select: none;
}

.lightbox-modal.open {
  display: flex;
}

/* Lightbox Toolbar */
.lightbox-header {
  height: 56px;
  padding: 0 20px;
  background-color: rgba(14, 21, 38, 0.92);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 2010;
}

.lightbox-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
}

.lightbox-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: #ffffff;
  font-family: monospace;
}

.lightbox-badge {
  font-size: 0.78rem;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--accent);
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 600;
}

.lightbox-counter {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.lightbox-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.lightbox-btn {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  height: 36px;
  padding: 0 12px;
  border-radius: var(--radius-sm);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.15s ease;
}

.lightbox-btn:hover {
  background: var(--bg-card);
  border-color: var(--accent);
  color: #ffffff;
}

.lightbox-btn.active {
  background: var(--accent);
  color: #0b0f19;
  border-color: var(--accent);
}

.lightbox-btn-close {
  background: rgba(239, 68, 68, 0.15);
  border-color: rgba(239, 68, 68, 0.3);
  color: #f87171;
  font-size: 1.1rem;
  width: 36px;
  padding: 0;
  justify-content: center;
}

.lightbox-btn-close:hover {
  background: #ef4444;
  color: #ffffff;
  border-color: #ef4444;
}

/* Lightbox Stage */
.lightbox-stage {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 20px;
}

.lightbox-stage.zoomed {
  overflow: auto;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 40px;
  cursor: grab;
}

.lightbox-stage.zoomed:active {
  cursor: grabbing;
}

.lightbox-img-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 100%;
  max-height: 100%;
  position: relative;
}

.lightbox-stage.zoomed .lightbox-img-wrapper {
  max-width: none;
  max-height: none;
  margin: auto;
}

.lightbox-img {
  max-width: 92vw;
  max-height: calc(100vh - 120px);
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
  transition: transform 0.2s ease, opacity 0.2s ease;
  display: block;
}

.lightbox-stage.zoomed .lightbox-img {
  max-width: none;
  max-height: none;
  border-radius: 0;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9);
}

/* Lightbox Arrows */
.lightbox-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(14, 21, 38, 0.85);
  border: 1px solid var(--border-color);
  color: #ffffff;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 2020;
}

.lightbox-arrow:hover {
  background-color: var(--accent);
  color: #0b0f19;
  border-color: var(--accent);
  transform: translateY(-50%) scale(1.08);
}

.lightbox-arrow.prev {
  left: 24px;
}

.lightbox-arrow.next {
  right: 24px;
}

/* Lightbox Hint & Instructions */
.lightbox-hint {
  position: absolute;
  bottom: 14px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(11, 15, 25, 0.85);
  border: 1px solid var(--border-color);
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 0.76rem;
  color: var(--text-secondary);
  pointer-events: none;
  display: flex;
  gap: 16px;
}

/* Biography & Overview Page */
.bio-hero-card {
  background: linear-gradient(135deg, var(--bg-surface) 0%, var(--bg-card) 100%);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 36px;
  margin-bottom: 40px;
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 36px;
  align-items: start;
}

.bio-portrait-wrap {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 2px solid var(--border-color);
  box-shadow: var(--shadow-md);
  cursor: pointer;
  background-color: #0b0f19;
}

.bio-portrait {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.3s ease;
}

.bio-portrait-wrap:hover .bio-portrait {
  transform: scale(1.03);
}

.bio-portrait-badge {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  background: rgba(11, 15, 25, 0.8);
  backdrop-filter: blur(4px);
  padding: 6px 10px;
  border-radius: 4px;
  text-align: center;
  font-size: 0.74rem;
  color: var(--accent);
  font-weight: 600;
}

.bio-intro-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.bio-name {
  font-size: 2.2rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: -0.02em;
}

.bio-dates {
  font-size: 1.1rem;
  color: var(--accent-gold);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
}

.bio-quote {
  font-style: italic;
  font-size: 1.05rem;
  color: #e2e8f0;
  border-left: 3px solid var(--accent);
  padding-left: 18px;
  margin: 8px 0;
  line-height: 1.7;
}

.lang-tabs {
  display: flex;
  gap: 8px;
  margin: 16px 0 24px;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 12px;
}

.lang-tab-btn {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  padding: 8px 18px;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.lang-tab-btn.active {
  background: var(--accent);
  color: #0b0f19;
  border-color: var(--accent);
}

.lang-pane {
  display: none;
}

.lang-pane.active {
  display: block;
}

.bio-section-box {
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  margin-bottom: 20px;
}

.bio-section-heading {
  font-size: 1.2rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.bio-section-text {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.8;
}

/* Categories Grid on Home */
.section-title-wrap {
  margin: 40px 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.section-main-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffffff;
}

.categories-explorer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 48px;
}

.category-card {
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.category-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent);
  box-shadow: var(--shadow-md);
  background-color: var(--bg-card-hover);
}

.category-card-thumb-wrap {
  width: 100%;
  aspect-ratio: 16 / 10;
  background-color: #0d1322;
  overflow: hidden;
}

.category-card-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.category-card:hover .category-card-thumb {
  transform: scale(1.05);
}

.category-card-body {
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.category-card-title {
  font-size: 1rem;
  font-weight: 700;
  color: #ffffff;
}

.category-card-badge {
  background-color: rgba(56, 189, 248, 0.12);
  color: var(--accent);
  border: 1px solid rgba(56, 189, 248, 0.25);
  font-size: 0.76rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 9999px;
}

/* Dedicated Search Page */
.search-controls-box {
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 28px;
  display: grid;
  grid-template-columns: 1fr 260px;
  gap: 16px;
}

.search-field-wrap {
  position: relative;
}

.search-field-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: #ffffff;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s;
}

.search-field-input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
}

.search-field-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
}

.category-select {
  padding: 12px 16px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: #ffffff;
  font-size: 0.95rem;
  outline: none;
  cursor: pointer;
}

.category-select:focus {
  border-color: var(--accent);
}

.search-stats-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  color: var(--text-secondary);
  font-size: 0.92rem;
}

.search-text-results {
  margin-bottom: 32px;
}

.search-text-item {
  background-color: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 18px 22px;
  margin-bottom: 12px;
  text-decoration: none;
  display: block;
  transition: all 0.2s ease;
}

.search-text-item:hover {
  border-color: var(--accent);
  background-color: var(--bg-card);
  transform: translateX(4px);
}

.search-text-title {
  color: #ffffff;
  font-weight: 700;
  font-size: 1.05rem;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.search-text-snippet {
  color: var(--text-secondary);
  font-size: 0.88rem;
  line-height: 1.6;
}

/* Mobile Toggle */
.mobile-nav-toggle {
  display: none;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .app-sidebar {
    transform: translateX(-100%);
    transition: transform 0.3s ease;
  }
  .app-sidebar.open {
    transform: translateX(0);
  }
  .app-main {
    margin-left: 0;
  }
  .mobile-nav-toggle {
    display: block;
  }
  .bio-hero-card {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .bio-portrait-wrap {
    max-width: 280px;
    margin: 0 auto;
  }
  .bio-dates {
    justify-content: center;
  }
  .search-controls-box {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .page-container {
    padding: 20px 16px;
  }
  .artwork-grid {
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 14px;
  }
  .top-header {
    padding: 10px 16px;
  }
  .page-title {
    font-size: 1.5rem;
  }
  .lightbox-arrow {
    width: 40px;
    height: 40px;
    font-size: 1.1rem;
  }
  .lightbox-arrow.prev { left: 10px; }
  .lightbox-arrow.next { right: 10px; }
}
"""

# JS Content
JS_CONTENT = r"""/* AnnaLis Gadea Documentation Application & Image Viewer Script */
(function() {
  'use strict';

  // State
  let currentGalleryItems = [];
  let currentIndex = 0;
  let isZoomed = false;
  let isMouseDown = false;
  let startX = 0, startY = 0, scrollLeft = 0, scrollTop = 0;
  let hasDragged = false;

  // DOM Elements
  const headerSearchInput = document.getElementById('headerSearchInput');
  const searchDropdown = document.getElementById('searchDropdown');
  const searchPageInput = document.getElementById('searchPageInput');
  const categoryFilter = document.getElementById('categoryFilter');
  const searchResultsGrid = document.getElementById('searchResultsGrid');
  const searchTextResults = document.getElementById('searchTextResults');
  const searchStats = document.getElementById('searchStats');
  const mobileNavToggle = document.getElementById('mobileNavToggle');
  const appSidebar = document.querySelector('.app-sidebar');

  // Lightbox DOM Elements
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxStage = document.getElementById('lightboxStage');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxCategory = document.getElementById('lightboxCategory');
  const lightboxCounter = document.getElementById('lightboxCounter');
  const lightboxOpenFull = document.getElementById('lightboxOpenFull');
  const lightboxZoomBtn = document.getElementById('lightboxZoomBtn');
  const lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
  const lightboxPrevBtn = document.getElementById('lightboxPrevBtn');
  const lightboxNextBtn = document.getElementById('lightboxNextBtn');

  const searchData = window.SEARCH_DATA || { pages: [], items: [] };

  // Helper: Normalize strings for tolerant search (umlauts, accents, case)
  function normalizeSearchText(str) {
    if (!str) return '';
    return str.toLowerCase()
      .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
      .normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  }

  // --- Mobile Sidebar Toggle ---
  if (mobileNavToggle && appSidebar) {
    mobileNavToggle.addEventListener('click', function(e) {
      e.stopPropagation();
      appSidebar.classList.toggle('open');
    });

    document.addEventListener('click', function(e) {
      if (!appSidebar.contains(e.target) && !mobileNavToggle.contains(e.target)) {
        appSidebar.classList.remove('open');
      }
    });
  }

  // --- Header Live Search ---
  if (headerSearchInput && searchDropdown) {
    headerSearchInput.addEventListener('input', function(e) {
      const q = e.target.value.trim();
      if (!q) {
        searchDropdown.classList.remove('open');
        searchDropdown.innerHTML = '';
        return;
      }
      renderHeaderSearch(q);
    });

    headerSearchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        const q = headerSearchInput.value.trim();
        if (q) {
          window.location.href = 'search.html?q=' + encodeURIComponent(q);
        }
      } else if (e.key === 'Escape') {
        searchDropdown.classList.remove('open');
      }
    });

    document.addEventListener('click', function(e) {
      if (!headerSearchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
        searchDropdown.classList.remove('open');
      }
    });
  }

  function renderHeaderSearch(q) {
    const nq = normalizeSearchText(q);

    const matchedPages = searchData.pages.filter(p => {
      const nt = normalizeSearchText(p.title);
      const nx = normalizeSearchText(p.text);
      return nt.includes(nq) || nx.includes(nq);
    }).slice(0, 4);

    const matchedArtworks = searchData.items.filter(item => {
      const nt = normalizeSearchText(item.title);
      const nc = normalizeSearchText(item.category);
      const np = normalizeSearchText(item.caption);
      return nt.includes(nq) || nc.includes(nq) || np.includes(nq);
    }).slice(0, 8);

    if (matchedPages.length === 0 && matchedArtworks.length === 0) {
      searchDropdown.innerHTML = '<div style="padding: 16px; text-align: center; color: var(--text-muted);">Keine Ergebnisse für "' + escapeHtml(q) + '"</div>';
      searchDropdown.classList.add('open');
      return;
    }

    let html = '';

    if (matchedPages.length > 0) {
      html += '<div class="search-result-group"><div class="search-group-title">Seiten & Serien</div>';
      matchedPages.forEach(p => {
        html += `
          <a class="search-result-item" href="${p.filename}">
            <div class="search-result-info">
              <div class="search-result-name">${highlightMatch(p.title, q)}</div>
              <div class="search-result-desc">${escapeHtml(p.badge || 'Dokumentation')}</div>
            </div>
          </a>
        `;
      });
      html += '</div>';
    }

    if (matchedArtworks.length > 0) {
      html += '<div class="search-result-group"><div class="search-group-title">Kunstwerke & Gemälde</div>';
      matchedArtworks.forEach(item => {
        const fullUrl = item.full || item.full_url || item.thumb || item.thumb_url;
        const thumbUrl = item.thumb || item.thumb_url || fullUrl;
        html += `
          <a class="search-result-item" href="${item.page_filename}">
            <img class="search-result-thumb" src="${thumbUrl}" alt="${escapeHtml(item.title)}" loading="lazy">
            <div class="search-result-info">
              <div class="search-result-name">${highlightMatch(item.title || 'Ohne Titel', q)}</div>
              <div class="search-result-desc">Serie: ${escapeHtml(item.category)}</div>
            </div>
          </a>
        `;
      });
      html += '</div>';
    }

    html += `<a class="search-see-all" href="search.html?q=${encodeURIComponent(q)}">Alle Suchergebnisse anzeigen →</a>`;
    searchDropdown.innerHTML = html;
    searchDropdown.classList.add('open');
  }

  // --- Dedicated Search Page Logic ---
  if (searchResultsGrid && searchStats) {
    const params = new URLSearchParams(window.location.search);
    const initialQuery = params.get('q') || '';
    if (searchPageInput) {
      searchPageInput.value = initialQuery;
      searchPageInput.addEventListener('input', runDedicatedSearch);
    }
    if (categoryFilter) {
      categoryFilter.addEventListener('change', runDedicatedSearch);
    }
    runDedicatedSearch();
  }

  function runDedicatedSearch() {
    if (!searchResultsGrid) return;
    const rawQ = (searchPageInput ? searchPageInput.value : '').trim();
    const nq = normalizeSearchText(rawQ);
    const cat = categoryFilter ? categoryFilter.value : '';

    // Search text in pages
    let matchedPages = [];
    if (nq && !cat) {
      matchedPages = searchData.pages.filter(p => {
        const nt = normalizeSearchText(p.title);
        const nx = normalizeSearchText(p.text);
        return nt.includes(nq) || nx.includes(nq);
      });
    }

    // Search artworks
    let matchedArtworks = searchData.items.filter(item => {
      const matchCat = !cat || item.category === cat;
      if (!matchCat) return false;
      if (!nq) return true;
      const nt = normalizeSearchText(item.title);
      const nc = normalizeSearchText(item.category);
      const np = normalizeSearchText(item.caption);
      return nt.includes(nq) || nc.includes(nq) || np.includes(nq);
    });

    searchStats.textContent = `${matchedArtworks.length} Kunstwerk(e) gefunden${rawQ ? ` für "${rawQ}"` : ''}${cat ? ` in "${cat}"` : ''}`;

    // Render Text Results if any
    if (searchTextResults) {
      if (matchedPages.length > 0) {
        let textHtml = `<div class="search-group-title" style="padding-left:0; margin-bottom:12px;">Passende Seiten & Textabschnitte (${matchedPages.length})</div>`;
        matchedPages.forEach(p => {
          let snippet = p.text ? p.text.substring(0, 240) + '...' : '';
          textHtml += `
            <a class="search-text-item" href="${p.filename}">
              <div class="search-text-title">
                <span>${highlightMatch(p.title, rawQ)}</span>
                <span class="nav-badge">${escapeHtml(p.badge)}</span>
              </div>
              <div class="search-text-snippet">${highlightMatch(snippet, rawQ)}</div>
            </a>
          `;
        });
        searchTextResults.innerHTML = textHtml;
        searchTextResults.style.display = 'block';
      } else {
        searchTextResults.innerHTML = '';
        searchTextResults.style.display = 'none';
      }
    }

    if (matchedArtworks.length === 0) {
      searchResultsGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: var(--text-muted);">
          <div style="font-size: 2.5rem; margin-bottom: 12px;">🎨</div>
          <h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 8px;">Keine Kunstwerke gefunden</h3>
          <p>Versuchen Sie es mit einem anderen Begriff wie "0445", "Genesis", "Elemente", oder wählen Sie "Alle Kategorien".</p>
        </div>
      `;
      return;
    }

    // Prepare gallery list for Lightbox in search results
    currentGalleryItems = matchedArtworks.map(m => ({
      title: m.title,
      category: m.category,
      full: m.full || m.full_url || m.thumb,
      full_url: m.full || m.full_url || m.thumb,
      thumb: m.thumb || m.thumb_url || m.full,
      thumb_url: m.thumb || m.thumb_url || m.full,
      caption: m.caption
    }));

    let html = '';
    matchedArtworks.forEach((item, idx) => {
      const fullUrl = item.full || item.full_url || item.thumb || item.thumb_url;
      const thumbUrl = item.thumb || item.thumb_url || fullUrl;
      html += `
        <a class="artwork-card" href="${fullUrl}" data-index="${idx}" onclick="event.preventDefault(); window.openLightbox(${idx});" target="_blank" rel="noopener">
          <div class="artwork-thumb-wrap">
            <img class="artwork-thumb" src="${thumbUrl}" alt="${escapeHtml(item.title)}" loading="lazy">
            <div class="artwork-zoom-overlay">
              <span class="zoom-overlay-badge">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                Ganzes Bild ansehen
              </span>
            </div>
          </div>
          <div class="artwork-info">
            <div class="artwork-title">${highlightMatch(item.title || 'Ohne Titel', rawQ)}</div>
            <div class="artwork-category">${escapeHtml(item.category)}</div>
          </div>
        </a>
      `;
    });
    searchResultsGrid.innerHTML = html;
  }

  // --- Lightbox Functions for Whole Image Display ---
  window.initGallery = function(items) {
    currentGalleryItems = items.map(it => ({
      title: it.title || '',
      category: it.category || '',
      full: it.full || it.full_url || it.thumb || it.thumb_url,
      full_url: it.full || it.full_url || it.thumb || it.thumb_url,
      thumb: it.thumb || it.thumb_url || it.full || it.full_url,
      thumb_url: it.thumb || it.thumb_url || it.full || it.full_url,
      caption: it.caption || ''
    }));
  };

  window.openLightbox = function(index) {
    if (!currentGalleryItems || !currentGalleryItems[index]) return;
    currentIndex = index;
    isZoomed = false;
    updateLightboxUI();
    if (lightboxModal) {
      lightboxModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  };

  function updateLightboxUI() {
    const item = currentGalleryItems[currentIndex];
    if (!item) return;

    // Reset zoom state
    if (lightboxStage) {
      lightboxStage.classList.remove('zoomed');
      lightboxStage.scrollLeft = 0;
      lightboxStage.scrollTop = 0;
    }
    if (lightboxZoomBtn) {
      lightboxZoomBtn.classList.remove('active');
      lightboxZoomBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg> 100% Zoom';
    }
    isZoomed = false;

    // The whole high-resolution image!
    const fullSrc = item.full || item.full_url || item.thumb || item.thumb_url;

    if (lightboxImg) {
      lightboxImg.style.opacity = '0.3';
      const imgLoader = new Image();
      imgLoader.onload = function() {
        lightboxImg.src = fullSrc;
        lightboxImg.style.opacity = '1';
      };
      imgLoader.onerror = function() {
        lightboxImg.src = fullSrc;
        lightboxImg.style.opacity = '1';
      };
      imgLoader.src = fullSrc;
    }

    if (lightboxTitle) lightboxTitle.textContent = item.title || 'AnnaLis Gadea Werk';
    if (lightboxCategory) lightboxCategory.textContent = item.category || 'Werkdokumentation';
    if (lightboxCounter) lightboxCounter.textContent = `${currentIndex + 1} / ${currentGalleryItems.length}`;
    if (lightboxOpenFull) {
      lightboxOpenFull.href = fullSrc;
    }
  }

  function closeLightbox() {
    if (lightboxModal) {
      lightboxModal.classList.remove('open');
      document.body.style.overflow = '';
    }
    if (lightboxStage) {
      lightboxStage.classList.remove('zoomed');
      lightboxStage.scrollLeft = 0;
      lightboxStage.scrollTop = 0;
    }
    isZoomed = false;
    if (lightboxImg) lightboxImg.src = '';
  }

  function toggleZoom() {
    isZoomed = !isZoomed;
    if (lightboxStage) {
      lightboxStage.classList.toggle('zoomed', isZoomed);
      if (isZoomed && lightboxImg) {
        // Center zoomed image initially
        setTimeout(() => {
          const extraX = (lightboxImg.offsetWidth - lightboxStage.clientWidth) / 2;
          const extraY = (lightboxImg.offsetHeight - lightboxStage.clientHeight) / 2;
          if (extraX > 0) lightboxStage.scrollLeft = extraX;
          if (extraY > 0) lightboxStage.scrollTop = extraY;
        }, 50);
      }
    }
    if (lightboxZoomBtn) {
      lightboxZoomBtn.classList.toggle('active', isZoomed);
      lightboxZoomBtn.innerHTML = isZoomed ?
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 14 10 14 10 20"></polyline><polyline points="20 10 14 10 14 4"></polyline><line x1="14" y1="10" x2="21" y2="3"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg> Einpassen' :
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg> 100% Zoom';
    }
  }

  // Drag to pan in zoom mode
  if (lightboxStage) {
    lightboxStage.addEventListener('mousedown', function(e) {
      if (!isZoomed) return;
      isMouseDown = true;
      hasDragged = false;
      startX = e.pageX - lightboxStage.offsetLeft;
      startY = e.pageY - lightboxStage.offsetTop;
      scrollLeft = lightboxStage.scrollLeft;
      scrollTop = lightboxStage.scrollTop;
    });

    lightboxStage.addEventListener('mouseleave', function() {
      isMouseDown = false;
    });

    lightboxStage.addEventListener('mouseup', function() {
      isMouseDown = false;
    });

    lightboxStage.addEventListener('mousemove', function(e) {
      if (!isMouseDown || !isZoomed) return;
      e.preventDefault();
      const x = e.pageX - lightboxStage.offsetLeft;
      const y = e.pageY - lightboxStage.offsetTop;
      const walkX = (x - startX) * 1.5;
      const walkY = (y - startY) * 1.5;
      if (Math.abs(walkX) > 4 || Math.abs(walkY) > 4) {
        hasDragged = true;
      }
      lightboxStage.scrollLeft = scrollLeft - walkX;
      lightboxStage.scrollTop = scrollTop - walkY;
    });
  }

  // Lightbox Event Listeners
  if (lightboxCloseBtn) lightboxCloseBtn.addEventListener('click', closeLightbox);
  if (lightboxZoomBtn) lightboxZoomBtn.addEventListener('click', toggleZoom);

  if (lightboxImg) {
    lightboxImg.addEventListener('click', function(e) {
      e.stopPropagation();
      if (!hasDragged) {
        toggleZoom();
      }
    });
  }

  if (lightboxModal) {
    lightboxModal.addEventListener('click', function(e) {
      if (e.target === lightboxModal || e.target === lightboxStage) {
        closeLightbox();
      }
    });
  }

  if (lightboxPrevBtn) {
    lightboxPrevBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = currentGalleryItems.length - 1;
      }
      updateLightboxUI();
    });
  }

  if (lightboxNextBtn) {
    lightboxNextBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (currentIndex < currentGalleryItems.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      updateLightboxUI();
    });
  }

  // Keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (!lightboxModal || !lightboxModal.classList.contains('open')) return;
    if (e.key === 'Escape') {
      closeLightbox();
    } else if (e.key === 'ArrowLeft') {
      if (lightboxPrevBtn) lightboxPrevBtn.click();
    } else if (e.key === 'ArrowRight') {
      if (lightboxNextBtn) lightboxNextBtn.click();
    } else if (e.key === 'z' || e.key === 'Z') {
      toggleZoom();
    }
  });

  // Touch Swipe for Mobile Lightbox
  let touchStartX = 0;
  let touchEndX = 0;
  if (lightboxStage) {
    lightboxStage.addEventListener('touchstart', function(e) {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    lightboxStage.addEventListener('touchend', function(e) {
      touchEndX = e.changedTouches[0].screenX;
      if (isZoomed) return;
      if (touchStartX - touchEndX > 50) {
        if (lightboxNextBtn) lightboxNextBtn.click();
      } else if (touchEndX - touchStartX > 50) {
        if (lightboxPrevBtn) lightboxPrevBtn.click();
      }
    }, { passive: true });
  }

  // Language Tabs Switcher on Homepage
  window.switchLang = function(lang) {
    document.querySelectorAll('.lang-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });
    document.querySelectorAll('.lang-pane').forEach(pane => {
      pane.classList.toggle('active', pane.getAttribute('data-lang') === lang);
    });
  };

  // Helper functions
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function highlightMatch(text, query) {
    if (!query || !text) return escapeHtml(text);
    const escaped = escapeHtml(text);
    const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return escaped.replace(regex, '<mark style="background: rgba(245, 158, 11, 0.35); color: #ffffff; padding: 1px 4px; border-radius: 3px;">$1</mark>');
  }

})();
"""

def get_clean_title(raw_title):
    t = raw_title.replace("Annalis Gadea – ", "").replace("Annalis Gadea - ", "").strip()
    if t == "Annalis Gadea" or not t:
        return "Übersicht & Biografie"
    return t

def render_sidebar(active_slug, categories):
    links_html = []
    
    # Overview
    is_home = active_slug in ["index", "annalis-gadea", ""]
    home_active = "active" if is_home else ""
    links_html.append(f"""
      <a class="nav-link {home_active}" href="index.html">
        <span class="nav-link-title">🏠 Übersicht & Biografie</span>
      </a>
    """)

    # Search
    search_active = "active" if active_slug == "search" else ""
    links_html.append(f"""
      <a class="nav-link {search_active}" href="search.html">
        <span class="nav-link-title">🔍 Suche im Werk</span>
      </a>
    """)

    links_html.append("""<div class="nav-section-title">Bilderserien & Galerien (19)</div>""")

    for cat in categories:
        slug = cat["slug"]
        c_active = "active" if active_slug == slug else ""
        c_title = cat["display_title"]
        count = len(cat.get("items", []))
        links_html.append(f"""
      <a class="nav-link {c_active}" href="{cat['filename']}">
        <span class="nav-link-title">{html.escape(c_title)}</span>
        <span class="nav-badge">{count}</span>
      </a>
        """)

    return f"""
  <aside class="app-sidebar">
    <div class="sidebar-header">
      <a class="sidebar-logo" href="index.html">
        <div class="sidebar-title">AnnaLis Gadea</div>
        <div class="sidebar-subtitle">Werkdokumentation</div>
        <div class="sidebar-meta">✶ 1946 † 2023 · Luzern, Schweiz</div>
      </a>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section-title">Dokumentation</div>
      {"".join(links_html)}
    </nav>
    <div class="sidebar-footer">
      <span>574 Kunstwerke</span>
      <span>Vollversion Offline</span>
    </div>
  </aside>
"""

def render_header(active_title=""):
    return f"""
    <header class="top-header">
      <button id="mobileNavToggle" class="mobile-nav-toggle" aria-label="Menü öffnen">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
      
      <div class="header-search-wrapper">
        <svg class="search-input-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" id="headerSearchInput" class="header-search-input" placeholder="Suche im Werk (z.B. 0445, Genesis, Luzern, Acryl)..." autocomplete="off" aria-label="Suche">
        <div id="searchDropdown" class="search-dropdown"></div>
      </div>

      <div class="header-quick-links">
        <a class="quick-link-btn" href="search.html">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          Suche
        </a>
        <a class="quick-link-btn" href="index.html">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          Übersicht
        </a>
      </div>
    </header>
"""

def render_lightbox_modal():
    return """
  <!-- Lightbox Modal for High-Resolution Whole Image Display -->
  <div id="lightboxModal" class="lightbox-modal" role="dialog" aria-modal="true" aria-label="Ganzes Bild ansehen">
    <div class="lightbox-header">
      <div class="lightbox-meta">
        <span id="lightboxTitle" class="lightbox-title">0000n</span>
        <span id="lightboxCategory" class="lightbox-badge">Serie</span>
        <span id="lightboxCounter" class="lightbox-counter">1 / 1</span>
      </div>
      <div class="lightbox-actions">
        <button id="lightboxZoomBtn" class="lightbox-btn" title="Zwischen Bildschirmgröße und 100% Originalauflösung umschalten">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
          100% Zoom
        </button>
        <a id="lightboxOpenFull" class="lightbox-btn" href="#" target="_blank" rel="noopener" title="Ganzes hochauflösendes Originalbild in neuem Tab öffnen">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          Originaldatei
        </a>
        <button id="lightboxCloseBtn" class="lightbox-btn lightbox-btn-close" title="Schließen (Esc)">&times;</button>
      </div>
    </div>
    <div id="lightboxStage" class="lightbox-stage">
      <button id="lightboxPrevBtn" class="lightbox-arrow prev" title="Vorheriges Bild (Pfeil links)">&#10094;</button>
      <div class="lightbox-img-wrapper">
        <img id="lightboxImg" class="lightbox-img" src="" alt="AnnaLis Gadea Werkansicht">
      </div>
      <button id="lightboxNextBtn" class="lightbox-arrow next" title="Nächstes Bild (Pfeil rechts)">&#10095;</button>
      <div class="lightbox-hint">
        <span>Klick auf Bild für 100% Zoom</span>
        <span>Pfeiltasten zum Blättern</span>
        <span>Esc zum Schließen</span>
      </div>
    </div>
  </div>
"""

def generate_index_html(bio_page, categories):
    paragraphs = bio_page.get("paragraphs", [])
    
    # Split paragraphs into German and English
    de_paras = []
    en_paras = []
    
    current_target = de_paras
    for p in paragraphs:
        if "Whatever I cannot describe in words" in p:
            current_target = en_paras
        current_target.append(p)

    # Categories explorer cards
    cat_cards_html = []
    for cat in categories:
        items = cat.get("items", [])
        thumb = items[0]["thumb_url"] if items else "images/image.png"
        count = len(items)
        cat_cards_html.append(f"""
        <a class="category-card" href="{cat['filename']}">
          <div class="category-card-thumb-wrap">
            <img class="category-card-thumb" src="{thumb}" alt="{html.escape(cat['display_title'])}" loading="lazy">
          </div>
          <div class="category-card-body">
            <div class="category-card-title">{html.escape(cat['display_title'])}</div>
            <span class="category-card-badge">{count} Werke</span>
          </div>
        </a>
        """)

    # German content rendering
    de_html = []
    for p in de_paras:
        if p.startswith("Über AnnaLis Gadea"):
            continue
        elif "„Was ich nicht in Worte fassen kann" in p:
            de_html.append(f"""<div class="bio-quote">{html.escape(p)}</div>""")
        elif p.startswith("Werk"):
            body = p.replace("Werk", "", 1).strip()
            de_html.append(f"""
              <div class="bio-section-box">
                <div class="bio-section-heading">🎨 Werk</div>
                <div class="bio-section-text">{html.escape(body)}</div>
              </div>
            """)
        elif p.startswith("Lebenslauf"):
            body = p.replace("Lebenslauf", "", 1).strip()
            de_html.append(f"""
              <div class="bio-section-box">
                <div class="bio-section-heading">📜 Lebenslauf</div>
                <div class="bio-section-text">{html.escape(body)}</div>
              </div>
            """)
        elif p.startswith("Web-Galerie"):
            body = p.replace("Web-Galerie", "", 1).strip()
            de_html.append(f"""
              <div class="bio-section-box">
                <div class="bio-section-heading">🖼️ Web-Galerie</div>
                <div class="bio-section-text">{html.escape(body)}</div>
              </div>
            """)
        else:
            de_html.append(f"""<p class="bio-section-text" style="margin-bottom:12px;">{html.escape(p)}</p>""")

    # English content rendering
    en_html = []
    for p in en_paras:
        if "Whatever I cannot describe in words" in p:
            en_html.append(f"""<div class="bio-quote">{html.escape(p)}</div>""")
        elif p.startswith("Works"):
            body = p.replace("Works", "", 1).strip()
            en_html.append(f"""
              <div class="bio-section-box">
                <div class="bio-section-heading">🎨 Works</div>
                <div class="bio-section-text">{html.escape(body)}</div>
              </div>
            """)
        elif p.startswith("Curriculum vitae"):
            body = p.replace("Curriculum vitae", "", 1).strip()
            en_html.append(f"""
              <div class="bio-section-box">
                <div class="bio-section-heading">📜 Curriculum Vitae</div>
                <div class="bio-section-text">{html.escape(body)}</div>
              </div>
            """)
        elif p.startswith("Web-Gallery"):
            body = p.replace("Web-Gallery", "", 1).strip()
            en_html.append(f"""
              <div class="bio-section-box">
                <div class="bio-section-heading">🖼️ Web-Gallery</div>
                <div class="bio-section-text">{html.escape(body)}</div>
              </div>
            """)
        else:
            en_html.append(f"""<p class="bio-section-text" style="margin-bottom:12px;">{html.escape(p)}</p>""")

    sidebar = render_sidebar("index", categories)
    header = render_header("Übersicht & Biografie")
    lightbox = render_lightbox_modal()

    # portrait data for lightbox
    portrait_item_json = json.dumps([{
        "title": "AnnaLis Gadea (Porträt)",
        "category": "Biografie",
        "full_url": "images/image.png",
        "thumb_url": "images/image.png",
        "full": "images/image.png",
        "thumb": "images/image.png",
        "caption": "AnnaLis Gadea (1946 – 2023)"
    }])

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AnnaLis Gadea – Werkdokumentation & Web-Galerie</title>
  <link rel="stylesheet" href="style.css">
  <script src="search_data.js"></script>
</head>
<body>

  {sidebar}

  <main class="app-main">
    {header}

    <div class="page-container">
      
      <section class="bio-hero-card">
        <div class="bio-portrait-wrap" onclick="window.openLightbox(0)" title="Klicken für Vollbild-Ansicht des Porträts">
          <img class="bio-portrait" src="images/image.png" alt="AnnaLis Gadea">
          <div class="bio-portrait-badge">🔍 Vollbild anzeigen</div>
        </div>
        <div class="bio-intro-content">
          <h1 class="bio-name">AnnaLis Gadea</h1>
          <div class="bio-dates">
            <span>✶ 1946</span>
            <span>·</span>
            <span>† 05. Mai 2023</span>
            <span>·</span>
            <span style="color:var(--text-secondary); font-size: 0.95rem;">Luzern, Schweiz</span>
          </div>
          <p style="color:var(--text-secondary); font-size:1.02rem;">
            Gesamtdokumentation des künstlerischen Schaffens mit über 1’500 Gemälden, Studien und Zeichnungen aus fünf Jahrzehnten (1968–2023).
          </p>

          <div class="lang-tabs">
            <button class="lang-tab-btn active" data-lang="de" onclick="switchLang('de')">🇩🇪 Deutsch</button>
            <button class="lang-tab-btn" data-lang="en" onclick="switchLang('en')">🇬🇧 English</button>
          </div>

          <div class="lang-pane active" data-lang="de">
            {"".join(de_html)}
          </div>

          <div class="lang-pane" data-lang="en">
            {"".join(en_html)}
          </div>
        </div>
      </section>

      <div class="section-title-wrap">
        <div>
          <h2 class="section-main-title">Entdecken Sie alle 19 Werkserien</h2>
          <p style="color:var(--text-secondary); margin-top:4px;">574 erfasste Arbeiten in Acryl, Eitempera, Aquarell, Gouache, Bleistift und Fotobearbeitung.</p>
        </div>
        <a href="search.html" class="quick-link-btn" style="color:var(--accent);">Alle 574 Werke durchsuchen →</a>
      </div>

      <div class="categories-explorer-grid">
        {"".join(cat_cards_html)}
      </div>

    </div>
  </main>

  {lightbox}

  <script src="app.js"></script>
  <script>
    window.initGallery({portrait_item_json});
  </script>
</body>
</html>
"""

def generate_gallery_html(category, categories):
    items = category.get("items", [])
    slug = category["slug"]
    title = category["display_title"]
    count = len(items)

    cards_html = []
    for idx, it in enumerate(items):
        t = it.get("title", f"Werk {idx+1}")
        full = it.get("full_url", it.get("thumb_url", ""))
        thumb = it.get("thumb_url", full)
        cards_html.append(f"""
        <a class="artwork-card" href="{full}" data-index="{idx}" onclick="event.preventDefault(); window.openLightbox({idx});" target="_blank" rel="noopener">
          <div class="artwork-thumb-wrap">
            <img class="artwork-thumb" src="{thumb}" alt="{html.escape(t)}" loading="lazy">
            <div class="artwork-zoom-overlay">
              <span class="zoom-overlay-badge">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                Ganzes Bild ansehen
              </span>
            </div>
          </div>
          <div class="artwork-info">
            <div class="artwork-title">{html.escape(t)}</div>
            <div class="artwork-category">{html.escape(title)}</div>
          </div>
        </a>
        """)

    # Gallery items JSON for JavaScript Lightbox
    items_json = []
    for it in items:
        items_json.append({
            "title": it.get("title", ""),
            "category": title,
            "full_url": it.get("full_url", it.get("thumb_url", "")),
            "thumb_url": it.get("thumb_url", it.get("full_url", "")),
            "full": it.get("full_url", it.get("thumb_url", "")),
            "thumb": it.get("thumb_url", it.get("full_url", "")),
            "caption": it.get("caption", "")
        })

    sidebar = render_sidebar(slug, categories)
    header = render_header(title)
    lightbox = render_lightbox_modal()

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AnnaLis Gadea – {html.escape(title)}</title>
  <link rel="stylesheet" href="style.css">
  <script src="search_data.js"></script>
</head>
<body>

  {sidebar}

  <main class="app-main">
    {header}

    <div class="page-container">
      <section class="page-hero">
        <div>
          <h1 class="page-title">{html.escape(title)}</h1>
          <div class="page-meta" style="margin-top:6px;">
            <span>Künstlerin: AnnaLis Gadea</span>
            <span>·</span>
            <span>Kategorie: {html.escape(title)}</span>
          </div>
        </div>
        <div class="page-meta-badge">{count} Gemälde & Arbeiten</div>
      </section>

      <div class="artwork-grid">
        {"".join(cards_html)}
      </div>
    </div>
  </main>

  {lightbox}

  <script src="app.js"></script>
  <script>
    window.initGallery({json.dumps(items_json)});
  </script>
</body>
</html>
"""

def generate_search_html(categories):
    cat_options = ["""<option value="">Alle Kategorien (574 Kunstwerke)</option>"""]
    for cat in categories:
        count = len(cat.get("items", []))
        cat_options.append(f"""<option value="{html.escape(cat['display_title'])}">{html.escape(cat['display_title'])} ({count})</option>""")

    sidebar = render_sidebar("search", categories)
    header = render_header("Suche im Werk")
    lightbox = render_lightbox_modal()

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AnnaLis Gadea – Suche im Gesamtwerk</title>
  <link rel="stylesheet" href="style.css">
  <script src="search_data.js"></script>
</head>
<body>

  {sidebar}

  <main class="app-main">
    {header}

    <div class="page-container">
      <section class="page-hero">
        <div>
          <h1 class="page-title">Suche im Gesamtkatalog</h1>
          <p style="color:var(--text-secondary); margin-top:6px;">
            Durchsuchen Sie alle 574 Werke nach Katalognummer (z.B. 0132, 0445, 0986), Serie, Biografie oder Thema.
          </p>
        </div>
      </section>

      <div class="search-controls-box">
        <div class="search-field-wrap">
          <svg class="search-field-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" id="searchPageInput" class="search-field-input" placeholder="Suchbegriff eingeben (z.B. 0132, Genesis, Toscana, Luzern, Acryl)..." autofocus>
        </div>
        <select id="categoryFilter" class="category-select">
          {"".join(cat_options)}
        </select>
      </div>

      <div class="search-stats-bar">
        <span id="searchStats">Wird geladen...</span>
      </div>

      <div id="searchTextResults" class="search-text-results" style="display:none;"></div>

      <div id="searchResultsGrid" class="artwork-grid">
        <!-- Results injected dynamically -->
      </div>
    </div>
  </main>

  {lightbox}

  <script src="app.js"></script>
</body>
</html>
"""

def generate_search_data_js(pages, categories):
    search_pages = []
    search_items = []

    for p in pages:
        slug = p["slug"]
        is_home = (slug == "annalis-gadea")
        badge = "Biografie & Übersicht" if is_home else "Galerieserie"
        filename = "index.html" if is_home else p.get("filename", f"{slug}.html")
        text = " ".join(p.get("paragraphs", []))
        search_pages.append({
            "slug": slug,
            "filename": filename,
            "title": p["title"],
            "badge": badge,
            "text": text
        })

    # Collect artworks
    for cat in categories:
        cat_title = cat["display_title"]
        for it in cat.get("items", []):
            full = it.get("full_url", it.get("thumb_url", ""))
            thumb = it.get("thumb_url", full)
            search_items.append({
                "page_slug": cat["slug"],
                "page_filename": cat["filename"],
                "category": cat_title,
                "title": it.get("title", ""),
                "caption": it.get("caption", ""),
                "thumb": thumb,
                "thumb_url": thumb,
                "full": full,
                "full_url": full
            })

    # Also add portrait image to searchable items
    search_items.insert(0, {
        "page_slug": "annalis-gadea",
        "page_filename": "index.html",
        "category": "Biografie",
        "title": "AnnaLis Gadea Porträt",
        "caption": "Porträt AnnaLis Gadea (1946 – 2023)",
        "thumb": "images/image.png",
        "thumb_url": "images/image.png",
        "full": "images/image.png",
        "full_url": "images/image.png"
    })

    data_obj = {
        "pages": search_pages,
        "items": search_items
    }

    return f"window.SEARCH_DATA = {json.dumps(data_obj, ensure_ascii=False, indent=2)};\n"

def build_documentation():
    print(f"Loading data from {DATA_SOURCE}...")
    with open(DATA_SOURCE, "r", encoding="utf-8") as f:
        all_pages = json.load(f)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    # Separate home page vs 19 gallery pages
    bio_page = all_pages[0]
    categories = []
    for p in all_pages[1:]:
        p["display_title"] = get_clean_title(p["title"])
        p["filename"] = f"{p['slug']}.html"
        categories.append(p)

    print(f"Loaded {len(categories)} gallery categories and 1 biography page.")

    # 1. Write style.css
    css_path = os.path.join(OUTPUT_DIR, "style.css")
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(CSS_CONTENT)
    print("style.css written.")

    # 2. Write app.js
    js_path = os.path.join(OUTPUT_DIR, "app.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(JS_CONTENT)
    print("app.js written.")

    # 3. Write search_data.js
    search_js_path = os.path.join(OUTPUT_DIR, "search_data.js")
    search_js_content = generate_search_data_js(all_pages, categories)
    with open(search_js_path, "w", encoding="utf-8") as f:
        f.write(search_js_content)
    print("search_data.js written.")

    # 4. Write index.html and annalis-gadea.html
    index_html = generate_index_html(bio_page, categories)
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    
    # alias annalis-gadea.html
    alias_path = os.path.join(OUTPUT_DIR, "annalis-gadea.html")
    with open(alias_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("index.html and annalis-gadea.html written.")

    # 5. Write search.html
    search_html = generate_search_html(categories)
    search_path = os.path.join(OUTPUT_DIR, "search.html")
    with open(search_path, "w", encoding="utf-8") as f:
        f.write(search_html)
    print("search.html written.")

    # 6. Write all 19 gallery pages
    for cat in categories:
        gal_html = generate_gallery_html(cat, categories)
        gal_path = os.path.join(OUTPUT_DIR, cat["filename"])
        with open(gal_path, "w", encoding="utf-8") as f:
            f.write(gal_html)
        print(f"Generated {cat['filename']} ({len(cat.get('items', []))} works)")

    print(f"\nAll documentation successfully generated into: {OUTPUT_DIR}")

if __name__ == "__main__":
    build_documentation()
