# 📈 TickerGrid Project Roadmap

**Project Vision:** A clean, minimalist Scandinavian-style investment hub for tracking Danish and International holdings with integrated news and note-taking.

---

## 🏗️ Epic 1: The Foundation (Backend & Infrastructure)

### ID: [TG-101] — Core API Setup
* **User Story:** As a dev, I want a FastAPI server so that the frontend can request market data.
* **Functional Requirements:**
    * Server must handle requests from `localhost:3000`.
    * A "Health Check" endpoint at `/`.
* **Tech Hints:** Use `CORSMiddleware`. Ensure `uvicorn` is used for the dev server.
* **Status:** [x] Backlog

### ID: [TG-102] — Data Persistence (SQLite)
* **User Story:** As an investor, I want my stocks and notes saved so I don't lose them on refresh.
* **Functional Requirements:**
    * Create a local `database.db` file.
    * Define schema for Tickers (symbol, name, type, is_owned).
    * Define schema for Notes (linked to ticker symbol).
* **Tech Hints:** Use SQLAlchemy `declarative_base`. Establish a One-to-Many relationship between Tickers and Notes.
* **Status:** [ ] Backlog

### ID: [TG-103] — Market Data Engine
* **User Story:** As an investor, I want real-time prices so I can see my portfolio value.
* **Functional Requirements:**
    * Fetch current price, currency, and daily change.
    * Fetch dividend yield data for Chowder calculations.
* **Tech Hints:** Wrap `yfinance.Ticker(symbol)` in a service function. Add error handling for invalid symbols.
* **Status:** [ ] Backlog

---

## 🗂️ Epic 2: The Grid (Portfolio & Watchlist)

### ID: [TG-201] — Manual Entry Interface
* **User Story:** As an investor, I want to add my Saxo/Nordnet stocks manually so I can start tracking them.
* **Functional Requirements:**
    * Form field for ticker symbol (auto-uppercase).
    * Dropdown/Toggle for Asset Type (Stock vs ETF).
* **Tech Hints:** `POST` request to `/tickers`. Validate symbol exists via `yfinance` before saving.
* **Status:** [ ] Backlog

### ID: [TG-202] — The TickerGrid View
* **User Story:** As an investor, I want a clean minimalist overview of my assets so I can see my performance at a glance.
* **Functional Requirements:**
    * Display tickers in a responsive grid or list.
    * Color-coded daily changes (Scandi-style: subtle Emerald for up, soft Rose/Gray for down).
* **Tech Hints:** Map through ticker array in React. Use CSS Modules for the "Clean" look.
* **Status:** [ ] Backlog

### ID: [TG-203] — Watchlist Logic
* **User Story:** As an investor, I want to separate things I own from things I'm watching so my actual portfolio stays clean.
* **Functional Requirements:**
    * Toggle switch on each ticker to move it between "Holding" and "Watching".
    * Filter the main view based on this status.
* **Tech Hints:** Add a boolean `is_owned` to the database model.
* **Status:** [ ] Backlog

---

## 📰 Epic 3: Intelligence & News

### ID: [TG-301] — Toggled News Feed
* **User Story:** As an investor, I want to switch between news for my portfolio and my watchlist so I can focus on specific info.
* **Functional Requirements:**
    * Fetch recent news articles for multiple symbols.
    * UI toggle to swap between the two data sets.
* **Tech Hints:** Use `ticker.news` on the backend. Aggregate news into a single list sorted by date.
* **Status:** [ ] Backlog

### ID: [TG-302] — Chowder Analytics Integration
* **User Story:** As an investor, I want to see a stock's Chowder Score to judge its dividend quality.
* **Functional Requirements:**
    * Calculate: Current Yield + 5-Year Dividend Growth Rate.
    * Display the result with a "Quality" badge.
* **Tech Hints:** Fetch `dividendRate` and historical dividends from `yfinance`.
* **Status:** [ ] Backlog

---

## 📝 Epic 4: Ticker Notepad (Work in Progress)

### ID: [TG-401] — Contextual Note-Taking
* **User Story:** As an investor, I want to save my research directly on a stock's profile so I remember why I like it.
* **Functional Requirements:**
    * Autosaving text area for each ticker.
    * Timestamp for when the note was last updated.
* **Tech Hints:** Use a `debounce` function in React to avoid hitting the database on every keystroke.
* **Status:** [ ] Backlog

---

## 🎨 Epic 5: UX & Design System

### ID: [TG-501] — Scandi-Minimalist Light Mode
* **User Story:** As a user, I want a clean, airy interface so that I don't feel overwhelmed by data.
* **Functional Requirements:**
    * High white space, sans-serif typography (Inter/Geist).
    * Minimalist borders instead of heavy shadows.
* **Tech Hints:** Define a global CSS variable set for colors: `--bg-primary`, `--text-main`, `--accent-emerald`.
* **Status:** [ ] Backlog

### ID: [TG-502] — Dark Mode Implementation
* **User Story:** As a user, I want a dark version for nighttime research.
* **Functional Requirements:**
    * Implementation of theme switching using CSS variables.
* **Status:** [ ] Backlog
