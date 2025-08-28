# CTF Methodology Guide

This guide outlines systematic approaches to tackling different types of CTF challenges.

## 🎯 General CTF Approach

### 1. Read and Understand
- **Read carefully**: Understand exactly what the challenge is asking for
- **Note keywords**: Look for hints in the challenge description
- **Identify category**: Determine the primary challenge type
- **Check constraints**: Note any time limits, attempt limits, or special rules

### 2. Initial Reconnaissance
- **Gather information**: Collect all provided files, URLs, and resources
- **Document everything**: Keep notes from the very beginning
- **First impressions**: Record your initial thoughts and hypotheses

### 3. Systematic Analysis
- **Use appropriate tools**: Select tools based on challenge category
- **Follow methodology**: Apply category-specific approaches (see below)
- **Document progress**: Keep detailed notes of what you try and what you find

### 4. Solution and Verification
- **Test thoroughly**: Ensure your solution works reliably
- **Document the process**: Write up how you solved it
- **Extract learning**: Identify what you learned for future challenges

## 📂 Category-Specific Methodologies

### Web Security Challenges

1. **Source Code Analysis**
   - View page source (Ctrl+U)
   - Check developer tools (F12)
   - Look for comments, hidden fields, JavaScript

2. **Network Analysis**
   - Use Burp Suite or OWASP ZAP
   - Intercept and analyze HTTP requests
   - Check headers, cookies, parameters

3. **Common Vulnerabilities**
   - SQL Injection: Test input fields
   - XSS: Look for user input reflection
   - Directory traversal: Test file access
   - Command injection: Test system command execution

4. **Tools to Try**
   - `curl`, `wget` for HTTP requests
   - `sqlmap` for SQL injection
   - `dirb`, `gobuster` for directory enumeration

### Cryptography Challenges

1. **Identify the Cipher**
   - Look for patterns in the ciphertext
   - Consider common encoding (Base64, hex, etc.)
   - Identify cipher type (Caesar, Vigenère, RSA, etc.)

2. **Frequency Analysis**
   - For substitution ciphers
   - Look for common letter patterns
   - Use statistical analysis tools

3. **Key Recovery**
   - Brute force weak keys
   - Look for key reuse or weak key generation
   - Analyze mathematical properties

4. **Tools to Try**
   - `hashcat`, `john` for password cracking
   - `openssl` for cryptographic operations
   - Online cipher tools and analyzers

### Forensics Challenges

1. **File Analysis**
   - Check file headers and metadata
   - Use `file`, `strings`, `hexdump` commands
   - Look for hidden data or steganography

2. **Network Forensics**
   - Analyze packet captures with Wireshark
   - Look for unusual traffic patterns
   - Extract files from network streams

3. **Memory/Disk Forensics**
   - Use Volatility for memory analysis
   - Analyze filesystem artifacts
   - Recover deleted files

4. **Tools to Try**
   - `binwalk` for firmware analysis
   - `steghide`, `stegsolve` for steganography
   - `volatility` for memory analysis

### Binary Exploitation (PWN)

1. **Static Analysis**
   - Disassemble the binary
   - Identify security mitigations
   - Look for obvious vulnerabilities

2. **Dynamic Analysis**
   - Run the program and observe behavior
   - Test with various inputs
   - Use debuggers to trace execution

3. **Exploitation**
   - Develop exploit based on vulnerability
   - Bypass security mitigations
   - Chain vulnerabilities if necessary

4. **Tools to Try**
   - `gdb`, `radare2` for debugging
   - `checksec` for security analysis
   - `pwntools` for exploit development

### Reverse Engineering

1. **Static Analysis**
   - Disassemble the binary
   - Analyze program flow
   - Identify key functions and algorithms

2. **Dynamic Analysis**
   - Run the program with various inputs
   - Use debuggers to understand runtime behavior
   - Trace function calls and memory access

3. **Pattern Recognition**
   - Look for known algorithms
   - Identify obfuscation techniques
   - Recognize common library functions

4. **Tools to Try**
   - `IDA Pro`, `Ghidra` for disassembly
   - `ltrace`, `strace` for system call tracing
   - `upx` for unpacking

## 🤝 Collaboration Best Practices

### Working with AI Agents
1. **Clear Communication**: Provide context and specific questions
2. **Iterative Approach**: Work through problems step by step
3. **Verification**: Always verify suggestions and solutions
4. **Learning Focus**: Ask for explanations, not just answers

### Documentation Standards
1. **Reproducible Steps**: Document so others can follow
2. **Tool Commands**: Include exact commands used
3. **Failure Analysis**: Document what didn't work and why
4. **Resource Links**: Include references to useful resources

## 📊 Progress Tracking

### Skill Assessment
- Track challenges solved by category
- Note difficulty progression over time
- Identify areas needing improvement

### Tool Proficiency
- Maintain list of tools mastered
- Note which tools work best for which scenarios
- Practice with new tools regularly

### Time Management
- Track time spent on different types of challenges
- Identify patterns in solution approaches
- Set reasonable time limits for attempts

---
*Methodology guide for systematic CTF challenge solving*