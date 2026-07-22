from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://maitero.com"
EMAIL = "rakeshbandi491@gmail.com"
CSS_VERSION = "20260722-3"
LOGO_VERSION = "20260722-2"
LASTMOD = "2026-07-22"

WRITTEN_CANONICAL: list[str] = []


def e(value: object) -> str:
    return escape(str(value), quote=True)


def clean_path(path: str) -> str:
    return path.strip("/")


def public_path(output_path: str) -> str:
    output_path = output_path.replace("\\", "/")
    if output_path == "index.html":
        return "/"
    if output_path.endswith("/index.html"):
        return "/" + output_path[: -len("/index.html")] + "/"
    return "/" + output_path


def full_url(path: str) -> str:
    if path == "/":
        return DOMAIN + "/"
    return DOMAIN + path


def write_file(output_path: str, html: str, include_in_sitemap: bool = True) -> None:
    target = ROOT / output_path
    target.parent.mkdir(parents=True, exist_ok=True)
    cleaned = "\n".join(line.rstrip() for line in html.strip().splitlines()) + "\n"
    target.write_text(cleaned, encoding="utf-8")
    if include_in_sitemap:
        WRITTEN_CANONICAL.append(public_path(output_path))


def list_html(items: Iterable[str], class_name: str = "check-list") -> str:
    return f'<ul class="{class_name}">' + "".join(f"<li>{e(item)}</li>" for item in items) + "</ul>"


def badge_list(items: Iterable[str]) -> str:
    return '<div class="badge-list">' + "".join(f"<span>{e(item)}</span>" for item in items) + "</div>"


def page_link(path: str, label: str, class_name: str = "") -> str:
    class_attr = f' class="{class_name}"' if class_name else ""
    return f'<a{class_attr} href="{e(path)}">{e(label)}</a>'


@dataclass
class ServicePage:
    title: str
    slug: str
    short: str
    hero: str
    audience: list[str]
    problems: list[str]
    warnings: list[str]
    questions: list[str]
    scope: list[str]
    activities: list[str]
    systems: list[str]
    documents: list[str]
    stakeholders: list[str]
    timeline: str
    deliverables: list[str]
    sample: str
    outcomes: list[str]
    risks: list[str]
    not_included: list[str]
    optional: list[str]
    processes: list[str]
    platforms: list[str]
    industries: list[str]
    resource: tuple[str, str]
    cta_label: str
    cta_path: str
    category: str
    accent_class: str = "page-services"
    faqs: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class ProblemPage:
    title: str
    slug: str
    short: str
    looks_like: list[str]
    causes: list[str]
    impact: list[str]
    systems: list[str]
    services: list[str]
    deliverables: list[str]
    resources: list[tuple[str, str]]
    consultation: tuple[str, str]


@dataclass
class ProcessPage:
    title: str
    slug: str
    definition: str
    stages: list[str]
    departments: list[str]
    systems: list[str]
    problems: list[str]
    controls: list[str]
    automation: list[str]
    reporting: list[str]
    services: list[str]


@dataclass
class PlatformPage:
    title: str
    slug: str
    role: str
    situations: list[str]
    functional: list[str]
    technical: list[str]
    processes: list[str]
    integrations: list[str]
    services: list[str]
    industries: list[str]
    cta: tuple[str, str]


@dataclass
class IndustryPage:
    title: str
    slug: str
    model: str
    operations: list[str]
    finance: list[str]
    requirements: list[str]
    processes: list[str]
    integrations: list[str]
    platforms: list[str]
    services: list[str]


SERVICES: list[ServicePage] = [
    ServicePage(
        title="ERP Readiness Assessment",
        slug="erp-assessment",
        short="A structured review of process, data, reporting, integrations, controls, ownership, and ERP maturity.",
        hero="Know whether to optimize, replace, stabilize, or select a new ERP before making a major spend.",
        audience=[
            "Leadership teams unsure whether the current ERP can support growth",
            "Finance teams dealing with manual close, reporting, or control issues",
            "Companies preparing for ERP selection, expansion, acquisition, or implementation",
        ],
        problems=[
            "Unclear ERP maturity",
            "Slow month-end close",
            "Manual workarounds",
            "Unreliable reporting",
            "Disconnected systems",
            "Weak ownership and governance",
        ],
        warnings=[
            "Reports require exports and offline reconciliations",
            "Teams disagree on whether the ERP should be replaced",
            "Integrations fail without clear ownership",
            "Executives cannot see a prioritized systems roadmap",
        ],
        questions=[
            "Should we optimize the current ERP or replace it?",
            "Which processes create the largest business risk?",
            "What should be fixed before selection or implementation?",
            "Which data, integration, reporting, and control gaps matter most?",
        ],
        scope=[
            "ERP maturity scoring across strategy, finance, operations, data, integrations, reporting, controls, people, and governance",
            "Current-state process review and risk assessment",
            "Reporting, dashboard, and month-end close review",
            "Future-state roadmap and next-step recommendation",
        ],
        activities=[
            "Stakeholder interviews",
            "System and process walkthroughs",
            "Document and report review",
            "Risk scoring and prioritization",
            "Executive findings readout",
        ],
        systems=[
            "ERP, CRM, billing, procurement, payroll, bank, reporting, and spreadsheet-based processes",
            "Source data, master data, integrations, and manual reconciliation files",
        ],
        documents=[
            "Chart of accounts and entity structure",
            "Close checklist, key reports, integration list, approval workflows, and pain-point inventory",
        ],
        stakeholders=["CFO", "Controller", "Operations", "IT", "Sales Operations", "ERP administrator", "Executive sponsor"],
        timeline="2 to 4 weeks depending on systems, stakeholders, and documentation readiness.",
        deliverables=[
            "ERP maturity scorecard",
            "Current-state findings report",
            "Risk and impact register",
            "Future-state roadmap",
            "Executive recommendation",
        ],
        sample="A readiness scorecard that ranks finance, operations, data, integrations, reporting, controls, technology, people, governance, scalability, and compliance.",
        outcomes=[
            "Clear decision on optimize versus replace",
            "Prioritized roadmap for process, data, reporting, and integration fixes",
            "Common executive understanding of ERP risk and readiness",
        ],
        risks=[
            "Selecting software before requirements are clear",
            "Starting implementation with weak data ownership",
            "Underestimating reporting and integration complexity",
        ],
        not_included=["Software configuration", "Custom development", "Vendor contract negotiation unless added to scope"],
        optional=["ERP selection sprint", "Data migration readiness review", "NetSuite health check"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Revenue Recognition"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Manufacturing", "Wholesale Distribution"],
        resource=("/resources/erp-readiness-checklist/", "ERP readiness checklist"),
        cta_label="Book an ERP Assessment",
        cta_path="/contact/erp-assessment/",
        category="Assess and Plan",
        accent_class="page-assessment",
        faqs=[
            ("Is this only for companies replacing ERP?", "No. The assessment also helps decide whether the current ERP should be optimized, stabilized, or better governed."),
            ("What makes the assessment finance-first?", "The review begins with financial close, reporting, controls, billing, revenue, data ownership, and audit reliability before moving into broader operations."),
        ],
    ),
    ServicePage(
        title="ERP Selection",
        slug="erp-selection",
        short="Requirements, vendor comparison, demo management, partner evaluation, cost review, and executive decision support.",
        hero="Compare ERP platforms with requirements, scoring, cost visibility, and implementation risk in one selection process.",
        audience=[
            "Companies outgrowing QuickBooks, spreadsheets, or legacy ERP",
            "Executive teams comparing NetSuite, Dynamics, Sage Intacct, Acumatica, Odoo, or other platforms",
            "Finance teams that need a defensible ERP recommendation",
        ],
        problems=["Vendor demos feel similar", "Requirements are incomplete", "Partner proposals are hard to compare", "Total cost is unclear", "Stakeholders disagree on priorities"],
        warnings=["The shortlist is based on sales demos instead of requirements", "Implementation scope differs across vendors", "Finance, operations, and IT score fit differently", "Contract and license assumptions are not visible"],
        questions=["Which ERP fits our operating model?", "What must be in the demo script?", "Which partner can actually deliver?", "What is the total cost and implementation risk?"],
        scope=["Business case support", "Requirements gathering", "RFI or RFP support", "Demo script and scorecard design", "Vendor and implementation partner scoring", "Cost and risk comparison"],
        activities=["Stakeholder workshops", "Functional and technical requirements definition", "Vendor longlist and shortlist", "Demo management", "Reference check support", "Executive recommendation"],
        systems=["Current ERP or accounting system", "CRM", "Billing", "Inventory", "Procurement", "Reporting", "Data warehouse"],
        documents=["Process inventory", "Pain-point list", "Current system costs", "Reporting examples", "Integration inventory", "Vendor proposals"],
        stakeholders=["Executive sponsor", "Finance", "Operations", "IT", "Sales Operations", "Procurement"],
        timeline="4 to 8 weeks for most mid-market selection sprints.",
        deliverables=["Requirements workbook", "Vendor demo scripts", "Vendor comparison scorecard", "Cost comparison", "Implementation partner evaluation", "Final selection recommendation"],
        sample="A scored vendor matrix comparing functional fit, scalability, customization, reporting, integration, implementation complexity, support, licensing, total cost, and industry fit.",
        outcomes=["Clear shortlist", "Aligned stakeholder scoring", "Transparent risk and cost picture", "Stronger implementation partner selection"],
        risks=["Choosing the system with the best demo", "Under-scoping data migration and integrations", "Missing requirements from finance or operations"],
        not_included=["Legal contract advice", "Software resale", "Guarantee of vendor pricing"],
        optional=["ERP business case", "Implementation partner selection", "Contract and proposal review"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Inventory and Fulfillment"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Manufacturing", "Wholesale Distribution"],
        resource=("/resources/erp-selection-guide/", "ERP selection guide"),
        cta_label="Request an ERP Selection Consultation",
        cta_path="/contact/erp-selection/",
        category="Select",
        accent_class="page-selection",
    ),
    ServicePage(
        title="ERP Implementation Advisory",
        slug="implementation-advisory",
        short="Independent implementation support across governance, design, data, integrations, testing, training, cutover, and hypercare.",
        hero="Protect ERP implementation quality with independent oversight from design through go-live.",
        audience=["Companies implementing a new ERP", "Executives who need visibility into project health", "Finance teams responsible for requirements, data, testing, and close readiness"],
        problems=["Scope drift", "Weak requirements traceability", "Unclear design decisions", "Partner dependency", "Data and testing delays", "Go-live risk"],
        warnings=["Status reports are optimistic but unresolved issues keep growing", "Design decisions are not documented", "Testing is rushed", "Business owners are not signing off on requirements"],
        questions=["Is the project on track?", "Are requirements traceable to configuration and testing?", "What risks threaten go-live?", "What should executives decide now?"],
        scope=["Project governance", "Implementation partner oversight", "Requirements traceability", "Solution design review", "Risk and issue management", "Status reporting", "Go-live readiness"],
        activities=["Steering committee preparation", "Risk register maintenance", "Design and configuration review", "Data migration coordination", "UAT planning", "Cutover readiness review"],
        systems=["ERP", "CRM", "billing", "procurement", "integration middleware", "reporting tools", "legacy systems"],
        documents=["Project plan", "requirements matrix", "design documents", "risk register", "test scripts", "cutover plan"],
        stakeholders=["Executive sponsor", "project manager", "implementation partner", "finance", "operations", "IT", "business process owners"],
        timeline="Flexible advisory support during implementation, typically weekly from design through hypercare.",
        deliverables=["Implementation risk register", "Requirements traceability view", "Design review notes", "UAT dashboard", "Cutover readiness report", "Executive status summary"],
        sample="A steering committee report showing milestones, critical risks, decisions required, ownership, and go-live readiness indicators.",
        outcomes=["Clear governance", "Improved partner accountability", "Earlier risk detection", "Better readiness for testing and launch"],
        risks=["Going live without complete testing", "Losing requirements during design", "Accepting unresolved data and integration issues"],
        not_included=["Acting as the software implementation partner unless separately scoped", "Legal or audit attestation"],
        optional=["ERP project management", "Solution design review", "Go-live readiness review"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Revenue Recognition"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Manufacturing", "Wholesale Distribution", "Professional Services"],
        resource=("/resources/project-scenarios/", "Representative project scenarios"),
        cta_label="Review My ERP Implementation",
        cta_path="/contact/erp-rescue/",
        category="Implement",
        accent_class="page-implementation",
    ),
    ServicePage(
        title="ERP Project Management",
        slug="erp-project-management",
        short="Project structure, workplan ownership, decision tracking, risk management, status reporting, and cross-functional coordination.",
        hero="Keep ERP work moving with practical project management that connects executives, business owners, IT, and implementation partners.",
        audience=["Teams without a dedicated ERP project lead", "Finance-led ERP projects", "Projects with multiple vendors or workstreams"],
        problems=["No single view of workstream status", "Decisions stall", "Risks are discussed but not owned", "Testing and migration timelines are unclear"],
        warnings=["Meetings create notes but not decisions", "Critical tasks have no accountable owner", "Executive sponsors hear about issues too late"],
        questions=["Who owns each decision?", "Which tasks are late?", "What must happen before the next milestone?", "Which risks need executive action?"],
        scope=["Project plan management", "Workstream coordination", "Risk and issue tracking", "Decision log", "Status reporting", "Meeting cadence"],
        activities=["Weekly status cadence", "Task and dependency review", "Partner follow-up", "Decision documentation", "Executive reporting"],
        systems=["ERP implementation tools", "project management tools", "requirements trackers", "test management workbooks"],
        documents=["Project charter", "project plan", "decision log", "risk register", "status reports"],
        stakeholders=["Project sponsor", "finance lead", "IT lead", "implementation partner", "workstream owners"],
        timeline="Weekly or fractional support through a defined ERP phase or the full project.",
        deliverables=["Project governance model", "Integrated workplan", "Risk and issue register", "Decision log", "Status report package"],
        sample="A concise project dashboard showing milestones, blocked decisions, risks, owners, and next two-week priorities.",
        outcomes=["Cleaner accountability", "Fewer late surprises", "Better executive visibility", "More disciplined decision-making"],
        risks=["Uncontrolled scope", "Partner misalignment", "Delayed decisions", "Missed testing or cutover milestones"],
        not_included=["Replacing the implementation partner", "Full-time internal PMO staffing unless separately agreed"],
        optional=["Go-live readiness review", "ERP rescue review", "Testing and UAT support"],
        processes=["Implementation governance", "Testing and UAT", "Cutover Planning"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Manufacturing"],
        resource=("/resources/methodology/", "Maitero methodology"),
        cta_label="Discuss ERP Project Management",
        cta_path="/contact/erp-rescue/",
        category="Implement",
        accent_class="page-implementation",
    ),
    ServicePage(
        title="Business Process Review",
        slug="business-process-review",
        short="A practical review of finance and operations workflows before ERP selection, implementation, or optimization.",
        hero="Find the process gaps behind ERP symptoms before you configure or replace software.",
        audience=["Teams preparing requirements", "Companies with manual workarounds", "Finance and operations leaders redesigning workflows"],
        problems=["Unclear handoffs", "Spreadsheet-based approvals", "Duplicate entry", "Reporting breaks between departments", "Controls depend on manual review"],
        warnings=["Users disagree about the real process", "Exceptions are handled outside the ERP", "Approvals are slow or undocumented"],
        questions=["Which steps can be automated?", "Where do controls fail?", "What should be standard before ERP design?", "What should be in scope for implementation?"],
        scope=["Current-state process mapping", "Gap and pain-point review", "Control and reporting analysis", "Future-state recommendations"],
        activities=["Process workshops", "Exception review", "Control walkthroughs", "Reporting dependency mapping", "Future-state design discussion"],
        systems=["ERP", "CRM", "billing", "procurement", "spreadsheets", "approval tools", "reporting tools"],
        documents=["Process maps", "policy documents", "approval workflows", "sample reports", "manual trackers"],
        stakeholders=["Finance", "operations", "sales operations", "procurement", "IT", "process owners"],
        timeline="2 to 6 weeks depending on process scope.",
        deliverables=["Current-state process map", "Pain-point register", "Control gap summary", "Future-state process recommendations"],
        sample="A future-state process map showing activities, system ownership, approval points, controls, reporting outputs, and integration handoffs.",
        outcomes=["Better requirements", "Cleaner workflows", "Reduced manual work", "Clearer ERP design priorities"],
        risks=["Configuring bad processes into the new ERP", "Missing control requirements", "Underestimating change management"],
        not_included=["Full operating model redesign", "Custom software build"],
        optional=["Requirements definition", "ERP assessment", "Workflow automation roadmap"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Revenue Recognition"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Salesforce"],
        industries=["Software and SaaS", "Professional Services", "Manufacturing", "Wholesale Distribution"],
        resource=("/resources/sample-deliverables/", "Sample process deliverables"),
        cta_label="Request a Process Review",
        cta_path="/contact/erp-assessment/",
        category="Assess and Plan",
        accent_class="page-assessment",
    ),
    ServicePage(
        title="Requirements Definition",
        slug="requirements-definition",
        short="Functional, technical, reporting, data, integration, control, and security requirements for selection or implementation.",
        hero="Turn business needs into requirements vendors, partners, and internal teams can actually use.",
        audience=["Teams selecting ERP", "Implementation teams with unclear scope", "Finance teams that need traceable requirements"],
        problems=["Requirements are too vague", "Demos are not comparable", "Implementation scope is ambiguous", "Testing cannot trace back to business needs"],
        warnings=["Important requirements live in meeting notes", "Departments use different priority definitions", "Integrations and reporting are listed too late"],
        questions=["What must the ERP support?", "Which requirements are critical?", "How should vendors be scored?", "What should be traced through testing?"],
        scope=["Functional requirements", "Technical requirements", "Reporting requirements", "Integration requirements", "Data and security requirements", "Prioritization"],
        activities=["Requirements workshops", "Process-to-requirement mapping", "Priority scoring", "Traceability setup", "Validation with stakeholders"],
        systems=["ERP", "CRM", "billing", "procurement", "inventory", "data warehouse", "reporting"],
        documents=["Process inventory", "current reports", "integration list", "pain points", "compliance needs"],
        stakeholders=["Finance", "operations", "IT", "sales operations", "executive sponsor"],
        timeline="2 to 5 weeks for focused requirements work.",
        deliverables=["Requirements matrix", "Prioritization model", "Demo requirements", "Traceability structure"],
        sample="A requirements matrix with owner, priority, process, system, demo evidence, configuration status, and testing reference.",
        outcomes=["Better vendor comparison", "Clear implementation scope", "Stronger testing coverage", "Less rework"],
        risks=["Incomplete requirements", "Unclear acceptance criteria", "Scope changes hidden as design issues"],
        not_included=["Vendor legal review", "Full implementation configuration"],
        optional=["ERP selection sprint", "Solution design review", "Testing and UAT planning"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Subscription Billing"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Retail and Ecommerce"],
        resource=("/resources/erp-selection-guide/", "ERP selection guide"),
        cta_label="Define ERP Requirements",
        cta_path="/contact/erp-selection/",
        category="Assess and Plan",
        accent_class="page-assessment",
    ),
    ServicePage(
        title="Solution Design Review",
        slug="solution-design-review",
        short="Independent review of proposed ERP configuration, workflows, integrations, roles, reports, and controls before build or go-live.",
        hero="Catch design issues before they become expensive ERP rework.",
        audience=["Teams in design or build", "Executives concerned about implementation quality", "Finance teams reviewing partner design decisions"],
        problems=["Design decisions are hard to evaluate", "Controls and reporting are under-designed", "Customization requests are growing", "Business owners are unsure what they approved"],
        warnings=["Design documents are too technical for process owners", "Reports are not mapped to requirements", "Roles and approvals are still vague"],
        questions=["Does the design meet requirements?", "Where is customization unnecessary?", "Will controls, reporting, and integrations work?", "What should be changed before build?"],
        scope=["Design document review", "Configuration and customization governance", "Workflow and approval review", "Reporting and integration fit review", "Risk findings"],
        activities=["Design walkthroughs", "Requirement trace checks", "Role and approval review", "Report and integration mapping", "Findings workshop"],
        systems=["ERP", "middleware", "CRM", "billing", "procurement", "reporting", "identity and security tools"],
        documents=["Design documents", "requirements matrix", "workflow diagrams", "role matrix", "report inventory"],
        stakeholders=["Finance process owners", "IT", "implementation partner", "ERP administrator", "executive sponsor"],
        timeline="1 to 3 weeks for a focused design review.",
        deliverables=["Design review memo", "Configuration risk list", "Customization governance recommendations", "Open decision log"],
        sample="A design risk register showing requirement gaps, control gaps, customization risk, integration dependency, and decision owner.",
        outcomes=["Less rework", "Clearer decisions", "Improved controls", "Better testing readiness"],
        risks=["Building around misunderstood requirements", "Over-customizing", "Missing reporting or role constraints"],
        not_included=["Legal advice", "Performance warranty", "Hands-on build unless scoped"],
        optional=["Testing and UAT support", "Integration architecture review", "Go-live readiness review"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Revenue Recognition"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica"],
        industries=["Software and SaaS", "Manufacturing", "Wholesale Distribution"],
        resource=("/resources/sample-deliverables/", "Sample deliverables"),
        cta_label="Review My Solution Design",
        cta_path="/contact/erp-rescue/",
        category="Implement",
        accent_class="page-implementation",
    ),
    ServicePage(
        title="Data Migration",
        slug="data-migration",
        short="Data inventory, ownership, cleansing, mapping, trial migration, reconciliation, cutover, validation, and sign-off planning.",
        hero="Move ERP data with ownership, mapping, validation, and reconciliation before it reaches go-live risk.",
        audience=["Teams migrating customers, vendors, items, chart of accounts, balances, contracts, transactions, or historical data", "Implementation teams behind on data readiness"],
        problems=["Data ownership is unclear", "Mappings are incomplete", "Trial loads keep failing", "Open transactions do not reconcile", "Historical data decisions are delayed"],
        warnings=["Teams discover duplicates during testing", "Data cleanup is still happening near cutover", "No sign-off process exists", "Reporting cannot reconcile to source systems"],
        questions=["Which data should migrate?", "Who owns cleansing?", "What must reconcile?", "How many trial migrations are needed?", "What is the cutover plan?"],
        scope=["Data migration strategy", "Source inventory", "Data quality review", "Mapping and transformation rules", "Trial migration planning", "Reconciliation and sign-off"],
        activities=["Data workshops", "Field mapping review", "Cleansing rules", "Trial load tracking", "Reconciliation planning", "Cutover migration coordination"],
        systems=["Legacy ERP", "QuickBooks", "CRM", "billing", "inventory", "spreadsheets", "data warehouse"],
        documents=["Data inventory", "mapping workbook", "sample extracts", "trial load results", "reconciliation reports"],
        stakeholders=["Finance", "operations", "IT", "data owners", "implementation partner", "ERP administrator"],
        timeline="3 to 8 weeks depending on source systems, history, and data quality.",
        deliverables=["Migration strategy", "Data inventory", "Mapping workbook", "Cleansing checklist", "Trial migration tracker", "Reconciliation sign-off plan"],
        sample="A migration tracker showing source, owner, mapping status, cleansing status, trial load result, reconciliation result, and sign-off owner.",
        outcomes=["Reduced go-live data risk", "Clear data ownership", "Better reconciliation", "Faster user trust after launch"],
        risks=["Migrating dirty data", "Losing audit trail", "Incomplete open transactions", "Unreconciled balances"],
        not_included=["Bulk data entry", "Data hosting", "Data deletion decisions without client sign-off"],
        optional=["Data remediation", "Integration testing", "Go-live readiness review"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Inventory and Fulfillment"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Manufacturing", "Wholesale Distribution", "Retail and Ecommerce"],
        resource=("/resources/erp-readiness-checklist/", "ERP readiness checklist"),
        cta_label="Review My Data Migration Plan",
        cta_path="/contact/data-migration/",
        category="Implement",
        accent_class="page-migration",
    ),
    ServicePage(
        title="Integration and Automation",
        slug="integration-automation",
        short="Integration architecture, data ownership, middleware fit, mappings, error handling, monitoring, testing, and workflow automation.",
        hero="Connect ERP, CRM, billing, procurement, ecommerce, banking, and reporting systems with clear ownership and controls.",
        audience=["Teams with broken integrations", "Companies connecting ERP to Salesforce, Stripe, Shopify, Workato, Celigo, or data platforms", "Finance leaders tired of manual re-entry"],
        problems=["Systems do not sync", "Errors are not monitored", "Duplicate data appears", "Finance reconciles integration gaps manually", "System of record decisions are unclear"],
        warnings=["Integration failures are found by users", "No one owns field mappings", "Manual imports replace automated flow", "Data differs across CRM, billing, and ERP"],
        questions=["What should be real-time versus scheduled?", "Which system owns each field?", "How should errors be handled?", "What should be automated first?"],
        scope=["Current-state architecture", "Future-state integration model", "System of record decisions", "Mapping review", "Error handling and monitoring", "Integration testing"],
        activities=["Integration inventory", "Data flow design", "Middleware review", "Security and authentication review", "Test planning", "Automation opportunity mapping"],
        systems=["ERP", "Salesforce", "HubSpot", "Stripe", "Chargebee", "Zuora", "Shopify", "Coupa", "Zip", "Workato", "Celigo", "Boomi", "Snowflake", "Power BI"],
        documents=["Integration inventory", "API specs", "field mappings", "error logs", "business rules", "test cases"],
        stakeholders=["Finance", "IT", "sales operations", "RevOps", "procurement", "data team", "implementation partner"],
        timeline="2 to 6 weeks for architecture review, longer for build oversight.",
        deliverables=["Integration architecture", "System-of-record matrix", "Field mapping review", "Error handling checklist", "Integration testing plan"],
        sample="An integration architecture showing source systems, direction, frequency, ownership, error handling, reconciliation points, and reporting dependencies.",
        outcomes=["Cleaner system ownership", "Reduced manual re-entry", "Faster issue detection", "More reliable reporting"],
        risks=["Duplicate records", "Silent integration failures", "Security gaps", "Manual reconciliation hidden as normal operations"],
        not_included=["Custom connector development unless separately scoped", "Middleware licensing"],
        optional=["Workato or Celigo review", "NetSuite integration review", "Reporting automation roadmap"],
        processes=["Lead to Cash", "Order to Cash", "Quote to Cash", "Procure to Pay"],
        platforms=["Oracle NetSuite", "Salesforce", "Workato", "Stripe", "Snowflake", "Power BI"],
        industries=["Software and SaaS", "Retail and Ecommerce", "Wholesale Distribution"],
        resource=("/resources/sample-deliverables/", "Sample integration deliverables"),
        cta_label="Review My Integration Architecture",
        cta_path="/contact/integration-review/",
        category="Implement",
        accent_class="page-integrations",
    ),
    ServicePage(
        title="Testing and UAT",
        slug="testing-uat",
        short="Test strategy, scripts, requirements traceability, defect triage, business sign-off, and go-live readiness support.",
        hero="Turn ERP testing from a late-stage scramble into evidence that the system is ready.",
        audience=["Implementation teams preparing for UAT", "Finance teams responsible for sign-off", "Projects with unclear testing coverage"],
        problems=["Test scripts do not reflect real processes", "Defects are not prioritized", "Requirements are not traced", "Business sign-off is unclear"],
        warnings=["Users test only happy paths", "Critical integrations have no end-to-end tests", "Reports are not reconciled during UAT"],
        questions=["What should be tested?", "Who signs off?", "Which defects block go-live?", "Are reports and integrations ready?"],
        scope=["Test strategy", "UAT planning", "Requirements traceability", "Defect triage", "Sign-off design", "Go-live readiness inputs"],
        activities=["Script review", "End-to-end test scenario design", "Defect review cadence", "Readiness reporting", "Sign-off facilitation"],
        systems=["ERP", "CRM", "billing", "procurement", "integration middleware", "reporting tools"],
        documents=["Requirements matrix", "test scripts", "defect logs", "integration test results", "report reconciliation evidence"],
        stakeholders=["Finance", "operations", "IT", "users", "implementation partner", "executive sponsor"],
        timeline="2 to 5 weeks depending on UAT scope.",
        deliverables=["UAT strategy", "Test scenario map", "Defect triage model", "UAT dashboard", "Sign-off checklist"],
        sample="A UAT dashboard showing test coverage, pass rate, blocker defects, owner, retest status, and unresolved go-live risk.",
        outcomes=["Better test coverage", "Clearer go-live decisions", "Reduced defects after launch", "Better user confidence"],
        risks=["Testing too late", "Missing integration failures", "Approving go-live without evidence"],
        not_included=["Automated test tooling unless scoped", "Replacing user participation"],
        optional=["Go-live readiness review", "ERP project rescue", "Training support"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Subscription Billing"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Manufacturing", "Wholesale Distribution"],
        resource=("/resources/sample-deliverables/", "Sample UAT dashboard"),
        cta_label="Plan ERP Testing",
        cta_path="/contact/go-live-readiness/",
        category="Implement",
        accent_class="page-implementation",
    ),
    ServicePage(
        title="Go-Live Readiness",
        slug="go-live-readiness",
        short="Readiness review across open defects, data, integrations, reports, controls, training, cutover, support, and executive decision criteria.",
        hero="Know what must be true before the ERP launch decision.",
        audience=["Teams approaching go-live", "Executives deciding whether to launch", "Projects with unresolved data, testing, or integration issues"],
        problems=["Go-live confidence is based on optimism", "Cutover tasks are incomplete", "Defect priority is unclear", "Users are not ready"],
        warnings=["Critical open issues have no owner", "Cutover weekend has no decision checkpoints", "Support and hypercare roles are unclear"],
        questions=["Should we go live?", "What blocks launch?", "Who owns cutover?", "What happens in hypercare?"],
        scope=["Readiness criteria", "Open defect review", "Data and integration readiness", "Report and control readiness", "Training and support review", "Cutover plan review"],
        activities=["Readiness workshops", "Cutover plan review", "Issue triage", "Executive readout", "Hypercare planning"],
        systems=["ERP", "connected systems", "reporting", "support channels", "project management tools"],
        documents=["Cutover plan", "defect log", "migration sign-off", "UAT results", "training plan", "support model"],
        stakeholders=["Executive sponsor", "project manager", "finance", "operations", "IT", "implementation partner", "support owners"],
        timeline="1 to 3 weeks before planned go-live.",
        deliverables=["Go-live readiness report", "Cutover checklist", "Blocker decision log", "Hypercare plan", "Executive go/no-go summary"],
        sample="A go-live readiness report with weighted criteria, blockers, risks accepted, owner assignments, and launch recommendation.",
        outcomes=["Clear go/no-go decision", "Reduced launch risk", "Better hypercare readiness", "Executive visibility"],
        risks=["Launching with unresolved blockers", "Incomplete data sign-off", "Poor user support after launch"],
        not_included=["Guarantee of implementation success", "Full system build"],
        optional=["Post-go-live stabilization", "ERP rescue review", "Managed support"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Manufacturing", "Wholesale Distribution", "Retail and Ecommerce"],
        resource=("/resources/sample-deliverables/", "Sample go-live checklist"),
        cta_label="Prepare for Go-Live",
        cta_path="/contact/go-live-readiness/",
        category="Implement",
        accent_class="page-implementation",
    ),
    ServicePage(
        title="ERP Rescue",
        slug="erp-rescue",
        short="Triage delayed, over-budget, unstable, or failed ERP implementations and produce a recovery roadmap.",
        hero="When an ERP implementation is at risk, Maitero helps identify what is broken and what must happen next.",
        audience=["Projects missing milestones", "Executives concerned about implementation partner performance", "Teams facing go-live instability or budget overruns"],
        problems=["Missed deadlines", "Uncontrolled scope", "Poor requirements", "Failed migration", "Broken integrations", "Weak testing", "Low adoption"],
        warnings=["Risks repeat across status meetings", "Business owners no longer trust the project plan", "Partner deliverables are late or incomplete", "Go-live date keeps moving"],
        questions=["Can the project be recovered?", "Which risks are critical?", "What should be paused, reworked, or escalated?", "What is the revised path to launch?"],
        scope=["Project health review", "Scope and requirement review", "Partner and governance review", "Data, integration, testing, and reporting triage", "Recovery roadmap"],
        activities=["Executive interviews", "Workstream triage", "Risk ranking", "Partner deliverable review", "Recovery planning", "Decision readout"],
        systems=["ERP", "CRM", "billing", "procurement", "integrations", "reporting", "legacy systems"],
        documents=["Project plan", "requirements", "design documents", "defect log", "migration tracker", "risk register", "status reports"],
        stakeholders=["Executive sponsor", "project manager", "implementation partner", "finance", "operations", "IT"],
        timeline="1 to 3 weeks for a rescue review, followed by recovery support if needed.",
        deliverables=["Project triage report", "Risk ranking", "Recovery roadmap", "Revised milestone plan", "Executive decision summary"],
        sample="A rescue roadmap showing stop, fix, continue, and escalate actions by workstream with owner, impact, and due date.",
        outcomes=["Clear recovery path", "Improved governance", "Better partner accountability", "Reduced chance of failed go-live"],
        risks=["Continuing a flawed implementation plan", "Ignoring data and integration blockers", "Launching unstable ERP"],
        not_included=["Litigation support", "Vendor contract enforcement", "Guarantee of rescue outcome"],
        optional=["Go-live readiness review", "Post-go-live stabilization", "Managed support"],
        processes=["Implementation governance", "Data Migration", "Testing and UAT", "Record to Report"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Manufacturing", "Wholesale Distribution", "Professional Services"],
        resource=("/resources/project-scenarios/", "ERP rescue project scenario"),
        cta_label="Review My ERP Implementation",
        cta_path="/contact/erp-rescue/",
        category="Stabilize and Rescue",
        accent_class="page-implementation",
    ),
    ServicePage(
        title="Post-Go-Live Stabilization",
        slug="post-go-live-stabilization",
        short="Hypercare, defect prioritization, reporting stabilization, data remediation, integration monitoring, and user support after launch.",
        hero="Stabilize ERP after go-live before workarounds become permanent operations.",
        audience=["Teams recently live on ERP", "Finance teams dealing with launch defects", "Executives who need reliable reporting after go-live"],
        problems=["Users are confused", "Reports do not reconcile", "Integrations fail", "Defects pile up", "Month-end close is unstable"],
        warnings=["Teams rebuild reports in spreadsheets", "Support tickets repeat", "No one owns enhancement priorities"],
        questions=["What should be fixed first?", "Which issues are defects versus enhancements?", "How should support be structured?", "What does stable operations require?"],
        scope=["Hypercare structure", "Defect and enhancement triage", "Reporting and close stabilization", "Integration monitoring", "User support model"],
        activities=["Issue review", "Priority backlog", "Close support planning", "Training gap review", "Stabilization dashboard"],
        systems=["ERP", "connected systems", "reporting tools", "support tickets", "data migration artifacts"],
        documents=["Defect log", "support tickets", "close checklist", "reconciliation reports", "training materials"],
        stakeholders=["Finance", "operations", "IT", "ERP administrator", "support team", "implementation partner"],
        timeline="30, 60, or 90 day stabilization plans.",
        deliverables=["Stabilization backlog", "Issue triage model", "Reporting remediation plan", "User support playbook", "30/60/90 roadmap"],
        sample="A stabilization dashboard separating blockers, defects, enhancements, training needs, report gaps, and integration issues.",
        outcomes=["Faster path to stable operations", "Cleaner support ownership", "More reliable reporting", "Reduced workaround growth"],
        risks=["Normalizing bad workarounds", "Leaving data defects unresolved", "Losing user trust"],
        not_included=["Long-term managed support unless selected", "Full reimplementation"],
        optional=["Managed ERP support", "ERP optimization roadmap", "Reporting stabilization"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Reporting and Analytics"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Wholesale Distribution"],
        resource=("/resources/engagement-packages/", "Post-go-live support packages"),
        cta_label="Plan Post-Go-Live Stabilization",
        cta_path="/contact/go-live-readiness/",
        category="Stabilize and Rescue",
        accent_class="page-optimization",
    ),
    ServicePage(
        title="ERP Optimization",
        slug="erp-optimization",
        short="Workflow, reporting, approval, role, data, integration, close, billing, revenue, procurement, and adoption improvements.",
        hero="Improve an existing ERP system without jumping too quickly into replacement.",
        audience=["Companies already live on ERP", "NetSuite, Dynamics, Sage, Acumatica, or Odoo teams with manual work", "Finance teams needing better close and reporting"],
        problems=["Spreadsheet dependency", "Slow close", "Poor dashboards", "Manual approvals", "Integration errors", "Role confusion", "Customization debt"],
        warnings=["Enhancement backlog has no priority model", "Users avoid the ERP", "Reports are recreated outside the system", "Approvals happen through email"],
        questions=["What should we fix first?", "Which customizations create risk?", "Can workflows be automated?", "How do we improve reporting and adoption?"],
        scope=["ERP health check", "Workflow review", "Reporting review", "Customization and script review", "Integration review", "Optimization roadmap"],
        activities=["System walkthroughs", "Backlog review", "Close and reporting analysis", "Automation opportunity review", "Prioritization workshop"],
        systems=["ERP", "CRM", "billing", "procurement", "reporting", "middleware", "spreadsheets"],
        documents=["Enhancement backlog", "key reports", "saved searches", "workflow list", "role matrix", "integration inventory"],
        stakeholders=["Finance", "operations", "IT", "ERP administrator", "executive sponsor"],
        timeline="2 to 6 weeks for a roadmap; ongoing advisory available.",
        deliverables=["ERP optimization roadmap", "Enhancement backlog", "Workflow automation plan", "Reporting improvement plan", "30/60/90 day priorities"],
        sample="A prioritized optimization backlog ranked by business impact, risk reduction, effort, ownership, and dependency.",
        outcomes=["Reduced manual work", "Better reporting", "Improved adoption", "Clear enhancement priorities"],
        risks=["Optimizing symptoms instead of root causes", "Adding customization without governance", "Ignoring controls and data quality"],
        not_included=["Guaranteed performance improvements without technical remediation", "Custom build unless scoped"],
        optional=["NetSuite optimization", "Reporting and analytics", "Managed ERP support"],
        processes=["Record to Report", "Order to Cash", "Revenue Recognition", "Reporting and Analytics"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Manufacturing", "Retail and Ecommerce"],
        resource=("/resources/netsuite-optimization-guide/", "NetSuite optimization guide"),
        cta_label="Discuss ERP Optimization",
        cta_path="/contact/erp-assessment/",
        category="Optimize",
        accent_class="page-optimization",
    ),
    ServicePage(
        title="Managed ERP Support",
        slug="managed-erp-support",
        short="Ongoing administration, enhancement management, reporting support, user support, integration monitoring, and release readiness.",
        hero="Create a practical support model after ERP launch so improvements do not stall.",
        audience=["Companies without a dedicated ERP owner", "NetSuite or ERP teams with recurring support requests", "Finance teams needing steady enhancement delivery"],
        problems=["Support requests are ad hoc", "Enhancement backlog grows", "Reports break after changes", "Releases are unmanaged", "Users lack training"],
        warnings=["No one owns ERP governance", "The same issues recur monthly", "Enhancements are prioritized by whoever asks loudest"],
        questions=["What support model do we need?", "How should enhancements be prioritized?", "Who monitors integrations?", "How should users request help?"],
        scope=["Support intake", "Enhancement management", "ERP administration support", "Reporting support", "Integration monitoring", "Release readiness"],
        activities=["Backlog triage", "Monthly support cadence", "Issue review", "Report updates", "User support and training planning"],
        systems=["ERP", "CRM", "billing", "procurement", "integration middleware", "reporting tools"],
        documents=["Support backlog", "role matrix", "integration inventory", "report catalog", "release notes"],
        stakeholders=["ERP administrator", "finance", "operations", "IT", "business owners"],
        timeline="Monthly support retainers or defined support blocks.",
        deliverables=["Support intake model", "Prioritized enhancement backlog", "Monthly support summary", "Release readiness checklist", "Training notes"],
        sample="A monthly support report showing completed tickets, open priorities, integration issues, reporting changes, risks, and next-month plan.",
        outcomes=["Clear ownership", "Faster support response", "Better enhancement discipline", "Lower dependency on urgent fixes"],
        risks=["Support debt", "Unmanaged releases", "Poor adoption", "Unmonitored integrations"],
        not_included=["24/7 emergency support unless contracted", "Software license fees"],
        optional=["NetSuite administration", "Reporting support", "Integration monitoring"],
        processes=["Record to Report", "Order to Cash", "Reporting and Analytics"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica", "Odoo"],
        industries=["Software and SaaS", "Professional Services", "Retail and Ecommerce"],
        resource=("/resources/engagement-packages/", "Managed support package"),
        cta_label="Discuss Managed ERP Support",
        cta_path="/contact/netsuite-support/",
        category="Support",
        accent_class="page-optimization",
    ),
    ServicePage(
        title="Reporting and Analytics",
        slug="reporting-analytics",
        short="Report inventory, KPI definition, dashboard design, reconciliation logic, data ownership, and analytics roadmap.",
        hero="Make ERP reporting reliable enough for month-end, board reporting, and operational decisions.",
        audience=["Finance teams rebuilding reports in spreadsheets", "Executives lacking trusted dashboards", "Companies connecting ERP to BI tools"],
        problems=["Reports disagree", "KPIs are undefined", "Data ownership is unclear", "Dashboards are not reconciled", "Manual report packages take too long"],
        warnings=["Different teams present different numbers", "Board reporting depends on manual manipulation", "Source-of-truth rules are missing"],
        questions=["Which reports matter most?", "Where should each metric come from?", "How should dashboards reconcile?", "What should be automated?"],
        scope=["Report inventory", "Metric definition", "Data source review", "Dashboard requirements", "Reconciliation and controls", "Analytics roadmap"],
        activities=["Report workshops", "KPI mapping", "Data lineage review", "Dashboard wireframes", "Reconciliation rules"],
        systems=["ERP", "CRM", "billing", "data warehouse", "Power BI", "Tableau", "Looker", "Excel", "Google Sheets"],
        documents=["Current reports", "metric definitions", "data exports", "dashboard examples", "reconciliation files"],
        stakeholders=["Finance", "executives", "operations", "sales operations", "data team", "IT"],
        timeline="2 to 6 weeks depending on report scope.",
        deliverables=["Report inventory", "KPI definition workbook", "Dashboard requirements", "Reconciliation model", "Reporting roadmap"],
        sample="A reporting requirements pack that connects each KPI to owner, source system, calculation rule, refresh timing, control, and dashboard audience.",
        outcomes=["Trusted metrics", "Faster reporting cycles", "Cleaner dashboard requirements", "Reduced spreadsheet dependency"],
        risks=["Automating bad definitions", "Dashboarding unreconciled data", "Ignoring close controls"],
        not_included=["BI platform licensing", "Full data warehouse build unless scoped"],
        optional=["NetSuite reporting", "Power BI roadmap", "Data warehouse integration review"],
        processes=["Record to Report", "Order to Cash", "Revenue Recognition"],
        platforms=["Oracle NetSuite", "Power BI", "Tableau", "Looker", "Snowflake"],
        industries=["Software and SaaS", "Professional Services", "Manufacturing"],
        resource=("/resources/sample-deliverables/", "Sample reporting deliverables"),
        cta_label="Improve ERP Reporting",
        cta_path="/contact/erp-assessment/",
        category="Optimize",
        accent_class="page-optimization",
    ),
    ServicePage(
        title="Internal Controls and Compliance",
        slug="internal-controls-compliance",
        short="Role design, approvals, segregation of duties, audit support, change controls, reporting controls, and process evidence.",
        hero="Improve ERP controls without slowing the business down.",
        audience=["Finance teams preparing for audit readiness", "Companies adding entities or controls", "Teams concerned about roles, approvals, and system access"],
        problems=["Weak approval workflows", "Roles are too broad", "Segregation of duties is unclear", "Manual evidence is hard to collect", "Changes are not governed"],
        warnings=["Users have access they do not need", "Approvals happen outside the ERP", "Audit evidence takes too long to compile"],
        questions=["Which controls should live in the ERP?", "Where are role conflicts?", "How should approvals and evidence work?", "What should be documented?"],
        scope=["Control walkthrough", "Role and permission review", "Approval workflow review", "Reporting control review", "Change governance"],
        activities=["Role matrix review", "Approval design review", "Evidence mapping", "Control gap workshop", "Remediation plan"],
        systems=["ERP", "identity systems", "approval tools", "reporting tools", "integration middleware"],
        documents=["Role list", "permission matrix", "approval workflows", "audit requests", "change logs"],
        stakeholders=["Controller", "finance", "IT", "internal audit", "ERP administrator", "process owners"],
        timeline="2 to 5 weeks depending on control scope.",
        deliverables=["Control gap summary", "Role remediation plan", "Approval workflow recommendations", "Audit evidence map", "Governance checklist"],
        sample="A role and control matrix showing sensitive access, conflicting duties, approval gaps, report owners, and remediation priority.",
        outcomes=["Stronger controls", "Cleaner audit evidence", "Reduced access risk", "Better governance"],
        risks=["Over-permissioned users", "Unsupported manual controls", "Uncontrolled system changes"],
        not_included=["Audit opinion", "Legal compliance certification"],
        optional=["ERP assessment", "NetSuite roles and permissions review", "Release management support"],
        processes=["Record to Report", "Procure to Pay", "Order to Cash"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Acumatica"],
        industries=["Software and SaaS", "Financial Services", "Healthcare Services", "Nonprofit Organizations"],
        resource=("/resources/sample-deliverables/", "Sample control deliverables"),
        cta_label="Review ERP Controls",
        cta_path="/contact/erp-assessment/",
        category="Optimize",
        accent_class="page-optimization",
    ),
    ServicePage(
        title="Finance Transformation",
        slug="finance-transformation",
        short="Finance operating model, close process, reporting, controls, automation, systems roadmap, and scalable finance operations.",
        hero="Build finance systems and processes that can support growth, reporting, and operational control.",
        audience=["CFOs and controllers planning finance modernization", "Companies expanding entities, products, or revenue models", "Teams preparing for ERP transformation"],
        problems=["Finance is reactive", "Close is slow", "Reporting is manual", "Processes do not scale", "Controls lag business growth"],
        warnings=["Finance depends on a few people and many spreadsheets", "New products or entities create reporting stress", "ERP and connected systems lack ownership"],
        questions=["What should finance look like at the next stage?", "Which systems and processes must change?", "What is the roadmap?", "How should controls and reporting scale?"],
        scope=["Finance maturity review", "Close and reporting model", "Process redesign", "Systems roadmap", "Automation and control opportunities"],
        activities=["Finance workshops", "Process and report review", "Operating model discussion", "Roadmap planning", "Executive readout"],
        systems=["ERP", "billing", "CRM", "procurement", "expense", "planning", "reporting", "data warehouse"],
        documents=["Close process", "board reporting", "finance org chart", "systems inventory", "pain-point list"],
        stakeholders=["CFO", "controller", "FP&A", "RevOps", "operations", "IT", "executive sponsor"],
        timeline="4 to 8 weeks for a transformation roadmap.",
        deliverables=["Finance transformation roadmap", "Close improvement plan", "Systems roadmap", "Automation backlog", "Operating model recommendations"],
        sample="A finance roadmap linking process priorities, systems changes, reporting improvements, control requirements, and ownership over 30, 60, 90, and 180 days.",
        outcomes=["Scalable finance operations", "Clear systems priorities", "Reduced manual effort", "Better executive reporting"],
        risks=["Buying software before fixing finance process", "Scaling weak controls", "Overbuilding systems too early"],
        not_included=["Accounting policy advice", "Hiring or staffing decisions unless advisory scope includes it"],
        optional=["ERP assessment", "ERP selection", "Reporting and analytics"],
        processes=["Record to Report", "Order to Cash", "Revenue Recognition", "Financial Planning and Analysis"],
        platforms=["Oracle NetSuite", "Microsoft Dynamics 365", "Sage Intacct", "Power BI", "Pigment"],
        industries=["Software and SaaS", "Professional Services", "Multi-Entity Businesses"],
        resource=("/resources/methodology/", "Finance-first methodology"),
        cta_label="Discuss Finance Transformation",
        cta_path="/contact/erp-assessment/",
        category="Assess and Plan",
        accent_class="page-assessment",
    ),
]


SERVICE_GROUPS = [
    ("Assess and Plan", ["ERP Readiness Assessment", "Business Process Review", "Requirements Definition", "Finance Transformation"]),
    ("Select", ["ERP Selection"]),
    ("Implement", ["ERP Implementation Advisory", "ERP Project Management", "Solution Design Review", "Data Migration", "Integration and Automation", "Testing and UAT", "Go-Live Readiness"]),
    ("Stabilize and Rescue", ["ERP Rescue", "Post-Go-Live Stabilization"]),
    ("Optimize", ["ERP Optimization", "Reporting and Analytics", "Internal Controls and Compliance"]),
    ("Support", ["Managed ERP Support"]),
]


PROBLEMS = [
    ProblemPage(
        title="Selecting a New ERP",
        slug="selecting-an-erp",
        short="Use requirements, scorecards, demo evidence, and implementation risk to choose a platform with confidence.",
        looks_like=["Leadership knows the current system is no longer enough", "Vendors all appear capable in demos", "Finance and operations have different priorities"],
        causes=["Requirements have not been defined deeply enough", "Implementation complexity is not visible", "Decision criteria are not weighted"],
        impact=["Costly platform mismatch", "Weak implementation scope", "Stakeholder disagreement after contract signature"],
        systems=["QuickBooks", "legacy ERP", "CRM", "billing", "inventory", "reporting"],
        services=["ERP Readiness Assessment", "ERP Selection", "Requirements Definition"],
        deliverables=["Requirements workbook", "Vendor scorecard", "Demo scripts", "Cost comparison", "Final recommendation"],
        resources=[("/resources/erp-selection-guide/", "ERP selection guide"), ("/resources/erp-readiness-checklist/", "ERP readiness checklist")],
        consultation=("/contact/erp-selection/", "Request an ERP Selection Consultation"),
    ),
    ProblemPage(
        title="Implementation at Risk",
        slug="implementation-at-risk",
        short="Triage missed milestones, unclear scope, weak testing, data delays, and partner performance before go-live risk becomes permanent.",
        looks_like=["Deadlines keep moving", "Risks repeat in status meetings", "Data, integrations, or reports are behind", "Business users lack confidence"],
        causes=["Weak governance", "Incomplete requirements", "Poor design decisions", "Insufficient testing", "Unclear ownership"],
        impact=["Budget overruns", "Go-live delay", "Lost user trust", "Post-launch instability"],
        systems=["ERP", "CRM", "billing", "middleware", "legacy ERP", "reporting"],
        services=["ERP Rescue", "Implementation Advisory", "Testing and UAT", "Go-Live Readiness"],
        deliverables=["Project triage report", "Risk ranking", "Recovery roadmap", "Executive decision summary"],
        resources=[("/resources/project-scenarios/", "ERP rescue scenario"), ("/resources/sample-deliverables/", "Sample risk register")],
        consultation=("/contact/erp-rescue/", "Review My ERP Implementation"),
    ),
    ProblemPage(
        title="Improve NetSuite",
        slug="improve-netsuite",
        short="Review NetSuite configuration, workflows, roles, reporting, integrations, revenue, close, and support model.",
        looks_like=["Users depend on saved search exports", "Month-end close is slower than expected", "Workflows and roles are confusing", "Integration issues keep returning"],
        causes=["Implementation shortcuts", "Unprioritized enhancements", "Customization debt", "Weak role governance", "Incomplete reporting design"],
        impact=["Manual work", "Poor adoption", "Reporting distrust", "Higher support load"],
        systems=["NetSuite", "Salesforce", "Stripe", "Chargebee", "Workato", "Celigo", "Power BI", "Snowflake"],
        services=["ERP Optimization", "Managed ERP Support", "Reporting and Analytics", "Integration and Automation"],
        deliverables=["NetSuite health findings", "Optimization backlog", "Workflow roadmap", "Reporting plan", "Support model"],
        resources=[("/resources/netsuite-optimization-guide/", "NetSuite optimization guide"), ("/platforms/oracle-netsuite/", "NetSuite consulting hub")],
        consultation=("/contact/netsuite-support/", "Request a NetSuite Health Check"),
    ),
    ProblemPage(
        title="Broken Integrations",
        slug="broken-integrations",
        short="Clarify system ownership, data mappings, error handling, monitoring, testing, and reconciliation across connected systems.",
        looks_like=["Salesforce and ERP numbers do not match", "Billing data arrives late or incorrectly", "Errors are discovered by users", "Manual imports replace automation"],
        causes=["No system-of-record rules", "Weak mappings", "No monitoring", "Poor integration testing", "Unclear ownership"],
        impact=["Duplicate data", "Manual reconciliation", "Revenue or billing delays", "Untrusted reporting"],
        systems=["NetSuite", "Salesforce", "HubSpot", "Stripe", "Chargebee", "Shopify", "Coupa", "Workato", "Celigo", "Boomi"],
        services=["Integration and Automation", "Reporting and Analytics", "Data Migration"],
        deliverables=["Integration architecture", "System-of-record matrix", "Error handling checklist", "Testing plan"],
        resources=[("/resources/sample-deliverables/", "Sample integration architecture"), ("/platforms/workato/", "Workato advisory")],
        consultation=("/contact/integration-review/", "Review My Integration Architecture"),
    ),
    ProblemPage(
        title="Unreliable Financial Reporting",
        slug="unreliable-reporting",
        short="Fix reporting root causes across metric definitions, data lineage, reconciliations, dashboards, and controls.",
        looks_like=["Reports disagree across teams", "Board reporting requires heavy spreadsheet work", "ERP reports do not reconcile to CRM, billing, or warehouse data"],
        causes=["Unclear KPI definitions", "Data ownership gaps", "Integration issues", "Manual transformations", "Weak report controls"],
        impact=["Slow decisions", "Board reporting risk", "Finance rework", "Low executive trust"],
        systems=["ERP", "CRM", "billing", "Power BI", "Tableau", "Looker", "Snowflake", "Excel"],
        services=["Reporting and Analytics", "ERP Assessment", "Integration and Automation"],
        deliverables=["Report inventory", "KPI definition workbook", "Dashboard requirements", "Reconciliation model"],
        resources=[("/resources/sample-deliverables/", "Sample reporting deliverables"), ("/solutions/business-processes/record-to-report/", "Record to Report")],
        consultation=("/contact/erp-assessment/", "Book an ERP Assessment"),
    ),
    ProblemPage(
        title="Preparing for Go-Live",
        slug="preparing-for-go-live",
        short="Evaluate defects, data, integrations, reports, controls, training, support, and cutover tasks before launch.",
        looks_like=["The launch date is close but readiness is unclear", "Critical defects remain open", "Cutover tasks are not fully owned", "Users need support planning"],
        causes=["Testing gaps", "Migration delays", "Weak cutover plan", "Incomplete training", "Unresolved decisions"],
        impact=["Launch delay", "Operational disruption", "Data errors", "User frustration"],
        systems=["ERP", "CRM", "billing", "integrations", "reporting", "support tools"],
        services=["Go-Live Readiness", "Testing and UAT", "Implementation Advisory"],
        deliverables=["Go-live readiness report", "Cutover checklist", "Hypercare plan", "Executive go/no-go summary"],
        resources=[("/resources/sample-deliverables/", "Sample go-live checklist"), ("/services/go-live-readiness/", "Go-live readiness service")],
        consultation=("/contact/go-live-readiness/", "Prepare for Go-Live"),
    ),
    ProblemPage(
        title="Need Ongoing ERP Support",
        slug="ongoing-erp-support",
        short="Build a support and enhancement model for ERP administration, reporting, users, releases, and integrations.",
        looks_like=["Support requests are ad hoc", "Enhancements stall", "Reports and integrations need steady care", "No clear ERP owner exists"],
        causes=["No support intake model", "Backlog is not prioritized", "ERP governance is informal", "Release changes are not planned"],
        impact=["Slow issue resolution", "Poor adoption", "Support debt", "More urgent fixes"],
        systems=["ERP", "CRM", "billing", "middleware", "reporting", "support tools"],
        services=["Managed ERP Support", "ERP Optimization", "Reporting and Analytics"],
        deliverables=["Support intake model", "Prioritized backlog", "Monthly support report", "Release checklist"],
        resources=[("/resources/engagement-packages/", "Managed support package"), ("/services/managed-erp-support/", "Managed ERP support")],
        consultation=("/contact/netsuite-support/", "Discuss Managed ERP Support"),
    ),
    ProblemPage(
        title="Replacing a Legacy ERP",
        slug="replacing-legacy-erp",
        short="Plan replacement around requirements, data migration, reporting, integrations, controls, and implementation readiness.",
        looks_like=["The legacy system cannot support growth", "Reporting and integrations depend on custom workarounds", "Only a few people understand the old system"],
        causes=["Outdated architecture", "Manual processes", "Poor documentation", "Unsupported customizations", "Growth beyond current controls"],
        impact=["Operational risk", "Reporting delays", "Data migration complexity", "Expensive implementation surprises"],
        systems=["Legacy ERP", "QuickBooks", "CRM", "billing", "inventory", "warehouse", "reporting"],
        services=["ERP Assessment", "ERP Selection", "Data Migration", "Implementation Advisory"],
        deliverables=["Replacement readiness findings", "Requirements workbook", "Migration strategy", "Implementation roadmap"],
        resources=[("/resources/erp-readiness-checklist/", "ERP readiness checklist"), ("/resources/erp-selection-guide/", "ERP selection guide")],
        consultation=("/contact/erp-assessment/", "Book an ERP Assessment"),
    ),
]


PROCESSES = [
    ProcessPage(
        title="Record to Report",
        slug="record-to-report",
        definition="Record to Report covers journal entries, approvals, reconciliations, intercompany, consolidation, foreign currency, fixed assets, accruals, close calendar, financial reporting, and audit support.",
        stages=["Transaction capture", "Journal entry and approval", "Reconciliation", "Consolidation", "Financial reporting", "Audit evidence"],
        departments=["Accounting", "FP&A", "Tax", "Operations", "IT"],
        systems=["ERP", "banking", "fixed assets", "intercompany tools", "reporting and BI"],
        problems=["Slow close", "Manual journals", "Unclear ownership", "Unreconciled reports", "Spreadsheet dependency"],
        controls=["Approval workflows", "segregation of duties", "close checklist", "report certification", "audit trail"],
        automation=["Journal templates", "bank feeds", "reconciliation rules", "close task management", "dashboard refresh"],
        reporting=["Trial balance", "financial statements", "entity consolidation", "variance analysis", "board reporting"],
        services=["ERP Assessment", "ERP Optimization", "Reporting and Analytics", "Internal Controls and Compliance"],
    ),
    ProcessPage(
        title="Order to Cash",
        slug="order-to-cash",
        definition="Order to Cash connects customer onboarding, order entry, fulfillment, billing, payments, collections, revenue recognition, and customer reporting.",
        stages=["Customer setup", "Order capture", "Fulfillment", "Billing", "Cash application", "Collections", "Revenue and reporting"],
        departments=["Sales Operations", "Finance", "Customer Success", "Operations", "IT"],
        systems=["CRM", "ERP", "billing", "payments", "ecommerce", "warehouse", "reporting"],
        problems=["Orders re-entered manually", "Billing delays", "Collections visibility gaps", "Revenue and fulfillment not aligned"],
        controls=["Customer approval", "credit checks", "billing review", "cash application controls", "revenue cut-off"],
        automation=["CRM to ERP order flow", "invoice generation", "payment matching", "dunning", "revenue schedules"],
        reporting=["Bookings", "billings", "cash collections", "DSO", "revenue by product", "customer margin"],
        services=["Integration and Automation", "Revenue Process Optimization", "ERP Selection", "Reporting and Analytics"],
    ),
    ProcessPage(
        title="Procure to Pay",
        slug="procure-to-pay",
        definition="Procure to Pay includes vendor onboarding, purchase requests, approvals, purchase orders, receiving, vendor bills, three-way match, payments, and spend reporting.",
        stages=["Vendor setup", "Requisition", "Approval", "Purchase order", "Receiving", "Vendor bill", "Payment", "Spend analysis"],
        departments=["Procurement", "Finance", "Operations", "IT", "Legal"],
        systems=["ERP", "procurement", "expense", "payments", "inventory", "reporting"],
        problems=["Email approvals", "late bills", "weak purchase controls", "manual three-way match", "poor spend visibility"],
        controls=["Vendor approval", "approval limits", "three-way match", "payment controls", "segregation of duties"],
        automation=["Purchase approvals", "PO matching", "invoice capture", "payment files", "spend dashboards"],
        reporting=["Spend by vendor", "open POs", "accruals", "payment timing", "budget variance"],
        services=["Business Process Review", "Integration and Automation", "Internal Controls and Compliance"],
    ),
    ProcessPage(
        title="Revenue Recognition",
        slug="revenue-recognition",
        definition="Revenue Recognition connects contracts, performance obligations, standalone selling price, allocation, revenue schedules, usage, modifications, deferred revenue, reconciliation, and audit evidence.",
        stages=["Contract review", "Obligation identification", "Allocation", "Schedule creation", "Revenue posting", "Deferred revenue reconciliation", "Disclosure reporting"],
        departments=["Revenue Accounting", "Sales Operations", "Legal", "Finance Systems", "Audit"],
        systems=["ERP", "CRM", "CPQ", "billing", "contract lifecycle management", "reporting"],
        problems=["Manual revenue schedules", "Contract changes not captured", "Deferred revenue reconciliation is hard", "Usage-based revenue lacks controls"],
        controls=["Contract review", "approval evidence", "schedule change controls", "reconciliation", "audit trail"],
        automation=["ARM configuration", "billing integration", "usage feed validation", "deferred revenue reports", "renewal workflows"],
        reporting=["Recognized revenue", "deferred revenue", "waterfall", "ARR/MRR tie-out", "revenue by product"],
        services=["ERP Assessment", "ERP Optimization", "Reporting and Analytics", "Internal Controls and Compliance"],
    ),
    ProcessPage(
        title="Subscription Billing",
        slug="subscription-billing",
        definition="Subscription Billing covers subscription creation, pricing, usage, billing schedules, invoices, credits, renewals, upgrades, downgrades, cancellations, revenue recognition, and collections.",
        stages=["Quote or order", "Subscription setup", "Billing schedule", "Usage capture", "Invoice", "Payment", "Renewal or change", "Revenue"],
        departments=["RevOps", "Billing", "Revenue Accounting", "Customer Success", "IT"],
        systems=["CRM", "CPQ", "billing platform", "ERP", "payments", "usage data", "reporting"],
        problems=["Manual billing changes", "Usage data arrives late", "Revenue and billing do not align", "Renewals are missed", "Credits are inconsistent"],
        controls=["Pricing approval", "billing review", "usage validation", "revenue tie-out", "credit approval"],
        automation=["CPQ to billing", "usage ingestion", "renewal notifications", "invoice generation", "payment reconciliation"],
        reporting=["ARR", "MRR", "churn", "renewals", "billings", "deferred revenue", "collections"],
        services=["Integration and Automation", "ERP Optimization", "Reporting and Analytics", "Finance Transformation"],
    ),
]


PLATFORMS = [
    PlatformPage(
        title="Oracle NetSuite",
        slug="oracle-netsuite",
        role="Maitero supports NetSuite assessment, implementation advisory, optimization, rescue, data migration, integrations, reporting, controls, automation, and managed support.",
        situations=["NetSuite implementation is in progress", "NetSuite is live but manual work remains", "Salesforce, Stripe, Shopify, Coupa, or reporting integrations need review", "Roles, workflows, saved searches, or close process need improvement"],
        functional=["General ledger", "AP and AR", "cash management", "fixed assets", "intercompany", "OneWorld", "multi-currency", "ARM", "SuiteBilling", "order management", "inventory", "project accounting"],
        technical=["SuiteScript", "SuiteFlow", "saved searches", "SuiteAnalytics", "SuiteQL", "RESTlets", "REST APIs", "SOAP", "OAuth", "custom records", "roles and permissions", "release management"],
        processes=["Record to Report", "Order to Cash", "Revenue Recognition", "Subscription Billing", "Procure to Pay"],
        integrations=["Salesforce to NetSuite", "Stripe to NetSuite", "Coupa to NetSuite", "Shopify to NetSuite", "NetSuite to Snowflake", "NetSuite to Power BI"],
        services=["NetSuite health check", "NetSuite optimization", "NetSuite integrations", "NetSuite reporting", "Managed ERP support"],
        industries=["Software and SaaS", "Professional Services", "Wholesale Distribution", "Retail and Ecommerce"],
        cta=("/contact/netsuite-support/", "Request a NetSuite Health Check"),
    ),
    PlatformPage(
        title="Microsoft Dynamics 365",
        slug="microsoft-dynamics-365",
        role="Maitero helps teams evaluate, implement, integrate, and optimize Dynamics 365 Business Central, Dynamics 365 Finance, and Dynamics CRM ecosystems.",
        situations=["Comparing Business Central and Finance", "Connecting Dynamics to Microsoft CRM, Power BI, or Power Platform", "Migrating from legacy systems", "Improving finance, procurement, inventory, or project operations"],
        functional=["Financial management", "multi-entity accounting", "procurement", "inventory", "manufacturing", "project operations", "CRM integration", "Power BI reporting"],
        technical=["Power Platform", "security roles", "Dataverse", "integration APIs", "workflow automation", "reporting models", "upgrade planning"],
        processes=["Record to Report", "Order to Cash", "Procure to Pay", "Inventory and Fulfillment"],
        integrations=["Dynamics CRM", "Power BI", "Microsoft 365", "banking", "warehouse systems", "ecommerce"],
        services=["ERP selection", "Implementation advisory", "Data migration", "Reporting and analytics", "ERP optimization"],
        industries=["Manufacturing", "Professional Services", "Wholesale Distribution", "Construction and Field Services"],
        cta=("/contact/erp-selection/", "Compare Dynamics 365 Fit"),
    ),
    PlatformPage(
        title="Sage Intacct",
        slug="sage-intacct",
        role="Maitero supports Sage Intacct evaluation, finance process design, multi-entity accounting, dimensions, reporting, integrations, optimization, and support planning.",
        situations=["Evaluating Sage Intacct for finance-led growth", "Improving dimensions and reporting", "Integrating Salesforce or billing systems", "Planning migration from QuickBooks"],
        functional=["Financial management", "multi-entity", "dimensions", "revenue management", "project accounting", "AP", "AR", "cash management", "consolidation"],
        technical=["Salesforce integration", "API integrations", "role design", "reporting dimensions", "planning integrations"],
        processes=["Record to Report", "Order to Cash", "Revenue Recognition", "Project Accounting"],
        integrations=["Salesforce", "Bill.com", "Stripe", "planning tools", "reporting tools"],
        services=["ERP selection", "Data migration", "Integration and automation", "Reporting and analytics"],
        industries=["Software and SaaS", "Professional Services", "Nonprofit Organizations"],
        cta=("/contact/erp-selection/", "Evaluate Sage Intacct"),
    ),
    PlatformPage(
        title="Acumatica",
        slug="acumatica",
        role="Maitero helps evaluate and improve Acumatica for finance, distribution, manufacturing, construction, inventory, field service, reporting, and integrations.",
        situations=["Evaluating Acumatica for distribution or manufacturing", "Planning data migration", "Connecting ecommerce or warehouse systems", "Improving inventory visibility"],
        functional=["Financial management", "distribution", "manufacturing", "construction", "project accounting", "inventory", "field service", "CRM", "ecommerce"],
        technical=["Workflow automation", "integration APIs", "reporting", "role security", "customization review"],
        processes=["Procure to Pay", "Order to Cash", "Inventory and Fulfillment", "Record to Report"],
        integrations=["Warehouse systems", "ecommerce", "CRM", "shipping", "EDI", "reporting"],
        services=["ERP selection", "Implementation advisory", "Data migration", "Integration and automation"],
        industries=["Manufacturing", "Wholesale Distribution", "Construction and Field Services", "Retail and Ecommerce"],
        cta=("/contact/erp-selection/", "Evaluate Acumatica"),
    ),
    PlatformPage(
        title="Odoo",
        slug="odoo",
        role="Maitero supports Odoo evaluation, implementation planning, module design, migration, integration, hosting decisions, upgrade planning, optimization, and support.",
        situations=["Considering Odoo for a broad operating suite", "Connecting sales, inventory, manufacturing, accounting, and ecommerce", "Planning custom modules or upgrades"],
        functional=["Accounting", "CRM", "sales", "purchase", "inventory", "manufacturing", "projects", "helpdesk", "ecommerce", "HR"],
        technical=["Custom modules", "hosting", "upgrade planning", "integrations", "workflow automation", "reporting"],
        processes=["Order to Cash", "Procure to Pay", "Inventory and Fulfillment", "Record to Report"],
        integrations=["Ecommerce", "payments", "shipping", "CRM", "reporting", "APIs"],
        services=["ERP selection", "Implementation advisory", "Data migration", "ERP optimization"],
        industries=["Retail and Ecommerce", "Manufacturing", "Professional Services", "Wholesale Distribution"],
        cta=("/contact/erp-selection/", "Evaluate Odoo"),
    ),
    PlatformPage(
        title="Salesforce",
        slug="salesforce",
        role="Maitero reviews Salesforce as a connected system in quote-to-cash, order-to-cash, billing, revenue, and ERP integration flows.",
        situations=["Salesforce and ERP do not match", "Opportunities, orders, subscriptions, or customer data need clean handoff", "Revenue and billing depend on Salesforce data"],
        functional=["Accounts", "opportunities", "products", "contracts", "subscriptions", "renewals", "customer success handoff"],
        technical=["APIs", "middleware", "field mappings", "system of record", "dedupe", "error monitoring"],
        processes=["Lead to Cash", "Quote to Cash", "Order to Cash", "Revenue Recognition"],
        integrations=["Salesforce to NetSuite", "Salesforce to Sage Intacct", "Salesforce to billing", "Salesforce to data warehouse"],
        services=["Integration and automation", "Requirements definition", "Reporting and analytics"],
        industries=["Software and SaaS", "Professional Services", "Technology Companies"],
        cta=("/contact/integration-review/", "Review Salesforce ERP Integration"),
    ),
    PlatformPage(
        title="Workato",
        slug="workato",
        role="Maitero reviews Workato architecture, recipes, mappings, monitoring, ownership, controls, and ERP integration fit.",
        situations=["Workato recipes are hard to govern", "Errors are recurring", "ERP, CRM, billing, or data integrations need clearer ownership", "Automation opportunities need prioritization"],
        functional=["Integration orchestration", "workflow automation", "approval automation", "data sync", "monitoring"],
        technical=["Recipes", "connectors", "APIs", "error handling", "retry logic", "authentication", "monitoring"],
        processes=["Lead to Cash", "Order to Cash", "Procure to Pay", "Reporting and Analytics"],
        integrations=["NetSuite", "Salesforce", "Stripe", "Shopify", "Snowflake", "Power BI", "Coupa"],
        services=["Integration architecture", "ERP optimization", "Reporting automation"],
        industries=["Software and SaaS", "Retail and Ecommerce", "Wholesale Distribution"],
        cta=("/contact/integration-review/", "Review Workato Architecture"),
    ),
]


INDUSTRIES = [
    IndustryPage("Software and SaaS", "software-saas", "Recurring revenue, subscriptions, renewals, usage, customer success, and multi-entity growth make ERP design highly dependent on billing, CRM, revenue, and reporting flow.", ["Subscription billing", "usage billing", "renewals", "contract modifications", "customer success systems"], ["Revenue recognition", "deferred revenue", "ARR and MRR reporting", "multi-entity accounting"], ["Salesforce integration", "Stripe or Chargebee integration", "ARM or revenue schedules", "SaaS metric reporting"], ["Quote to Cash", "Subscription Billing", "Revenue Recognition", "Record to Report"], ["Salesforce", "Stripe", "Chargebee", "HubSpot", "Snowflake"], ["NetSuite", "Sage Intacct", "Dynamics 365"], ["ERP Selection", "NetSuite Optimization", "Integration and Automation", "Reporting and Analytics"]),
    IndustryPage("Professional Services", "professional-services", "Project-based businesses need ERP processes that connect time, expense, project billing, revenue, resource planning, and profitability.", ["Project accounting", "time and expense", "resource management", "contract management"], ["Project billing", "revenue recognition", "utilization", "project profitability", "forecasting"], ["Project accounting", "approval workflows", "CRM integration", "margin reporting"], ["Project Accounting", "Order to Cash", "Record to Report"], ["CRM", "expense management", "time tracking", "planning"], ["Sage Intacct", "NetSuite", "Dynamics 365"], ["ERP Assessment", "ERP Selection", "Reporting and Analytics"]),
    IndustryPage("Manufacturing", "manufacturing", "Manufacturers need ERP decisions to account for inventory, procurement, production, costing, quality, planning, warehouse operations, and financial reporting.", ["Bill of materials", "work orders", "production planning", "MRP", "quality management"], ["Inventory costing", "margin reporting", "procurement controls", "close impact of inventory"], ["Inventory visibility", "shop floor integration", "EDI", "warehouse management"], ["Procure to Pay", "Order to Cash", "Record to Report"], ["Warehouse systems", "EDI", "shipping", "quality systems"], ["Dynamics 365", "Acumatica", "NetSuite", "Odoo"], ["ERP Selection", "Implementation Advisory", "Data Migration"]),
    IndustryPage("Wholesale Distribution", "wholesale-distribution", "Distribution companies need reliable inventory, purchasing, pricing, fulfillment, EDI, shipping, returns, and margin reporting.", ["Inventory", "warehousing", "order management", "purchasing", "demand planning"], ["Margin reporting", "inventory valuation", "customer-specific terms", "supplier management"], ["EDI", "shipping integrations", "warehouse management", "pricing rules"], ["Order to Cash", "Procure to Pay", "Inventory and Fulfillment"], ["EDI", "WMS", "shipping", "ecommerce"], ["NetSuite", "Acumatica", "Dynamics 365"], ["ERP Selection", "Integration and Automation", "Data Migration"]),
    IndustryPage("Retail and Ecommerce", "retail-ecommerce", "Retail and ecommerce ERP design must connect orders, inventory, POS, ecommerce, payments, returns, product data, sales tax, and revenue reporting.", ["Ecommerce integration", "POS", "omnichannel orders", "fulfillment", "returns"], ["Payment reconciliation", "sales tax", "inventory reporting", "revenue reporting"], ["Shopify integration", "payment matching", "product data ownership", "fulfillment rules"], ["Order to Cash", "Inventory and Fulfillment", "Record to Report"], ["Shopify", "Stripe", "Avalara", "warehouse", "shipping"], ["NetSuite", "Acumatica", "Odoo"], ["Integration and Automation", "ERP Optimization", "Data Migration"]),
    IndustryPage("Construction and Field Services", "construction-field-services", "Construction and field services companies need ERP processes around job costing, project billing, field service, procurement, equipment, retainage, and project profitability.", ["Job costing", "project costing", "field service", "change orders", "subcontractors"], ["Project profitability", "retainage", "revenue recognition", "equipment costing"], ["Field service integration", "mobile workflows", "procurement controls", "billing milestones"], ["Project Accounting", "Procure to Pay", "Record to Report"], ["Field service", "time tracking", "procurement", "reporting"], ["Acumatica", "Dynamics 365", "NetSuite"], ["ERP Selection", "Implementation Advisory", "Reporting and Analytics"]),
]


ENGAGEMENT_PACKAGES = [
    ("ERP Readiness Assessment", "2 to 4 weeks", "Best for teams deciding whether to optimize, replace, or prepare for ERP selection.", ["Assessment scorecard", "risk register", "roadmap"]),
    ("ERP Selection Sprint", "4 to 8 weeks", "Best for teams comparing platforms and implementation partners.", ["requirements workbook", "demo scripts", "vendor scorecard"]),
    ("ERP Rescue Review", "1 to 3 weeks", "Best for delayed or unstable ERP implementations.", ["triage report", "risk ranking", "recovery roadmap"]),
    ("NetSuite Health Check", "2 to 4 weeks", "Best for live NetSuite teams with reporting, workflow, role, integration, or close issues.", ["health findings", "optimization backlog", "support model"]),
    ("Data Migration Readiness Review", "2 to 4 weeks", "Best before trial migrations or cutover.", ["data inventory", "mapping review", "reconciliation plan"]),
    ("Integration Architecture Review", "2 to 4 weeks", "Best for ERP, CRM, billing, procurement, ecommerce, or reporting connection issues.", ["architecture map", "ownership matrix", "testing checklist"]),
    ("Go-Live Readiness Review", "1 to 3 weeks", "Best before launch decision.", ["readiness report", "cutover checklist", "go/no-go summary"]),
    ("ERP Optimization Roadmap", "2 to 6 weeks", "Best for live ERP systems with manual work and poor reporting.", ["optimization backlog", "30/60/90 roadmap", "executive readout"]),
]


DELIVERABLES = [
    ("ERP readiness scorecard", "Ranks readiness across strategy, finance, operations, data, integrations, reporting, controls, technology, people, governance, scalability, and compliance."),
    ("Requirements matrix", "Connects business needs to process, owner, priority, vendor response, configuration status, and testing evidence."),
    ("Vendor comparison scorecard", "Scores ERP platforms and implementation partners against functional fit, cost, complexity, support, and risk."),
    ("Current-state process map", "Shows current activities, systems, handoffs, manual work, controls, reports, and exceptions."),
    ("Integration architecture", "Documents system ownership, flow direction, frequency, data mappings, security, monitoring, and reconciliation."),
    ("Data migration tracker", "Tracks source, owner, cleansing, mapping, trial load, reconciliation, and sign-off status."),
    ("Risk register", "Prioritizes project, process, data, integration, reporting, control, and adoption risks with owner and due date."),
    ("UAT dashboard", "Shows test coverage, pass rate, defects, blocker status, retest ownership, and sign-off progress."),
    ("Cutover plan", "Defines pre-cutover, cutover, launch, rollback, and hypercare responsibilities."),
    ("Optimization roadmap", "Prioritizes fixes by impact, risk reduction, effort, dependency, and owner."),
]


def nav_items_for(items: list[ServicePage], group: str) -> str:
    links = []
    for item in items:
        if item.category == group:
            links.append(page_link(f"/services/{item.slug}/", item.title))
    return "".join(links)


def header() -> str:
    services_cols = "".join(
        f'<div><strong>{e(group)}</strong>{nav_items_for(SERVICES, group)}</div>'
        for group, _ in SERVICE_GROUPS
    )
    solution_links = """
      <div><strong>By business problem</strong>
        <a href="/solutions/business-problems/">Business Problems</a>
        <a href="/solutions/selecting-an-erp/">Selecting an ERP</a>
        <a href="/solutions/implementation-at-risk/">Implementation at Risk</a>
        <a href="/solutions/broken-integrations/">Broken Integrations</a>
        <a href="/solutions/unreliable-reporting/">Unreliable Reporting</a>
      </div>
      <div><strong>By process</strong>
        <a href="/solutions/business-processes/">Business Processes</a>
        <a href="/solutions/business-processes/record-to-report/">Record to Report</a>
        <a href="/solutions/business-processes/order-to-cash/">Order to Cash</a>
        <a href="/solutions/business-processes/procure-to-pay/">Procure to Pay</a>
        <a href="/solutions/business-processes/revenue-recognition/">Revenue Recognition</a>
      </div>
      <div><strong>By project stage</strong>
        <a href="/solutions/project-stage/">Project Stages</a>
        <a href="/solutions/preparing-for-go-live/">Preparing for Go-Live</a>
        <a href="/solutions/replacing-legacy-erp/">Replacing Legacy ERP</a>
        <a href="/solutions/ongoing-erp-support/">Ongoing ERP Support</a>
      </div>
    """
    platform_links = """
      <div><strong>ERP platforms</strong>
        <a href="/platforms/oracle-netsuite/">Oracle NetSuite</a>
        <a href="/platforms/microsoft-dynamics-365/">Microsoft Dynamics 365</a>
        <a href="/platforms/sage-intacct/">Sage Intacct</a>
        <a href="/platforms/acumatica/">Acumatica</a>
        <a href="/platforms/odoo/">Odoo</a>
      </div>
      <div><strong>Connected systems</strong>
        <a href="/platforms/salesforce/">Salesforce</a>
        <a href="/platforms/workato/">Workato</a>
        <a href="/services/integration-automation/">Integration Architecture</a>
      </div>
    """
    return f"""
    <div class="top-bar">
      <div class="top-bar-inner">
        <p>New: ERP readiness checklist and structured decision paths for selection, rescue, integration, and optimization.</p>
        <div class="utility-links"><a href="/resources/erp-readiness-checklist/">Readiness Checklist</a><a href="/contact/">Contact</a><a href="/contact/erp-assessment/">Book Assessment</a></div>
      </div>
    </div>
    <header class="site-header">
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="/" aria-label="Maitero ERP home"><img class="brand-logo" src="/assets/maitero-erp-logo.png?v={LOGO_VERSION}" alt="Maitero ERP" /></a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links"><span class="sr-only">Toggle navigation</span><span></span><span></span><span></span></button>
        <div class="nav-links" id="nav-links">
          <a href="/">Home</a>
          <div class="nav-item"><a href="/services/">Services</a><div class="dropdown mega-menu mega-services" aria-label="Services submenu">{services_cols}</div></div>
          <div class="nav-item"><a href="/solutions/">Solutions</a><div class="dropdown mega-menu mega-solutions" aria-label="Solutions submenu">{solution_links}</div></div>
          <div class="nav-item"><a href="/platforms/">Platforms</a><div class="dropdown mega-menu mega-platforms" aria-label="Platforms submenu">{platform_links}</div></div>
          <a href="/industries/">Industries</a>
          <a href="/resources/">Resources</a>
          <a href="/why-maitero/">Why Maitero</a>
          <a class="nav-cta" href="/contact/erp-assessment/">Book ERP Assessment</a>
        </div>
      </nav>
    </header>
    """


def footer() -> str:
    return f"""
    <footer class="footer">
      <div class="container footer-grid system-footer-grid">
        <div><a class="brand footer-brand" href="/" aria-label="Maitero ERP home"><img class="brand-logo" src="/assets/maitero-erp-logo.png?v={LOGO_VERSION}" alt="Maitero ERP" /></a><p>Systems Aligned. Business Accelerated.</p><p class="footer-note">Independent, finance-first ERP advisory for selection, implementation, rescue, integration, reporting, and optimization.</p></div>
        <div><h2>Services</h2><a href="/services/erp-assessment/">Assessment</a><a href="/services/erp-selection/">Selection</a><a href="/services/implementation-advisory/">Implementation</a><a href="/services/data-migration/">Data Migration</a><a href="/services/erp-rescue/">ERP Rescue</a><a href="/services/erp-optimization/">Optimization</a><a href="/services/managed-erp-support/">Managed Support</a></div>
        <div><h2>Solutions</h2><a href="/solutions/business-problems/">Business Problems</a><a href="/solutions/business-processes/">Business Processes</a><a href="/solutions/project-stage/">Project Stages</a><a href="/solutions/broken-integrations/">Broken Integrations</a><a href="/solutions/unreliable-reporting/">Unreliable Reporting</a></div>
        <div><h2>Platforms</h2><a href="/platforms/oracle-netsuite/">NetSuite</a><a href="/platforms/microsoft-dynamics-365/">Dynamics 365</a><a href="/platforms/sage-intacct/">Sage Intacct</a><a href="/platforms/acumatica/">Acumatica</a><a href="/platforms/odoo/">Odoo</a><a href="/platforms/salesforce/">Salesforce</a><a href="/platforms/workato/">Workato</a></div>
        <div><h2>Industries</h2><a href="/industries/software-saas/">SaaS</a><a href="/industries/professional-services/">Professional Services</a><a href="/industries/manufacturing/">Manufacturing</a><a href="/industries/wholesale-distribution/">Distribution</a><a href="/industries/retail-ecommerce/">Retail</a><a href="/industries/construction-field-services/">Construction</a></div>
        <div><h2>Resources</h2><a href="/resources/erp-selection-guide/">Guides</a><a href="/resources/erp-readiness-checklist/">Checklists</a><a href="/resources/sample-deliverables/">Sample Deliverables</a><a href="/resources/engagement-packages/">Engagement Packages</a><a href="/resources/project-scenarios/">Project Scenarios</a><a href="/why-maitero/">Company</a><a href="/contact/">Contact</a></div>
      </div>
      <div class="container footer-bottom">
        <p>&copy; 2026 Maitero ERP. All rights reserved.</p>
        <nav class="footer-legal-links" aria-label="Legal"><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a><a href="/sitemap.xml">Sitemap</a><a href="/contact/">Client Portal</a></nav>
      </div>
    </footer>
    """


def assistant() -> str:
    return """
    <div class="floating-assistant" aria-label="Maitero ERP assistant">
      <input class="assistant-toggle" id="maitero-assistant-toggle" type="checkbox" />
      <label class="assistant-button" for="maitero-assistant-toggle" aria-label="Open Maitero ERP assistant">
        <span class="assistant-status" aria-hidden="true"></span>
        <span class="assistant-button-text">ERP Assistant</span>
      </label>
      <section class="assistant-panel" aria-labelledby="maitero-assistant-title">
        <div class="assistant-panel-head">
          <p>Maitero Assistant</p>
          <label for="maitero-assistant-toggle" aria-label="Close Maitero ERP assistant">X</label>
        </div>
        <h2 id="maitero-assistant-title">Find the right ERP next step</h2>
        <p class="assistant-intro">Choose the closest situation. The assistant will recommend a service, page, resource, and consultation path.</p>
        <div class="assistant-choice-grid" data-assistant-choices>
          <button type="button" data-assistant-goal="select">Select an ERP</button>
          <button type="button" data-assistant-goal="improve">Improve an ERP</button>
          <button type="button" data-assistant-goal="rescue">Rescue implementation</button>
          <button type="button" data-assistant-goal="integration">Fix integration</button>
          <button type="button" data-assistant-goal="golive">Prepare for go-live</button>
          <button type="button" data-assistant-goal="reporting">Improve reporting</button>
          <button type="button" data-assistant-goal="netsuite">Improve NetSuite</button>
          <button type="button" data-assistant-goal="support">Ongoing support</button>
        </div>
        <div class="assistant-result" data-assistant-result aria-live="polite">
          <strong>Common starting point</strong>
          <p>Most teams begin with an ERP readiness assessment when the root cause is not clear.</p>
          <a class="assistant-cta" href="/contact/erp-assessment/">Book ERP Assessment</a>
        </div>
      </section>
    </div>
    """


def layout(title: str, description: str, output_path: str, body: str, schema: str = "") -> str:
    path = public_path(output_path)
    schema_html = f'\n    <script type="application/ld+json">{schema}</script>' if schema else ""
    return f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>{e(title)}</title>
        <meta name="description" content="{e(description)}" />
        <link rel="canonical" href="{e(full_url(path))}" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="Maitero ERP" />
        <meta property="og:title" content="{e(title)}" />
        <meta property="og:description" content="{e(description)}" />
        <meta property="og:url" content="{e(full_url(path))}" />
        <meta property="og:image" content="{DOMAIN}/assets/erp-advisory-hero.png" />
        <meta name="twitter:card" content="summary_large_image" />{schema_html}
        <link rel="icon" href="/assets/maitero-erp-mark.png?v={LOGO_VERSION}" type="image/png" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=Manrope:wght@600;700;800&amp;display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="/styles.css?v={CSS_VERSION}" />
      </head>
      <body>
        {header()}
        <main id="top">{body}</main>
        {footer()}
        {assistant()}
        <script src="/script.js?v={CSS_VERSION}"></script>
      </body>
    </html>
    """


def hero(kicker: str, title: str, description: str, hero_class: str = "page-services", actions: str = "") -> str:
    return f"""
    <section class="page-hero {e(hero_class)}">
      <div class="page-hero-inner">
        <p class="hero-brand">{e(kicker)}</p>
        <h1>{e(title)}</h1>
        <p>{e(description)}</p>
        {actions}
      </div>
    </section>
    """


def final_cta(title: str = "Your ERP project does not need more uncertainty.", body: str = "Tell Maitero where the project stands and receive guidance on the most practical next step.", href: str = "/contact/erp-assessment/", label: str = "Book an ERP Assessment") -> str:
    return f"""
    <section class="final-cta">
      <div class="container final-cta-inner">
        <div><p class="eyebrow">Next step</p><h2>{e(title)}</h2><p>{e(body)}</p></div>
        <a class="button button-primary" href="{e(href)}">{e(label)}</a>
      </div>
    </section>
    """


def card(title: str, text: str, href: str | None = None, link_label: str = "Explore", items: list[str] | None = None) -> str:
    body = f"<article class=\"page-card\"><h3>{e(title)}</h3><p>{e(text)}</p>"
    if items:
        body += list_html(items)
    if href:
        body += page_link(href, link_label)
    return body + "</article>"


def render_home() -> None:
    start_cards = [
        ("We are selecting an ERP", "Build requirements, score vendors, compare costs, and choose with evidence.", "/solutions/selecting-an-erp/"),
        ("Our implementation is at risk", "Triage governance, requirements, partner performance, data, integrations, testing, and launch risk.", "/solutions/implementation-at-risk/"),
        ("We need to improve NetSuite", "Review configuration, roles, workflows, reports, integrations, ARM, close, and support model.", "/solutions/improve-netsuite/"),
        ("Our systems are not connected", "Clarify system ownership, mappings, error handling, monitoring, and integration testing.", "/solutions/broken-integrations/"),
        ("Our reporting is unreliable", "Fix metric definitions, data lineage, reconciliations, dashboards, and controls.", "/solutions/unreliable-reporting/"),
        ("We are preparing for go-live", "Review defects, data, integrations, training, cutover, support, and executive go/no-go criteria.", "/solutions/preparing-for-go-live/"),
        ("We need ongoing ERP support", "Create a support model for administration, enhancements, releases, users, and integrations.", "/solutions/ongoing-erp-support/"),
        ("We are replacing a legacy system", "Plan requirements, data migration, integrations, controls, reporting, and implementation readiness.", "/solutions/replacing-legacy-erp/"),
    ]
    process_tabs = "".join(
        f'<button type="button" data-tab-target="{e(p.slug)}"{"" if i else " aria-selected=\"true\""}>{e(p.title)}</button>'
        for i, p in enumerate(PROCESSES[:5])
    )
    process_panels = "".join(
        f'<article class="process-panel{" is-active" if i == 0 else ""}" data-tab-panel="{e(p.slug)}"><h3>{e(p.title)}</h3><p>{e(p.definition)}</p><div class="mini-grid"><div><strong>Common problems</strong>{list_html(p.problems)}</div><div><strong>Automation opportunities</strong>{list_html(p.automation)}</div><div><strong>Relevant services</strong>{list_html(p.services)}</div></div><a href="/solutions/business-processes/{e(p.slug)}/">Explore {e(p.title)}</a></article>'
        for i, p in enumerate(PROCESSES[:5])
    )
    services_html = "".join(
        card(group, ", ".join(items), "/services/", "View services")
        for group, items in SERVICE_GROUPS
    )
    package_html = "".join(
        f'<article><span class="package-label">{e(duration)}</span><h3>{e(name)}</h3><p>{e(desc)}</p>{list_html(items, "deliverable-list")}<a href="/resources/engagement-packages/">Review package</a></article>'
        for name, duration, desc, items in ENGAGEMENT_PACKAGES[:8]
    )
    deliverables_html = "".join(card(name, desc, "/resources/sample-deliverables/", "View sample deliverables") for name, desc in DELIVERABLES[:6])
    industry_html = "".join(card(item.title, item.model, f"/industries/{item.slug}/", "Explore industry") for item in INDUSTRIES)
    resources_html = "".join(
        card(title, text, href, label)
        for title, text, href, label in [
            ("ERP readiness checklist", "Evaluate maturity, risks, and replacement readiness before starting selection.", "/resources/erp-readiness-checklist/", "Use checklist"),
            ("ERP selection guide", "Structure requirements, demos, vendor scoring, partner review, and total cost analysis.", "/resources/erp-selection-guide/", "Read guide"),
            ("NetSuite optimization guide", "Review workflows, saved searches, roles, reports, integrations, close, and support.", "/resources/netsuite-optimization-guide/", "Read guide"),
        ]
    )
    body = f"""
    <section class="hero home-hero" aria-label="Maitero ERP introduction">
      <div class="hero-media" aria-hidden="true"></div><div class="hero-overlay" aria-hidden="true"></div>
      <div class="hero-inner">
        <p class="hero-brand">Maitero ERP</p>
        <h1>Make Better ERP Decisions. Build Stronger Business Systems.</h1>
        <p class="hero-lede">Maitero helps growing companies assess, select, implement, integrate, and improve ERP systems through independent, finance-first advisory services.</p>
        <p class="hero-support">Enter through your service need, business problem, process, platform, industry, or project stage and move toward a clear next step.</p>
        <div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Book an ERP Assessment</a><a class="button button-secondary" href="/solutions/">Explore ERP Solutions</a></div>
        <div class="trust-bullets"><span>Independent advisory</span><span>Finance-first process review</span><span>Implementation-ready deliverables</span><span>Structured decision paths</span></div>
      </div>
    </section>
    <section class="proof-section"><div class="container proof-strip"><div><strong>What Maitero does</strong><span>Assessment, selection, implementation advisory, migration, integrations, reporting, rescue, optimization, and support.</span></div><div><strong>Who Maitero helps</strong><span>Growing finance, operations, and technology teams that need clearer ERP decisions.</span></div><div><strong>How Maitero is different</strong><span>Independent guidance centered on process, data, reporting, controls, and business ownership.</span></div><div><strong>What clients receive</strong><span>Scorecards, roadmaps, matrices, architecture, trackers, readiness reports, and executive recommendations.</span></div></div></section>
    <section class="section-pad"><div class="container"><div class="section-heading"><p class="eyebrow">Choose your situation</p><h2>Start with the way your team describes the problem.</h2><p>Visitors do not always know the consulting term. These paths connect common symptoms to the right service, resource, and consultation.</p></div><div class="page-card-grid routing-grid">{''.join(card(t, d, h, "Open path") for t, d, h in start_cards)}</div></div></section>
    <section class="section-pad alt"><div class="container"><div class="section-heading"><p class="eyebrow">Services overview</p><h2>Service groups aligned to the ERP transformation journey.</h2><p>Maitero services are organized by the stage of work: assess, select, implement, stabilize, optimize, and support.</p></div><div class="page-card-grid">{services_html}</div></div></section>
    <section class="section-pad"><div class="container"><div class="section-heading"><p class="eyebrow">Business process explorer</p><h2>Connect ERP problems to the process they affect.</h2><p>Each process path shows common problems, systems, controls, automation opportunities, deliverables, and related services.</p></div><div class="process-tabs" data-tabs>{process_tabs}</div><div class="process-panels">{process_panels}</div></div></section>
    <section class="method section-pad"><div class="container"><div class="section-heading"><p class="eyebrow">Maitero lifecycle</p><h2>Assess. Define. Select. Design. Implement. Test. Launch. Stabilize. Optimize.</h2><p>The methodology keeps decisions, requirements, data, integrations, testing, and business ownership visible through the ERP lifecycle.</p></div><ol class="timeline lifecycle">{''.join(f'<li><span>{i+1:02d}</span><h3>{e(step)}</h3><p>{e(copy)}</p></li>' for i, (step, copy) in enumerate([("Assess", "Review maturity, risks, systems, processes, reporting, and ownership."), ("Define", "Document requirements, controls, data, integrations, and reporting needs."), ("Select", "Compare platforms, partners, demos, costs, and implementation risk."), ("Design", "Review configuration, workflows, roles, reports, and integration architecture."), ("Test", "Trace requirements through UAT, defects, reports, and sign-off."), ("Launch", "Confirm data, cutover, training, support, and go/no-go readiness."), ("Stabilize", "Triage defects, reporting, support, and user adoption after launch."), ("Optimize", "Prioritize improvements, automation, controls, and managed support.")]))}</ol></div></section>
    <section class="section-pad platforms"><div class="container"><div class="section-heading"><p class="eyebrow">Platform ecosystem</p><h2>ERP decisions include connected systems.</h2><p>Maitero reviews ERP platforms together with CRM, billing, procurement, integration, data, and reporting systems.</p></div><div class="platform-groups">{''.join(card(p.title, p.role, f"/platforms/{p.slug}/", "Explore platform", p.integrations[:4]) for p in PLATFORMS)}</div></div></section>
    <section class="section-pad"><div class="container"><div class="section-heading"><p class="eyebrow">Engagement packages</p><h2>Defined scopes for the most common ERP decisions.</h2><p>Each package explains who it is for, duration, activities, stakeholders, deliverables, expected outcome, and next step.</p></div><div class="offer-grid">{package_html}</div></div></section>
    <section class="section-pad alt"><div class="container"><div class="section-heading"><p class="eyebrow">Sample deliverables</p><h2>Practical artifacts, not vague consulting language.</h2><p>See the types of documents used to make ERP decisions easier to review, govern, and execute.</p></div><div class="page-card-grid">{deliverables_html}</div></div></section>
    <section class="section-pad"><div class="container"><div class="section-heading"><p class="eyebrow">Industry experience</p><h2>ERP requirements differ by business model.</h2><p>Industry pages connect common challenges to processes, platforms, integrations, services, resources, and consultation paths.</p></div><div class="industry-grid">{industry_html}</div></div></section>
    <section class="section-pad alt"><div class="container split"><div><p class="eyebrow">Representative project scenario</p><h2>A finance-led ERP rescue before a risky launch.</h2><p class="large-copy">A software company preparing for NetSuite go-live had incomplete UAT, Salesforce integration defects, unclear revenue reporting, and unresolved data migration items. This is a representative scenario, not a verified customer case.</p></div><div class="check-panel"><h3>Maitero approach</h3>{list_html(["Triage governance, scope, data, integrations, reporting, and testing", "Rank launch blockers and assign decision owners", "Create recovery roadmap and executive go/no-go criteria", "Prepare hypercare and stabilization plan"])}<a class="inline-link" href="/resources/project-scenarios/">View project scenarios</a></div></div></section>
    <section class="resources section-pad"><div class="container"><div class="section-heading"><p class="eyebrow">Resources</p><h2>Guides, checklists, scenarios, and sample deliverables.</h2><p>Use the resource center to prepare for assessment, selection, implementation, rescue, migration, integration, optimization, and NetSuite improvement.</p></div><div class="resource-list">{resources_html}</div></div></section>
    {final_cta()}
    """
    schema = '{"@context":"https://schema.org","@type":"ProfessionalService","name":"Maitero ERP","url":"https://maitero.com/","logo":"https://maitero.com/assets/maitero-erp-logo.png?v=20260722-2","email":"rakeshbandi491@gmail.com","serviceType":["ERP Assessment","ERP Selection","ERP Implementation Advisory","ERP Data Migration","ERP Integration","ERP Optimization","Managed ERP Support"]}'
    write_file("index.html", layout("Maitero ERP Consulting for Growing Businesses", "Independent, finance-first ERP advisory for assessment, selection, implementation, rescue, data migration, integrations, reporting, optimization, and managed support.", "index.html", body, schema=schema))


def render_services_overview() -> None:
    groups = []
    for group, names in SERVICE_GROUPS:
        service_links = []
        for name in names:
            match = next((s for s in SERVICES if s.title == name), None)
            if match:
                service_links.append(f'<a href="/services/{match.slug}/">{e(match.title)}</a>')
        groups.append(f'<article class="page-card"><h3>{e(group)}</h3><p>{e(", ".join(names))}</p><div class="stacked-links">{"".join(service_links)}</div></article>')
    body = hero("Services", "ERP services organized by transformation stage.", "Assess readiness, select the right platform, guide implementation, rescue stalled projects, optimize current ERP, and support the system after launch.", "page-services", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Book an ERP Assessment</a><a class="button button-secondary" href="/solutions/">Explore Solutions</a></div>')
    body += f'<section class="page-section"><div class="container"><div class="section-heading"><p class="eyebrow">Service categories</p><h2>Start with the stage your team is in.</h2><p>Every service page follows the same structure: overview, who it is for, warning signs, questions answered, scope, methodology, stakeholders, timeline, deliverables, outcomes, related pages, FAQs, and CTA.</p></div><div class="page-card-grid">{"" .join(groups)}</div></div></section>'
    body += final_cta()
    write_file("services/index.html", layout("ERP Consulting Services | Maitero ERP", "Maitero ERP services for assessment, selection, implementation advisory, project management, data migration, integration, rescue, optimization, reporting, controls, and support.", "services/index.html", body))


def render_service_page(service: ServicePage) -> None:
    related_cards = [
        card("Related processes", "Business processes connected to this service.", "/solutions/business-processes/", "View processes", service.processes),
        card("Relevant platforms", "Platforms and connected systems commonly reviewed.", "/platforms/", "View platforms", service.platforms),
        card("Relevant industries", "Industry contexts where this service is commonly useful.", "/industries/", "View industries", service.industries),
        card("Related resource", f"Use the {service.resource[1]} to prepare for this work.", service.resource[0], service.resource[1]),
    ]
    faqs = service.faqs or [
        ("How does Maitero scope this service?", f"The first conversation clarifies project stage, systems involved, stakeholders, timing, and the deliverables needed for {service.title.lower()}."),
        ("What does the client need to provide?", "Maitero usually needs access to process owners, current reports, system documentation, issue lists, project artifacts, and relevant data or integration inventories."),
    ]
    body = hero("Service", service.title, service.hero, service.accent_class, f'<div class="hero-actions"><a class="button button-primary" href="{e(service.cta_path)}">{e(service.cta_label)}</a><a class="button button-secondary" href="/services/">View All Services</a></div>')
    body += f"""
    <section class="page-section">
      <div class="container page-layout">
        <aside class="article-aside"><p class="eyebrow">{e(service.category)}</p><h2>Service summary</h2><p>{e(service.short)}</p><div class="article-meta"><span>Typical timeline: {e(service.timeline)}</span><span>Primary CTA: {e(service.cta_label)}</span></div></aside>
        <div class="content-stack">
          <article class="content-card"><h3>Who this service is for</h3>{list_html(service.audience)}</article>
          <article class="content-card"><h3>Problems addressed</h3>{list_html(service.problems)}</article>
          <article class="content-card"><h3>Warning signs</h3>{list_html(service.warnings)}</article>
          <article class="content-card"><h3>Questions Maitero answers</h3>{list_html(service.questions)}</article>
        </div>
      </div>
    </section>
    <section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">Scope and methodology</p><h2>What Maitero performs during the engagement.</h2></div><div class="page-card-grid">{card("Scope of work", "The main workstreams in this engagement.", None, items=service.scope)}{card("Activities performed", "Practical activities used to create evidence and decisions.", None, items=service.activities)}{card("Systems reviewed", "Systems and process artifacts commonly reviewed.", None, items=service.systems)}{card("Documents required", "Typical inputs requested from the client team.", None, items=service.documents)}{card("Stakeholders involved", "People usually needed for the work.", None, items=service.stakeholders)}{card("Maitero responsibilities", "Structure the work, identify risks, document findings, facilitate decisions, and produce usable deliverables.", None, items=["Facilitate workshops", "Review artifacts", "Maintain issue and decision clarity", "Prepare executive readouts"])}</div></div></section>
    <section class="page-section"><div class="container"><div class="section-heading"><p class="eyebrow">Deliverables and outcomes</p><h2>What the client receives.</h2></div><div class="outcomes-grid">{card("Deliverables", "Tangible outputs from the engagement.", None, items=service.deliverables)}{card("Sample deliverable", service.sample, "/resources/sample-deliverables/", "View sample deliverables")}{card("Expected outcomes", "The business results this work is designed to support.", None, items=service.outcomes)}</div></div></section>
    <section class="page-section alt"><div class="container"><div class="page-card-grid">{card("Risks addressed", "Common risks this service reduces.", None, items=service.risks)}{card("What is not included", "Clear boundaries keep the scope useful and controlled.", None, items=service.not_included)}{card("Optional services", "Common next scopes that pair with this work.", None, items=service.optional)}</div></div></section>
    <section class="page-section"><div class="container"><div class="section-heading"><p class="eyebrow">Related pathways</p><h2>Connect this service to the rest of the Maitero system.</h2></div><div class="page-card-grid">{''.join(related_cards)}</div></div></section>
    <section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">FAQs</p><h2>Common questions about {e(service.title)}.</h2></div><div class="faq-list">{''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)}</div></div></section>
    {final_cta(href=service.cta_path, label=service.cta_label)}
    """
    write_file(f"services/{service.slug}/index.html", layout(f"{service.title} | Maitero ERP", service.short, f"services/{service.slug}/index.html", body))


def render_solutions() -> None:
    problem_cards = "".join(card(p.title, p.short, f"/solutions/{p.slug}/", "Open solution") for p in PROBLEMS)
    process_cards = "".join(card(p.title, p.definition, f"/solutions/business-processes/{p.slug}/", "Explore process") for p in PROCESSES)
    stages = ["Exploring ERP", "Preparing an ERP business case", "Gathering requirements", "Comparing ERP platforms", "Selecting an implementation partner", "Preparing for implementation", "Implementation in progress", "Data migration in progress", "Testing and UAT", "Preparing for go-live", "Post-go-live stabilization", "Optimizing an existing ERP", "Replacing a failed ERP", "Preparing for expansion or acquisition"]
    body = hero("Solutions", "Find help by problem, process, or project stage.", "Use Maitero solution paths when you know the situation but not the exact consulting service you need.", "page-services", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Book ERP Assessment</a><a class="button button-secondary" href="/services/">View Services</a></div>')
    body += f'<section class="page-section"><div class="container"><div class="section-heading"><p class="eyebrow">By business problem</p><h2>Start with the symptom your team recognizes.</h2></div><div class="page-card-grid">{problem_cards}</div></div></section>'
    body += f'<section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">By business process</p><h2>Connect ERP work to operational flow.</h2></div><div class="page-card-grid">{process_cards}</div></div></section>'
    body += f'<section class="page-section"><div class="container split"><div><p class="eyebrow">By project stage</p><h2>Match guidance to where the ERP project stands.</h2><p class="large-copy">A visitor can enter before selection, during implementation, near go-live, after launch, or while optimizing an existing ERP.</p><a class="button navy-button" href="/solutions/project-stage/">View Project Stages</a></div><div class="check-panel"><h3>Stages covered</h3>{list_html(stages)}</div></div></section>{final_cta()}'
    write_file("solutions/index.html", layout("ERP Solutions by Problem, Process, and Stage | Maitero ERP", "Find Maitero ERP services by business problem, business process, ERP platform, industry, or project stage.", "solutions/index.html", body))
    write_file("solutions/business-problems/index.html", layout("ERP Business Problems | Maitero ERP", "ERP problem paths for slow close, broken integrations, unreliable reporting, failed implementation, poor adoption, legacy replacement, and support gaps.", "solutions/business-problems/index.html", hero("Business Problems", "ERP issues usually show up as business symptoms.", "Each problem page explains what the problem looks like, causes, impact, systems involved, Maitero services, deliverables, resources, and consultation path.", "page-services") + f'<section class="page-section"><div class="container"><div class="page-card-grid">{problem_cards}</div></div></section>{final_cta()}'))
    write_file("solutions/business-processes/index.html", layout("ERP Business Process Consulting | Maitero ERP", "Business process paths for Record to Report, Order to Cash, Procure to Pay, Revenue Recognition, and Subscription Billing.", "solutions/business-processes/index.html", hero("Business Processes", "ERP value depends on process clarity.", "Each process page connects common problems, systems, controls, automation, reporting, services, deliverables, and related resources.", "page-services") + f'<section class="page-section"><div class="container"><div class="page-card-grid">{process_cards}</div></div></section>{final_cta()}'))
    write_file("solutions/project-stage/index.html", layout("ERP Project Stage Guidance | Maitero ERP", "ERP project-stage guidance from exploration and business case through requirements, implementation, testing, go-live, stabilization, rescue, and optimization.", "solutions/project-stage/index.html", hero("Project Stages", "Find Maitero guidance by where the ERP project stands.", "Use project-stage paths when your team knows timing and risk but not the exact service name.", "page-implementation") + f'<section class="page-section"><div class="container"><div class="page-card-grid">{ "".join(card(stage, "Recommended next step, related service, expected deliverables, and consultation path for this ERP stage.", "/contact/erp-assessment/", "Discuss this stage") for stage in stages) }</div></div></section>{final_cta()}'))


def render_problem_page(problem: ProblemPage) -> None:
    service_links = [f"/services/{next((s.slug for s in SERVICES if s.title == name), 'erp-assessment')}/" for name in problem.services]
    body = hero("Solution", problem.title, problem.short, "page-services", f'<div class="hero-actions"><a class="button button-primary" href="{e(problem.consultation[0])}">{e(problem.consultation[1])}</a><a class="button button-secondary" href="/solutions/business-problems/">All Problems</a></div>')
    body += f"""
    <section class="page-section"><div class="container page-layout"><aside class="article-aside"><p class="eyebrow">Problem path</p><h2>From symptom to next step.</h2><p>{e(problem.short)}</p>{badge_list(problem.services)}</aside><div class="content-stack">{card("What the problem looks like", "Signals a business team usually notices first.", None, items=problem.looks_like)}{card("Common causes", "Root causes Maitero investigates before recommending software or process changes.", None, items=problem.causes)}{card("Business impact", "Why this problem matters beyond system frustration.", None, items=problem.impact)}</div></div></section>
    <section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">Systems and workstreams</p><h2>What Maitero reviews.</h2></div><div class="page-card-grid">{card("Systems involved", "Common systems or data sources behind this problem.", None, items=problem.systems)}{card("Maitero services", "Services that usually address this problem.", None, items=problem.services)}{card("Recommended deliverables", "Outputs that help the team make progress.", None, items=problem.deliverables)}</div></div></section>
    <section class="page-section"><div class="container"><div class="section-heading"><p class="eyebrow">Related pages</p><h2>Keep moving through the decision path.</h2></div><div class="page-card-grid">{''.join(card(name, "Service commonly used to address this problem.", href, "View service") for name, href in zip(problem.services, service_links))}{''.join(card(label, "Resource connected to this problem.", href, "Open resource") for href, label in problem.resources)}</div></div></section>
    {final_cta(href=problem.consultation[0], label=problem.consultation[1])}
    """
    write_file(f"solutions/{problem.slug}/index.html", layout(f"{problem.title} | Maitero ERP Solutions", problem.short, f"solutions/{problem.slug}/index.html", body))


def render_process_page(process: ProcessPage) -> None:
    body = hero("Business Process", process.title, process.definition, "page-implementation", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Request Process Assessment</a><a class="button button-secondary" href="/solutions/business-processes/">All Processes</a></div>')
    body += f"""
    <section class="page-section"><div class="container page-layout"><aside class="article-aside"><p class="eyebrow">Process definition</p><h2>Why it matters</h2><p>{e(process.definition)}</p></aside><div class="content-stack">{card("Process stages", "The activities Maitero maps and reviews.", None, items=process.stages)}{card("Departments involved", "Teams that typically own or influence the process.", None, items=process.departments)}{card("Systems involved", "Systems and data sources commonly connected.", None, items=process.systems)}</div></div></section>
    <section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">Risk and improvement areas</p><h2>Common problems, controls, automation, and reporting needs.</h2></div><div class="page-card-grid">{card("Common problems", "Symptoms that create ERP friction.", None, items=process.problems)}{card("Common control risks", "Control points that need system support.", None, items=process.controls)}{card("Automation opportunities", "Where workflow and integration can remove manual work.", None, items=process.automation)}{card("Reporting requirements", "Outputs the process must support.", None, items=process.reporting)}{card("Maitero approach", "Review the current state, define future-state requirements, connect systems, and produce deliverables.", None, items=["Process map", "requirements matrix", "controls and reporting view", "optimization roadmap"])}{card("Recommended services", "Services commonly tied to this process.", "/services/", "View services", process.services)}</div></div></section>
    {final_cta("Need a clearer ERP process?", "Maitero can review the process, identify system gaps, and define practical next steps.", "/contact/erp-assessment/", "Request Process Assessment")}
    """
    write_file(f"solutions/business-processes/{process.slug}/index.html", layout(f"{process.title} ERP Process Consulting | Maitero ERP", process.definition, f"solutions/business-processes/{process.slug}/index.html", body))


def render_platforms() -> None:
    body = hero("Platforms", "ERP and connected system advisory.", "Maitero works across ERP, CRM, billing, procurement, integration, data, and reporting platforms so business processes connect cleanly.", "page-platforms", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-selection/">Compare ERP Platforms</a><a class="button button-secondary" href="/services/integration-automation/">Review Integrations</a></div>')
    body += f'<section class="page-section"><div class="container"><div class="section-heading"><p class="eyebrow">Platform categories</p><h2>ERP decisions include the surrounding ecosystem.</h2></div><div class="platform-groups">{ "".join(card(p.title, p.role, f"/platforms/{p.slug}/", "Explore platform", p.services[:4]) for p in PLATFORMS) }</div></div></section>{final_cta(href="/contact/erp-selection/", label="Compare ERP Platforms")}'
    write_file("platforms/index.html", layout("ERP and Business Systems Platforms | Maitero ERP", "Maitero ERP advisory for NetSuite, Dynamics 365, Sage Intacct, Acumatica, Odoo, Salesforce, Workato, integrations, reporting, and connected systems.", "platforms/index.html", body))


def render_platform_page(platform: PlatformPage) -> None:
    hero_class = "page-netsuite" if "NetSuite" in platform.title else "page-dynamics" if "Dynamics" in platform.title else "page-platforms"
    body = hero("Platform", platform.title, platform.role, hero_class, f'<div class="hero-actions"><a class="button button-primary" href="{e(platform.cta[0])}">{e(platform.cta[1])}</a><a class="button button-secondary" href="/platforms/">All Platforms</a></div>')
    body += f"""
    <section class="page-section"><div class="container page-layout"><aside class="article-aside"><p class="eyebrow">Maitero role</p><h2>Platform-specific advisory.</h2><p>{e(platform.role)}</p></aside><div class="content-stack">{card("Common client situations", "When this platform page is relevant.", None, items=platform.situations)}{card("Functional capabilities", "Business capabilities Maitero reviews.", None, items=platform.functional)}{card("Technical capabilities", "Technical areas involved in architecture, support, or optimization.", None, items=platform.technical)}</div></div></section>
    <section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">Connected work</p><h2>Processes, integrations, services, and industry use cases.</h2></div><div class="page-card-grid">{card("Business processes supported", "Processes commonly connected to this platform.", "/solutions/business-processes/", "View processes", platform.processes)}{card("Common integrations", "Connected systems and data flows often reviewed.", "/services/integration-automation/", "Review integrations", platform.integrations)}{card("Implementation services", "How Maitero helps around implementation and optimization.", "/services/", "View services", platform.services)}{card("Industry use cases", "Industries where this platform is commonly evaluated.", "/industries/", "View industries", platform.industries)}{card("Data migration", "Source data, mappings, history, open transactions, and reconciliation planning.", "/services/data-migration/", "Plan migration")}{card("Reporting and controls", "Reports, dashboards, roles, permissions, approvals, and audit evidence.", "/services/reporting-analytics/", "Improve reporting")}</div></div></section>
    {final_cta(f"Need clearer {platform.title} decisions?", "Maitero can review fit, implementation quality, data, integrations, reporting, controls, and optimization priorities.", platform.cta[0], platform.cta[1])}
    """
    write_file(f"platforms/{platform.slug}/index.html", layout(f"{platform.title} Consulting | Maitero ERP", platform.role, f"platforms/{platform.slug}/index.html", body))


def render_industries() -> None:
    body = hero("Industries", "ERP requirements differ by business model.", "Maitero industry pages connect operational challenges, finance needs, ERP capabilities, integrations, services, resources, and consultation paths.", "page-industries", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Book Industry Assessment</a><a class="button button-secondary" href="/solutions/">Explore Solutions</a></div>')
    body += f'<section class="page-section"><div class="container"><div class="industry-grid">{ "".join(card(i.title, i.model, f"/industries/{i.slug}/", "Explore industry", i.requirements[:4]) for i in INDUSTRIES) }</div></div></section>{final_cta()}'
    write_file("industries/index.html", layout("Industries Served | Maitero ERP", "ERP advisory by industry for SaaS, professional services, manufacturing, wholesale distribution, retail and ecommerce, construction and field services.", "industries/index.html", body))


def render_industry_page(industry: IndustryPage) -> None:
    body = hero("Industry", industry.title, industry.model, "page-industries", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Book Industry Consultation</a><a class="button button-secondary" href="/industries/">All Industries</a></div>')
    body += f"""
    <section class="page-section"><div class="container page-layout"><aside class="article-aside"><p class="eyebrow">Business model</p><h2>{e(industry.title)} ERP needs.</h2><p>{e(industry.model)}</p></aside><div class="content-stack">{card("Operational challenges", "The operating details ERP must support.", None, items=industry.operations)}{card("Finance and reporting challenges", "Finance issues that shape ERP requirements.", None, items=industry.finance)}{card("Required ERP capabilities", "Capabilities commonly reviewed during assessment or selection.", None, items=industry.requirements)}</div></div></section>
    <section class="page-section alt"><div class="container"><div class="section-heading"><p class="eyebrow">Recommended pathways</p><h2>Processes, integrations, platforms, and services.</h2></div><div class="page-card-grid">{card("Important business processes", "Processes commonly reviewed for this industry.", "/solutions/business-processes/", "View processes", industry.processes)}{card("Common integrations", "Connected systems commonly involved.", "/services/integration-automation/", "Review integrations", industry.integrations)}{card("Recommended ERP platforms", "Platforms commonly evaluated for this industry.", "/platforms/", "View platforms", industry.platforms)}{card("Maitero services", "Services commonly useful for this industry.", "/services/", "View services", industry.services)}{card("Industry project scenario", "Representative project patterns, risks, deliverables, and expected improvements.", "/resources/project-scenarios/", "View scenarios")}{card("Industry deliverables", "Requirements, process maps, data plans, integration architecture, dashboards, and roadmaps.", "/resources/sample-deliverables/", "View deliverables")}</div></div></section>
    {final_cta(f"Need ERP guidance for {industry.title}?", "Maitero can connect your industry requirements to the right service, platform, process, deliverables, and consultation path.", "/contact/erp-assessment/", "Book Industry Consultation")}
    """
    write_file(f"industries/{industry.slug}/index.html", layout(f"{industry.title} ERP Consulting | Maitero ERP", industry.model, f"industries/{industry.slug}/index.html", body))


def render_resources() -> None:
    resource_cards = [
        ("ERP Readiness Checklist", "A practical checklist for maturity, process, data, integration, reporting, controls, people, governance, scalability, and compliance.", "/resources/erp-readiness-checklist/"),
        ("ERP Selection Guide", "A guide to requirements, shortlist, RFP, demos, scorecards, partner review, cost analysis, and selection mistakes.", "/resources/erp-selection-guide/"),
        ("NetSuite Optimization Guide", "A NetSuite guide covering close, reporting, workflows, saved searches, roles, permissions, integrations, ARM, and support.", "/resources/netsuite-optimization-guide/"),
        ("Maitero Methodology", "The finance-first lifecycle from assess and define through launch, stabilization, and optimization.", "/resources/methodology/"),
        ("Engagement Packages", "Defined packages for assessment, selection, rescue, health checks, migration, integrations, go-live, and optimization.", "/resources/engagement-packages/"),
        ("Sample Deliverables", "Examples of scorecards, matrices, architectures, migration trackers, risk registers, UAT dashboards, and roadmaps.", "/resources/sample-deliverables/"),
        ("Project Scenarios", "Representative scenarios showing client profile, situation, systems, risks, approach, deliverables, timeline, and outcomes.", "/resources/project-scenarios/"),
    ]
    body = hero("Resources", "Guides, checklists, templates, scenarios, and sample deliverables.", "The resource center helps visitors prepare for ERP assessment, selection, implementation, rescue, migration, integration, optimization, and NetSuite improvement.", "page-resources", '<div class="hero-actions"><a class="button button-primary" href="/resources/erp-readiness-checklist/">Use Readiness Checklist</a><a class="button button-secondary" href="/contact/erp-assessment/">Book Assessment</a></div>')
    body += f'<section class="page-section"><div class="container"><div class="resource-index">{ "".join(card(t, d, h, "Open resource") for t, d, h in resource_cards) }</div></div></section>{final_cta()}'
    write_file("resources/index.html", layout("ERP Resource Center | Maitero ERP", "ERP guides, checklists, templates, assessments, project scenarios, sample deliverables, and NetSuite resources from Maitero ERP.", "resources/index.html", body))
    render_methodology()
    render_engagement_packages()
    render_sample_deliverables()
    render_project_scenarios()
    render_simple_resource("ERP Readiness Checklist", "resources/erp-readiness-checklist/index.html", "Use this checklist before ERP selection, implementation, rescue, or optimization.", ["Strategy and sponsorship", "Finance close and reporting", "Operations process clarity", "Data ownership and quality", "Integration inventory", "Controls and compliance", "People and governance", "Scalability and growth"], "/contact/erp-assessment/", "Book an ERP Assessment")
    render_simple_resource("ERP Selection Guide", "resources/erp-selection-guide/index.html", "Use this guide to structure ERP requirements, shortlist, demos, vendor scoring, implementation partner review, and cost analysis.", ["Business case", "Stakeholder alignment", "Functional requirements", "Technical requirements", "Reporting requirements", "Integration requirements", "Vendor shortlist", "RFP and demo scripts", "Scorecards", "Final recommendation"], "/contact/erp-selection/", "Request ERP Selection Consultation")
    render_simple_resource("NetSuite Optimization Guide", "resources/netsuite-optimization-guide/index.html", "Use this guide to review NetSuite workflows, roles, permissions, reports, saved searches, integrations, revenue, close, controls, and support.", ["Configuration health", "Close process", "Saved searches", "SuiteAnalytics", "Roles and permissions", "Workflow automation", "ARM and revenue", "Integration monitoring", "Enhancement backlog", "Release management"], "/contact/netsuite-support/", "Request NetSuite Health Check")


def render_methodology() -> None:
    steps = [("Assess", "Review maturity, pain points, process, systems, data, reporting, integrations, controls, people, and governance."), ("Define", "Translate findings into requirements, ownership, priorities, risks, and success criteria."), ("Select", "Compare ERP platforms, demos, partners, pricing, and implementation risk."), ("Design", "Review solution design, workflows, roles, integrations, reports, controls, and customization decisions."), ("Implement", "Support governance, project management, requirements traceability, data, integrations, and partner accountability."), ("Test", "Plan UAT, trace requirements, triage defects, reconcile reports, and document sign-off."), ("Launch", "Review cutover, data, training, support, and executive go/no-go readiness."), ("Stabilize", "Prioritize defects, support, reporting, user adoption, and enhancement backlog after go-live."), ("Optimize", "Build a 30/60/90 roadmap for automation, controls, reporting, integrations, and managed support.")]
    body = hero("Methodology", "A finance-first ERP advisory lifecycle.", "Maitero keeps business decisions, deliverables, ownership, and risk visible from first assessment through optimization.", "page-about")
    body += f'<section class="page-section"><div class="container"><ol class="timeline lifecycle">{ "".join(f"<li><span>{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>" for i, (t, d) in enumerate(steps)) }</ol></div></section>{final_cta()}'
    write_file("resources/methodology/index.html", layout("Maitero ERP Methodology", "Maitero ERP methodology for assessment, requirements, selection, design, implementation, testing, go-live, stabilization, and optimization.", "resources/methodology/index.html", body))


def render_engagement_packages() -> None:
    package_html = "".join(f'<article class="page-card"><span class="package-label">{e(duration)}</span><h3>{e(name)}</h3><p>{e(desc)}</p>{list_html(items)}<a href="/contact/erp-assessment/">Discuss package</a></article>' for name, duration, desc, items in ENGAGEMENT_PACKAGES)
    body = hero("Engagement Packages", "Defined ERP advisory packages.", "Packages explain best-fit client, duration, meetings, activities, stakeholders, deliverables, outcomes, and follow-on services.", "page-services")
    body += f'<section class="page-section"><div class="container"><div class="page-card-grid">{package_html}</div></div></section>{final_cta()}'
    write_file("resources/engagement-packages/index.html", layout("ERP Engagement Packages | Maitero ERP", "Defined Maitero ERP engagement packages for readiness, selection, rescue, NetSuite health, data migration, integration architecture, go-live readiness, and optimization.", "resources/engagement-packages/index.html", body))


def render_sample_deliverables() -> None:
    deliverable_html = "".join(card(name, desc, "/contact/erp-assessment/", "Discuss deliverable") for name, desc in DELIVERABLES)
    body = hero("Sample Deliverables", "Examples of the artifacts Maitero produces.", "Each deliverable explains what it is, why it is used, who uses it, when it is produced, what it contains, and how it improves the project.", "page-resources")
    body += f'<section class="page-section"><div class="container"><div class="page-card-grid">{deliverable_html}</div></div></section>{final_cta()}'
    write_file("resources/sample-deliverables/index.html", layout("ERP Sample Deliverables | Maitero ERP", "Sample ERP deliverables including readiness scorecards, process maps, requirements matrices, vendor scorecards, integration architecture, data migration trackers, risk registers, UAT dashboards, cutover plans, and roadmaps.", "resources/sample-deliverables/index.html", body))


def render_project_scenarios() -> None:
    scenarios = [
        ("Representative ERP rescue before go-live", "A software company approaching NetSuite go-live had incomplete UAT, Salesforce integration defects, unclear revenue reporting, and unresolved data migration items.", ["Project triage", "risk ranking", "go-live readiness report", "hypercare plan"]),
        ("Representative legacy ERP replacement", "A distributor outgrew a legacy ERP with weak inventory visibility, manual reporting, and undocumented EDI dependencies.", ["readiness assessment", "requirements matrix", "migration strategy", "platform shortlist"]),
        ("Representative reporting stabilization", "A services company had board reports rebuilt manually from ERP, CRM, and planning exports.", ["report inventory", "KPI definitions", "data lineage", "dashboard roadmap"]),
    ]
    body = hero("Project Scenarios", "Representative ERP situations and Maitero response.", "Until verified public case studies are available, these scenarios are clearly labeled as representative examples rather than customer claims.", "page-resources")
    body += f'<section class="page-section"><div class="container"><div class="page-card-grid">{ "".join(card(t, d, "/contact/erp-assessment/", "Discuss similar situation", items) for t, d, items in scenarios) }</div></div></section>{final_cta()}'
    write_file("resources/project-scenarios/index.html", layout("Representative ERP Project Scenarios | Maitero ERP", "Representative ERP project scenarios covering rescue, legacy ERP replacement, reporting stabilization, systems involved, problems, risks, approach, deliverables, timeline, and outcomes.", "resources/project-scenarios/index.html", body))


def render_simple_resource(title: str, output_path: str, description: str, items: list[str], cta_path: str, cta_label: str) -> None:
    body = hero("Resource", title, description, "page-resources", f'<div class="hero-actions"><a class="button button-primary" href="{e(cta_path)}">{e(cta_label)}</a><a class="button button-secondary" href="/resources/">All Resources</a></div>')
    body += f'<section class="page-section"><div class="container article-layout"><aside class="article-aside"><p class="eyebrow">How to use it</p><h2>Prepare the next ERP discussion.</h2><p>{e(description)}</p></aside><div class="content-stack"><article class="resource-article"><h2>Topics covered</h2>{list_html(items)}</article><article class="resource-article"><h2>Recommended next step</h2><p>Use this resource to collect the current state, identify missing decisions, and choose the relevant Maitero consultation path.</p><div class="resource-callout"><strong>Conversion path</strong><p>Bring the answers into the consultation so the first call can focus on the highest-risk decision.</p></div></article></div></div></section>{final_cta(href=cta_path, label=cta_label)}'
    write_file(output_path, layout(f"{title} | Maitero ERP", description, output_path, body))


def render_why_maitero() -> None:
    body = hero("Why Maitero", "Independent, finance-first ERP guidance.", "Maitero builds trust through detailed methodology, practical deliverables, platform fluency, representative scenarios, transparent engagement structure, and useful resources.", "page-about", '<div class="hero-actions"><a class="button button-primary" href="/contact/erp-assessment/">Book ERP Assessment</a><a class="button button-secondary" href="/resources/sample-deliverables/">View Deliverables</a></div>')
    body += f"""
    <section class="page-section"><div class="container"><div class="page-card-grid">{card("Finance-first advisory", "ERP decisions are evaluated through close, reporting, controls, billing, revenue, cash, and operational visibility.", "/resources/methodology/", "View methodology")}{card("Independent guidance", "Maitero is not positioned as a software reseller. The focus is fit, risk, process, data, and execution quality.", "/services/erp-selection/", "Review selection support")}{card("Practical deliverables", "Every engagement produces artifacts the client can use to make decisions and manage work.", "/resources/sample-deliverables/", "See deliverables")}{card("How engagements work", "Engagements begin with project stage, business impact, systems involved, stakeholders, timeline, and deliverables.", "/resources/engagement-packages/", "View packages")}{card("Leadership perspective", "The work is designed for CFOs, controllers, operations, IT, RevOps, and executive sponsors who need clear decisions.", "/contact/", "Contact Maitero")}{card("Technology ecosystem", "ERP is reviewed with CRM, billing, procurement, integration, data, reporting, and spreadsheet dependencies.", "/platforms/", "View platforms")}</div></div></section>{final_cta()}"""
    write_file("why-maitero/index.html", layout("Why Maitero ERP", "Why choose Maitero ERP for independent, finance-first ERP assessment, selection, implementation advisory, rescue, data migration, integrations, optimization, reporting, and support.", "why-maitero/index.html", body))


CONTACT_INTENTS = {
    "general": ("Contact Maitero ERP", "Tell Maitero what is happening with your ERP project.", "General inquiry"),
    "erp-assessment": ("Book an ERP Assessment", "Share your current ERP, company size, entities, challenges, project stage, and target timeline.", "ERP Assessment"),
    "erp-selection": ("Request an ERP Selection Consultation", "Share current systems, reason for replacement, platforms under consideration, required go-live date, and decision stakeholders.", "ERP Selection"),
    "erp-rescue": ("Review My ERP Implementation", "Share ERP platform, implementation partner, current phase, primary risks, planned go-live date, and project status.", "ERP Rescue"),
    "netsuite-support": ("Request a NetSuite Health Check", "Share NetSuite modules, main issue, integrations, subsidiaries, and required support type.", "NetSuite Support"),
    "data-migration": ("Review My Data Migration Plan", "Share source systems, data owners, migration stage, trial load status, reconciliation issues, and cutover timing.", "Data Migration"),
    "integration-review": ("Review My Integration Architecture", "Share connected systems, middleware, main sync issue, ownership gaps, error handling, and reporting impact.", "Integration Review"),
    "go-live-readiness": ("Prepare for Go-Live", "Share launch date, open defects, data status, integration status, training status, and support model.", "Go-Live Readiness"),
}


def render_contact(intent: str, output_path: str) -> None:
    title, desc, label = CONTACT_INTENTS[intent]
    form = f"""
    <form class="contact-form" action="https://formsubmit.co/{EMAIL}" method="post" data-contact-form>
      <input type="hidden" name="_subject" value="New Maitero ERP {e(label)} request" />
      <input type="hidden" name="_template" value="table" />
      <input type="hidden" name="_captcha" value="false" />
      <input type="hidden" name="_next" value="https://maitero.com/thanks.html" />
      <input type="hidden" name="intent" value="{e(label)}" data-intent-field />
      <input type="hidden" name="assistant-recommendation" value="" data-assistant-field />
      <input type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" hidden />
      <label>Name<input type="text" name="name" autocomplete="name" required /></label>
      <label>Company<input type="text" name="company" autocomplete="organization" required /></label>
      <label>Email<input type="email" name="email" autocomplete="email" required /></label>
      <label>Phone<input type="tel" name="phone" autocomplete="tel" /></label>
      <label>Current ERP system<select name="current-erp"><option value="">Select one</option><option>QuickBooks or spreadsheets</option><option>NetSuite</option><option>Microsoft Dynamics</option><option>Sage Intacct</option><option>Acumatica</option><option>Odoo</option><option>Legacy ERP</option><option>Other</option></select></label>
      <label>Company size<select name="company-size"><option value="">Select one</option><option>Under 50 employees</option><option>50-150 employees</option><option>150-500 employees</option><option>500+ employees</option></select></label>
      <label>Number of entities<select name="entities"><option value="">Select one</option><option>1 entity</option><option>2-5 entities</option><option>6-15 entities</option><option>16+ entities</option></select></label>
      <label>Project stage<select name="project-stage"><option value="">Select one</option><option>Exploring ERP</option><option>Building business case</option><option>Selecting ERP</option><option>Implementation in progress</option><option>Data migration in progress</option><option>Testing and UAT</option><option>Preparing for go-live</option><option>Post-go-live</option><option>Optimizing existing ERP</option></select></label>
      <label class="full">Primary challenge<select name="challenge" required><option value="">Select one</option><option>Need to select a new ERP</option><option>Implementation is at risk</option><option>Need to improve NetSuite</option><option>Systems are disconnected</option><option>Reporting is unreliable</option><option>Data migration is risky</option><option>Preparing for go-live</option><option>Need ongoing ERP support</option></select></label>
      <label class="full">Target timeline<select name="timeline"><option value="">Select one</option><option>Immediate</option><option>Next 30 days</option><option>Next quarter</option><option>3-6 months</option><option>Researching options</option></select></label>
      <label class="full">Connected systems<input type="text" name="connected-systems" placeholder="Example: Salesforce, Stripe, Shopify, Workato, Power BI" /></label>
      <label class="full">Message<textarea name="message" rows="5" placeholder="{e(desc)}"></textarea></label>
      <button class="button button-primary full" type="submit">Submit {e(label)} Request</button>
      <p class="form-privacy">By submitting this form, you agree that Maitero ERP may use the information to respond to your request. See the <a href="/privacy.html">privacy notice</a>.</p>
    </form>
    """
    body = hero("Contact", title, desc, "page-contact")
    body += f'<section class="contact section-pad"><div class="container contact-layout"><div><p class="eyebrow">{e(label)}</p><h2>Share the project stage, systems, risks, and timing.</h2><p>{e(desc)}</p><div class="contact-points"><span>Response within one business day</span><span>Matched consultation path</span><span>Clear next-step recommendation</span></div><div class="contact-confidence"><div class="response-card"><strong>Prefer direct email?</strong><a href="mailto:{EMAIL}">{EMAIL}</a><p>Include your current ERP, connected systems, and target timeline.</p></div><div><h3>What happens next</h3><ol class="next-steps"><li>Maitero reviews your request by service intent.</li><li>The first conversation focuses on business impact, project stage, and immediate risk.</li><li>You receive a practical next step, recommended deliverables, and proposed scope.</li></ol></div></div></div>{form}</div></section>'
    write_file(output_path, layout(f"{title} | Maitero ERP", desc, output_path, body))


def render_legal() -> None:
    privacy = hero("Privacy", "Privacy notice.", "How Maitero ERP handles information submitted through the website.", "page-about") + f'<section class="page-section"><div class="container legal-page"><p>Information submitted through Maitero ERP forms is used to respond to the request, evaluate fit, and communicate about relevant ERP advisory services. Do not submit confidential system exports, passwords, or sensitive regulated data through the public website form.</p><div class="legal-section"><h2>Information collected</h2><p>Forms may collect name, company, email, phone, current ERP, project stage, systems involved, and message details.</p></div><div class="legal-section"><h2>Contact</h2><p>Questions can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></div></section>'
    terms = hero("Terms", "Website terms.", "General terms for using the Maitero ERP website.", "page-about") + '<section class="page-section"><div class="container legal-page"><p>The information on this website is provided for general business and ERP planning purposes. It is not legal, tax, accounting, security, or audit advice. Engagement scope, deliverables, pricing, and responsibilities are defined in a separate written agreement.</p><div class="legal-section"><h2>No warranty</h2><p>Maitero ERP does not guarantee software vendor pricing, implementation partner performance, or specific business outcomes from website content alone.</p></div></div></section>'
    thanks = hero("Thank You", "Your request was received.", "Maitero ERP will review the details and respond with the most relevant next step.", "page-contact") + '<section class="page-section"><div class="container"><div class="page-card-grid"><article class="page-card"><h3>While you wait</h3><p>Use the readiness checklist to organize current systems, challenges, and timeline.</p><a href="/resources/erp-readiness-checklist/">Open checklist</a></article><article class="page-card"><h3>Explore services</h3><p>Review the service path that matches your project stage.</p><a href="/services/">View services</a></article><article class="page-card"><h3>View deliverables</h3><p>See examples of artifacts Maitero uses to make ERP work clearer.</p><a href="/resources/sample-deliverables/">View deliverables</a></article></div></div></section>'
    page404 = hero("404", "This page could not be found.", "The URL may have changed as Maitero moved to hierarchical service, solution, platform, industry, and resource pages.", "page-contact") + '<section class="page-section"><div class="container"><div class="page-card-grid"><article class="page-card"><h3>Services</h3><p>Assessment, selection, implementation, rescue, optimization, and support.</p><a href="/services/">View services</a></article><article class="page-card"><h3>Solutions</h3><p>Find help by business problem, process, or project stage.</p><a href="/solutions/">View solutions</a></article><article class="page-card"><h3>Contact</h3><p>Describe the ERP situation and receive a practical next-step recommendation.</p><a href="/contact/erp-assessment/">Book assessment</a></article></div></div></section>'
    write_file("privacy.html", layout("Privacy Policy | Maitero ERP", "Maitero ERP privacy notice for website form and consultation request information.", "privacy.html", privacy))
    write_file("terms.html", layout("Terms | Maitero ERP", "Maitero ERP website terms and general use notice.", "terms.html", terms))
    write_file("thanks.html", layout("Thank You | Maitero ERP", "Thank you for contacting Maitero ERP.", "thanks.html", thanks))
    write_file("404.html", layout("Page Not Found | Maitero ERP", "The requested Maitero ERP page could not be found.", "404.html", page404), include_in_sitemap=False)


def render_alias(output_path: str, target_path: str, title: str) -> None:
    html = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta http-equiv="refresh" content="0; url={e(target_path)}" />
        <link rel="canonical" href="{e(full_url(target_path))}" />
        <title>{e(title)} moved | Maitero ERP</title>
        <link rel="icon" href="/assets/maitero-erp-mark.png?v={LOGO_VERSION}" type="image/png" />
        <link rel="stylesheet" href="/styles.css?v={CSS_VERSION}" />
      </head>
      <body>
        <main class="alias-page"><a class="brand" href="/"><img class="brand-logo" src="/assets/maitero-erp-logo.png?v={LOGO_VERSION}" alt="Maitero ERP" /></a><h1>{e(title)} moved.</h1><p>This page now lives at <a href="{e(target_path)}">{e(target_path)}</a>.</p></main>
      </body>
    </html>
    """
    write_file(output_path, html, include_in_sitemap=False)


def render_aliases() -> None:
    aliases = {
        "services.html": ("/services/", "Services"),
        "platforms.html": ("/platforms/", "Platforms"),
        "industries.html": ("/industries/", "Industries"),
        "resources.html": ("/resources/", "Resources"),
        "about.html": ("/why-maitero/", "Why Maitero"),
        "contact.html": ("/contact/", "Contact"),
        "erp-assessment.html": ("/services/erp-assessment/", "ERP Assessment"),
        "erp-selection.html": ("/services/erp-selection/", "ERP Selection"),
        "implementation-support.html": ("/services/implementation-advisory/", "ERP Implementation Advisory"),
        "data-migration.html": ("/services/data-migration/", "Data Migration"),
        "erp-integrations.html": ("/services/integration-automation/", "Integration and Automation"),
        "erp-optimization.html": ("/services/erp-optimization/", "ERP Optimization"),
        "netsuite-consulting.html": ("/platforms/oracle-netsuite/", "NetSuite Consulting"),
        "microsoft-dynamics-consulting.html": ("/platforms/microsoft-dynamics-365/", "Microsoft Dynamics 365 Consulting"),
        "erp-selection-checklist.html": ("/resources/erp-readiness-checklist/", "ERP Selection Checklist"),
        "erp-project-risk-guide.html": ("/resources/project-scenarios/", "ERP Project Risk Guide"),
        "data-migration-checklist.html": ("/services/data-migration/", "Data Migration Checklist"),
        "netsuite-vs-dynamics-guide.html": ("/platforms/", "NetSuite vs Dynamics Guide"),
        "erp-demo-scorecard.html": ("/resources/erp-selection-guide/", "ERP Demo Scorecard"),
        "erp-integration-planning-guide.html": ("/services/integration-automation/", "ERP Integration Planning Guide"),
    }
    for output_path, (target, title) in aliases.items():
        render_alias(output_path, target, title)


def render_sitemap() -> None:
    unique = []
    for path in WRITTEN_CANONICAL:
        if path not in unique:
            unique.append(path)
    urls = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in sorted(unique, key=lambda item: (item != "/", item)):
        priority = "1.0" if path == "/" else "0.9" if path in ["/services/", "/solutions/", "/platforms/", "/resources/", "/contact/"] else "0.7"
        urls.append(f"  <url><loc>{e(full_url(path))}</loc><lastmod>{LASTMOD}</lastmod><priority>{priority}</priority></url>")
    urls.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(urls) + "\n", encoding="utf-8")


def render_robots() -> None:
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://maitero.com/sitemap.xml\n", encoding="utf-8")


def main() -> None:
    render_home()
    render_services_overview()
    for service in SERVICES:
        render_service_page(service)
    render_solutions()
    for problem in PROBLEMS:
        render_problem_page(problem)
    for process in PROCESSES:
        render_process_page(process)
    render_platforms()
    for platform in PLATFORMS:
        render_platform_page(platform)
    render_industries()
    for industry in INDUSTRIES:
        render_industry_page(industry)
    render_resources()
    render_why_maitero()
    for intent in CONTACT_INTENTS:
        path = "contact/index.html" if intent == "general" else f"contact/{intent}/index.html"
        render_contact(intent, path)
    render_legal()
    render_aliases()
    render_sitemap()
    render_robots()


if __name__ == "__main__":
    main()
