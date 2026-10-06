/* ==========================================================================
   ANYopenSoft portal — progressive enhancement only.
   Every section of the page is fully readable without this script.
   JavaScript adds: responsive navigation toggle, project directory
   category filtering, text search, live result count and a zero-result
   state with a reset action. No dependencies, no build step.
   ========================================================================== */

(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  /* ------------------------- Navigation toggle ------------------------- */

  var navToggle = document.querySelector(".nav-toggle");
  var siteNav = document.getElementById("site-nav");

  function closeNav() {
    root.classList.remove("nav-open");
    if (navToggle) {
      navToggle.setAttribute("aria-expanded", "false");
    }
  }

  if (navToggle && siteNav) {
    navToggle.addEventListener("click", function () {
      var isOpen = root.classList.toggle("nav-open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    siteNav.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        closeNav();
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && root.classList.contains("nav-open")) {
        closeNav();
        navToggle.focus();
      }
    });
  }

  /* ------------------------- Project directory ------------------------- */

  var projectList = document.getElementById("project-list");
  var searchInput = document.getElementById("project-search");
  var filterButtons = Array.prototype.slice.call(
    document.querySelectorAll(".filter-btn")
  );
  var clearButtons = Array.prototype.slice.call(
    document.querySelectorAll(".clear-btn, [data-clear]")
  );
  var resultsStatus = document.querySelector(".results-status");
  var noResults = document.getElementById("no-results");

  if (!projectList || !searchInput || filterButtons.length === 0) {
    return;
  }

  var projects = Array.prototype.slice.call(
    projectList.querySelectorAll(".project")
  );
  var total = projects.length;
  var activeFilter = "all";
  var query = "";

  function projectText(project) {
    return (project.textContent || "")
      .toLowerCase()
      .replace(/\s+/g, " ")
      .trim();
  }

  var searchTexts = projects.map(projectText);

  function projectMatches(index) {
    if (activeFilter !== "all") {
      var categories = (projects[index].getAttribute("data-categories") || "")
        .split(/\s+/)
        .filter(Boolean);
      if (categories.indexOf(activeFilter) === -1) {
        return false;
      }
    }
    if (query) {
      return searchTexts[index].indexOf(query) !== -1;
    }
    return true;
  }

  function applyFilters() {
    var visible = 0;
    projects.forEach(function (project, index) {
      var matches = projectMatches(index);
      project.hidden = !matches;
      if (matches) {
        visible += 1;
      }
    });

    if (resultsStatus) {
      resultsStatus.textContent =
        "Showing " + visible + " of " + total + " repositories.";
    }

    if (noResults) {
      noResults.hidden = visible !== 0;
    }

    clearButtons.forEach(function (button) {
      button.hidden = activeFilter === "all" && !query;
    });
  }

  function resetFilters() {
    activeFilter = "all";
    query = "";
    searchInput.value = "";
    filterButtons.forEach(function (button) {
      var isActive = button.getAttribute("data-filter") === "all";
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });
    applyFilters();
  }

  filterButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      filterButtons.forEach(function (other) {
        other.classList.remove("is-active");
        other.setAttribute("aria-pressed", "false");
      });
      button.classList.add("is-active");
      button.setAttribute("aria-pressed", "true");
      activeFilter = button.getAttribute("data-filter") || "all";
      applyFilters();
    });
  });

  searchInput.addEventListener("input", function () {
    query = searchInput.value.toLowerCase().trim();
    applyFilters();
  });

  clearButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      resetFilters();
      searchInput.focus();
    });
  });

  applyFilters();
})();
