Password Complexity Checker & Compliant Password Generator
A lightweight, user‑friendly Python tool for evaluating password strength and generating compliant, high‑entropy passwords. Built with security best practices, this utility helps users create stronger passwords and see how their existing ones measure up.

✨ Features
  
Interactive menu system
Check passwords, generate new ones, or exit, all from a simple looped interface.
•  Password complexity checker
Validates passwords against:
•  Minimum length (12+ characters)
•  Uppercase letters
•  Lowercase letters
•  Digits
•  Special characters
•  Compliant password generator
Produces strong, enterprise‑friendly passwords:
•  Avoid ambiguous characters
•  Include at least one character from each required category
•  Use a safe, compatible punctuation set
•  Default to 14 characters (configurable)
•  Clear feedback
If a password fails any requirement, the tool explains why.
•  Looping mode
Users can check or generate multiple passwords without restarting the script.

📦 Installation
Clone the repository:

```
git clone https://github.com/HackingHusky/password-checker
cd python_checker.py
chmod +x python_checker.py
```
No external dependencies are required; everything uses Python’s standard library.

You’ll see a menu like:

🔍 Check a password
Enter option 1, then type any password you want to evaluate.
The tool will display:
•  Overall strength
•  Detailed feedback on missing requirements
🔧 Generate a compliant password
Enter option 2 to generate a secure, compliant password.
The tool will evaluate the generated password using the same rules.

🧠 How It Works
The script uses Python’s built‑in, and  modules to:
•  Validate password structure
•  Randomly generate secure passwords
•  Avoid problematic or ambiguous characters
•  Provide clear, actionable feedback
Everything is modular, so it is easy to extend with:
•  Entropy scoring
•  Logging
•  CLI flags
•  JSON output
•  Integration into larger security tools
