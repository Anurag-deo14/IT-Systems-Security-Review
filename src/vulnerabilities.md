## Identified Vulnerabilities

1. **Weak Password (Login System)**:
   - The system allows weak passwords such as "1234".
   - **Impact**: Easy for attackers to guess the password and access the admin panel.
   - **Recommendation**: Enforce stronger password policies (min. 8 characters, including letters, numbers, special characters).

2. **No HTTPS (Insecure Communication)**:
   - The web app does not use HTTPS, exposing sensitive data like passwords in transit.
   - **Impact**: Attackers can intercept communications between the server and users.
   - **Recommendation**: Implement HTTPS with a valid SSL certificate.

3. **Missing Rate Limiting (Brute-force attack)**:
   - There is no rate limiting on the login endpoint, allowing brute-force attacks.
   - **Recommendation**: Implement rate limiting to restrict login attempts.
