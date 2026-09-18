Task 2 – Web Application Security Testing

Overview

This project demonstrates basic web application security testing using an intentionally vulnerable Flask web application running locally.

The purpose of the project is to identify common web application security issues, document their risk levels, provide evidence, and recommend appropriate remediation.

Application

Application Name: SecureLab – Web Security Testing Portal

Technology: Python, Flask

Testing Environment: Localhost

Target:

"http://127.0.0.1:5000"

Objectives

The assessment was performed to:

- Test authentication controls
- Test access control
- Test input handling
- Review HTTP security headers
- Identify basic OWASP Top 10-related weaknesses
- Document security findings with evidence
- Provide recommended fixes

Scope

Testing was performed only against the locally created SecureLab application.

No unauthorized public websites, systems, or third-party applications were tested.

Application Features

The application contains:

- Login page
- Authentication
- Dashboard
- Search functionality
- Session management
- Logout functionality
- Basic user profile functionality

Security Testing Methodology

The following testing activities were performed:

1. Authentication testing
2. Invalid-login testing
3. Authentication/access-control testing
4. Input-handling testing
5. Security-header review
6. Basic automated scanning with OWASP ZAP

Vulnerabilities Identified

ID| Finding| Risk
VUL-01| Weak Authentication / Predictable Test Credentials| High
VUL-02| Insecure Input Handling / Reflected XSS| High
VUL-03| Missing Security Headers| Medium

VUL-01 – Weak Authentication

Description

The intentionally vulnerable test application contains predictable test credentials.

Risk

High

Impact

Weak or predictable credentials can make unauthorized account access easier if similar credentials are used in a real application.

Evidence

See:

"screenshots/02-successful-login.png"

Recommended Fix

- Enforce strong password requirements.
- Remove default or predictable credentials.
- Store passwords using a secure password-hashing algorithm.
- Implement login rate limiting.
- Consider multi-factor authentication for sensitive accounts.

---

VUL-02 – Insecure Input Handling / Reflected XSS

Description

The search functionality reflects user-controlled input into the HTML response without appropriate output encoding.

Risk

High

Impact

Improper handling of user-controlled input can allow attacker-controlled content to be interpreted by a user's browser.

Evidence

See:

"screenshots/05-input-handling.png"

Recommended Fix

- Apply contextual output encoding.
- Validate input on the server side.
- Use safe template rendering.
- Avoid constructing HTML using untrusted input.
- Deploy an appropriate Content Security Policy.

---

VUL-03 – Missing Security Headers

Description

The application does not configure several commonly recommended HTTP security headers.

Risk

Medium

Impact

Missing security headers can reduce browser-side security protections.

Evidence

See:

"screenshots/06-security-headers.png"

Recommended Fix

Configure appropriate security headers, including where applicable:

- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Strict-Transport-Security for HTTPS deployments

---

Positive Security Control

The application performs an authentication check before allowing access to the dashboard.

When the dashboard is requested without an authenticated session, the user is redirected to the login page.

Evidence:

"screenshots/04-access-control.png"

Test Cases

Test ID| Test| Expected Result
TC-01| Login with valid credentials| Authentication succeeds
TC-02| Login with invalid password| Authentication is rejected
TC-03| Access dashboard without authentication| User is redirected to login
TC-04| Submit special characters through search| Input should be safely handled
TC-05| Review security headers| Appropriate security headers should be configured

Evidence

Screenshots are stored in:

screenshots/
├── 01-login-page.png
├── 02-successful-login.png
├── 03-invalid-login.png
├── 04-access-control.png
├── 05-input-handling.png
├── 06-security-headers.png
├── 07-zap-results.png
└── 08-local-server.png

Tools Used

- Python
- Flask
- Web Browser / Developer Tools
- OWASP ZAP
- Git and GitHub

Security & Ethical Considerations

This project was created for educational security testing.

The application is intentionally vulnerable and must only be used in a controlled local environment.

Testing was restricted to the locally created application.

Conclusion

The assessment identified weaknesses related to authentication, input handling, and HTTP security configuration.

The exercise demonstrates a basic security-testing workflow:

Identify → Test → Capture Evidence → Assess Risk → Recommend Fix → Document

The identified issues should be addressed before deploying an equivalent application to a production environment.
