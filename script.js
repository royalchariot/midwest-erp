const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

const closeNavigation = () => {
  if (!navToggle || !navLinks) return;
  navToggle.setAttribute("aria-expanded", "false");
  navLinks.classList.remove("is-open");
};

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const isOpen = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!isOpen));
    navLinks.classList.toggle("is-open", !isOpen);
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement && window.innerWidth <= 1180) {
      closeNavigation();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeNavigation();
      navToggle.focus();
    }
  });

  document.addEventListener("click", (event) => {
    if (event.target instanceof Node && !navToggle.contains(event.target) && !navLinks.contains(event.target)) {
      closeNavigation();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 1180) closeNavigation();
  });
}

const normalizePath = (path) => {
  const clean = (path || "/").split("#")[0].split("?")[0];
  if (!clean || clean === "/index.html") return "/";
  return clean.endsWith("/index.html") ? clean.slice(0, -10) : clean;
};

const currentPath = normalizePath(window.location.pathname);
document.querySelectorAll(".nav-links a").forEach((link) => {
  const linkPath = normalizePath(link.getAttribute("href"));
  if (linkPath === currentPath || (linkPath !== "/" && currentPath.startsWith(linkPath))) {
    link.setAttribute("aria-current", "page");
  }
});

document.querySelectorAll("[data-tabs]").forEach((tabs) => {
  const buttons = [...tabs.querySelectorAll("[data-tab-target]")];
  const panels = [...document.querySelectorAll("[data-tab-panel]")];

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const target = button.dataset.tabTarget;
      buttons.forEach((item) => item.setAttribute("aria-selected", String(item === button)));
      panels.forEach((panel) => panel.classList.toggle("is-active", panel.dataset.tabPanel === target));
    });
  });
});

const assistantRecommendations = {
  select: {
    title: "ERP Selection",
    text: "Start with requirements, demo scripts, vendor scoring, implementation partner review, and total cost comparison.",
    service: "/services/erp-selection/",
    resource: "/resources/erp-selection-guide/",
    contact: "/contact/erp-selection/",
    label: "Request ERP Selection Consultation",
  },
  improve: {
    title: "ERP Optimization",
    text: "Start with a health check across workflows, reporting, roles, integrations, data quality, and enhancement backlog.",
    service: "/services/erp-optimization/",
    resource: "/resources/sample-deliverables/",
    contact: "/contact/erp-assessment/",
    label: "Discuss ERP Optimization",
  },
  rescue: {
    title: "ERP Rescue",
    text: "Start with a project triage review covering governance, scope, partner performance, data, integrations, testing, and go-live risk.",
    service: "/services/erp-rescue/",
    resource: "/resources/project-scenarios/",
    contact: "/contact/erp-rescue/",
    label: "Review My Implementation",
  },
  integration: {
    title: "Integration Architecture Review",
    text: "Start with system-of-record decisions, field mappings, error handling, monitoring, reconciliation, and integration testing.",
    service: "/services/integration-automation/",
    resource: "/resources/sample-deliverables/",
    contact: "/contact/integration-review/",
    label: "Review My Integration",
  },
  golive: {
    title: "Go-Live Readiness",
    text: "Start with readiness criteria across defects, data, integrations, reports, controls, training, cutover, and hypercare.",
    service: "/services/go-live-readiness/",
    resource: "/resources/sample-deliverables/",
    contact: "/contact/go-live-readiness/",
    label: "Prepare for Go-Live",
  },
  reporting: {
    title: "Reporting and Analytics",
    text: "Start with report inventory, KPI definitions, data lineage, reconciliation rules, dashboards, and controls.",
    service: "/services/reporting-analytics/",
    resource: "/resources/sample-deliverables/",
    contact: "/contact/erp-assessment/",
    label: "Improve ERP Reporting",
  },
  netsuite: {
    title: "NetSuite Health Check",
    text: "Start with configuration, workflows, saved searches, SuiteAnalytics, roles, permissions, integrations, close, and support.",
    service: "/platforms/oracle-netsuite/",
    resource: "/resources/netsuite-optimization-guide/",
    contact: "/contact/netsuite-support/",
    label: "Request NetSuite Health Check",
  },
  support: {
    title: "Managed ERP Support",
    text: "Start with support intake, enhancement management, user support, reporting support, release readiness, and integration monitoring.",
    service: "/services/managed-erp-support/",
    resource: "/resources/engagement-packages/",
    contact: "/contact/netsuite-support/",
    label: "Discuss Managed Support",
  },
};

const assistantResult = document.querySelector("[data-assistant-result]");
document.querySelectorAll("[data-assistant-goal]").forEach((button) => {
  button.addEventListener("click", () => {
    const rec = assistantRecommendations[button.dataset.assistantGoal];
    if (!rec || !assistantResult) return;
    const payload = `${rec.title}: ${rec.text}`;
    try {
      window.localStorage.setItem("maitero-assistant-recommendation", payload);
    } catch {
      // Local storage can be disabled; the contact link still carries intent.
    }
    assistantResult.innerHTML = `
      <strong>${rec.title}</strong>
      <p>${rec.text}</p>
      <div class="assistant-result-links">
        <a href="${rec.service}">Service page</a>
        <a href="${rec.resource}">Resource</a>
      </div>
      <a class="assistant-cta" href="${rec.contact}?assistant=${encodeURIComponent(payload)}">${rec.label}</a>
    `;
  });
});

const contactForm = document.querySelector("[data-contact-form]");
if (contactForm) {
  const params = new URLSearchParams(window.location.search);
  const assistantText = params.get("assistant");
  const assistantField = contactForm.querySelector("[data-assistant-field]");
  const messageField = contactForm.querySelector("textarea[name='message']");

  let stored = "";
  try {
    stored = window.localStorage.getItem("maitero-assistant-recommendation") || "";
  } catch {
    stored = "";
  }

  const recommendation = assistantText || stored;
  if (recommendation && assistantField instanceof HTMLInputElement) {
    assistantField.value = recommendation;
  }
  if (recommendation && messageField instanceof HTMLTextAreaElement && !messageField.value) {
    messageField.value = `Assistant recommendation: ${recommendation}\n\nProject notes: `;
  }
}
