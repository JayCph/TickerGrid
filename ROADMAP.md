# 📈 TickerGrid Project Roadmap

**Project Vision:** A clean, minimalist Scandinavian-style investment hub for tracking Danish and International holdings with integrated news and note-taking.

---

## 🏗️ Epic 1: The Foundation (Backend & Infrastructure)
- [ ] **[TG-101] Core API Setup**
    * **Story:** As a dev, I want a FastAPI server so that the frontend can request market data.
    * **Tasks:** Initialize FastAPI, set up CORS for `localhost:3000`.
- [ ] **[TG-102] Data Persistence (SQLite)**
    * **Story:** As an investor, I want my stocks and notes saved so I don't lose them on refresh.
    * **Tasks:** Set up SQLAlchemy models for `Ticker` and `Note`.
- [ ] **[TG-103] Market Data Engine**
    * **Story:** As an investor, I want real-time prices so I can see my portfolio value.
    * **Tasks:** Integrate `yfinance` for price and dividend yield fetching.

---

## 🗂️ Epic 2: The Grid (Portfolio & Watchlist)
- [ ] **[TG-201] Manual Entry Interface**
    * **Story:** As an investor, I want to add my Saxo/Nordnet stocks manually.
    * **Tasks:** Create a form to input Symbol, Type (Stock/ETF), and Category.
- [ ] **[TG-202] The TickerGrid View**
    * **Story:** As an investor, I want a clean minimalist overview of my assets.
    * **Tasks:** Build the primary Scandi-style grid/list component.
- [ ] **[TG-203] Watchlist Logic**
    * **Story:** As an investor, I want to separate things I own from things I'm watching.
    * **Tasks:** Add a `status` toggle (Owned vs. Watching) to the database.

---

## 📰 Epic 3: Intelligence & News
- [ ] **[TG-301] Toggled News Feed**
    * **Story:** As an investor, I want to switch between news for my portfolio and my watchlist.
    * **Tasks:** Build a news component with a toggle switch using `yfinance.news`.
- [ ] **[TG-302] Chowder Analytics Integration**
    * **Story:** As an investor, I want to see a stock's Chowder Score to judge its quality.
    * **Tasks:** Implement the math logic for Dividend Yield + 5yr Dividend Growth.

---

## 📝 Epic 4: Ticker Notepad (Work in Progress)
- [ ] **[TG-401] Contextual Note-Taking**
    * **Story:** As an investor, I want to save my research directly on a stock's profile.
    * **Tasks:** Create a persistent text area that saves notes to the `Note` table.
- [ ] **[TG-402] Note Visibility**
    * **Story:** As an investor, I want my notes to follow the ticker from Watchlist to Portfolio.
    * **Tasks:** Link notes to ticker symbols globally.

---

## 🎨 Epic 5: UX & Design System
- [ ] **[TG-501] Scandi-Minimalist Light Mode**
    * **Story:** As a user, I want a clean, airy interface that feels modern.
    * **Tasks:** Define the CSS color palette (Whites, soft grays, Emerald accents).
- [ ] **[TG-502] Dark Mode Implementation**
    * **Story:** As a user, I want a dark version for nighttime research.
    * **Tasks:** CSS variables for theme switching.
