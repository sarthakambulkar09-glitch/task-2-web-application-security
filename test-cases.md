Security Test Cases

Project

Project Name: SecureLab – Web Application Security Testing Portal

Task: Task 2 – Web Application Security Testing

Testing Environment: Localhost

Target: http://127.0.0.1:5000

---

TC-01 – Valid Login

Objective

Verify that a valid test account can successfully authenticate.

Test Steps

1. Open the SecureLab login page.
2. Enter the authorized test username.
3. Enter the corresponding test password.
4. Click Login.

Expected Result

The user should be authenticated and redirected to the dashboard.

Actual Result

The application successfully authenticated the valid test account.

Status

PASS

Evidence

"01-login-page.png" and "02-successful-login.png"

---

TC-02 – Invalid Login

Objective

Verify that incorrect credentials are rejected.

Test Steps

1. Open the login page.
2. Enter a valid test username.
3. Enter an incorrect password.
4. Click Login.

Expected Result

The application should reject the login attempt and display an appropriate error message.

Actual Result

The application rejected the invalid credentials and displayed an error message.

Status

PASS

Evidence

"03-invalid-login.png"

---

TC-03 – Unauthenticated Dashboard Access

Objective

Verify that the dashboard cannot be accessed without authentication.

Test Steps

1. Log out from the application.
2. Open:

"http://127.0.0.1:5000/dashboard"

3. Observe the application response.

Expected Result

An unauthenticated user should not be allowed to access the dashboard.

Actual Result

The application redirected the unauthenticated request to the login page.

Status

PASS

Evidence

"04-access-control.png"

---

TC-04 – Input Handling

Objective

Check whether user-controlled input is safely handled before being displayed.

Test Steps

1. Login to the application.
2. Open the Dashboard.
3. Locate the Search Query field.
4. Enter a harmless HTML test value such as:

"<test>"

5. Submit the form.
6. Observe the response.

Expected Result

User-controlled input should be safely encoded before being displayed in the HTML response.

Actual Result

The submitted value was reflected in the response without safe output encoding.

Status

FAIL

Finding

Potential Reflected Cross-Site Scripting / Unsafe Output Encoding.

Evidence

"05-input-handling.png"

---

TC-05 – HTTP Security Headers

Objective

Review the HTTP response for commonly recommended security headers.

Test Steps

1. Start the local Flask application.
2. Send a HEAD request to the local application.
3. Review the returned HTTP response headers.

Expected Result

Appropriate security headers should be configured according to the application's security requirements.

Actual Result

Record the headers actually observed during testing.

Status

FAIL / REVIEW REQUIRED

Finding

Missing or incomplete HTTP security headers, if confirmed during testing.

Evidence

"06-security-headers.png"

---

Test Summary

Test Case| Test Area| Result
TC-01| Valid Authentication| PASS
TC-02| Invalid Authentication| PASS
TC-03| Access Control| PASS
TC-04| Input Handling| FAIL
TC-05| Security Headers| FAIL / REVIEW REQUIRED

---

Testing Limitation

Testing was performed only against the intentionally created local application running on "127.0.0.1".

No third-party, production, or unauthorized website was tested.
