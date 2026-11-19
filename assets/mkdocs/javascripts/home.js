(() => {
  const initSearch = () => {
    const form = document.querySelector("[data-home-search]");
    if (!form) return;

    form.onsubmit = (event) => {
      event.preventDefault();
      const toggle = document.querySelector("[data-md-toggle='search']");
      const search = document.querySelector(".md-search__input");
      if (!toggle || !search) return;

      toggle.checked = true;
      toggle.dispatchEvent(new Event("change", { bubbles: true }));
      search.value = form.querySelector("input").value.trim();
      search.dispatchEvent(new Event("input", { bubbles: true }));
      search.focus();
    };
  };

  if (typeof document$ !== "undefined") {
    document$.subscribe(initSearch);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initSearch, { once: true });
  } else {
    initSearch();
  }
})();
