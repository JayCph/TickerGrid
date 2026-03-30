// app/page.tsx
"use client";

import styles from "./page.module.css";

export default function Home() {
  const handleSearch = (e) => {
    e.preventDefault();
    const ticker = e.target.ticker.value;
    console.log(`Calculating Chowder Score & metrics for: ${ticker}`);
    // Fetching logic here
  };

  return (
    <div className={styles.wrapper}>
      <main className={styles.mainCard}>
        <div className={styles.content}>
          <div>
            <h1 className={styles.title}>Stock Analyzer</h1>
            <p className={styles.subtitle}>
              Enter a ticker to evaluate its metrics and historical performance.
            </p>
          </div>

          <form onSubmit={handleSearch} className={styles.form}>
            <div className={styles.inputWrapper}>
              <label htmlFor="ticker" className={styles.label}>
                Ticker Symbol
              </label>
              <input
                type="text"
                name="ticker"
                id="ticker"
                className={styles.input}
                placeholder="e.g. QQQ or a high-quality dividend stock"
                autoComplete="off"
              />
            </div>

            <button type="submit" className={styles.button}>
              Analyze
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}
