"use client";

export default function Home() {
  const handleSearch = (e) => {
    e.preventDefault();
    const ticker = e.target.ticker.value;
    console.log(`Searching for: ${ticker}`);
    //  fetching logic here
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <div className="flex flex-col gap-4 text-base font-medium sm:flex-row">
          <form
            onSubmit={handleSearch}
            className="flex flex-col sm:flex-row items-end gap-4"
          >
            <div className="flex flex-col">
              <label htmlFor="ticker" className="mb-1 text-sm">
                Ticker Symbol
              </label>
              <input
                type="text"
                name="ticker"
                id="ticker"
                className="h-12 border border-gray-300 rounded-md px-3 text-black dark:text-white dark:bg-zinc-800"
                placeholder="e.g. AAPL"
              />
            </div>
            <button
              type="submit"
              className="flex h-12 w-full items-center justify-center rounded-full border border-solid border-black/[.08] px-5 transition-colors hover:border-transparent hover:bg-black/[.04] dark:border-white/[.145] dark:hover:bg-[#1a1a1a] md:w-[158px]"
            >
              Find STOCK!
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}
