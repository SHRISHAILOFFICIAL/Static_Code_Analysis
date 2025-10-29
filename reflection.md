### reflection.md

#### 1. Which issues were the easiest to fix, and which were the hardest? Why?
- **Easiest fixes:** Formatting and style warnings, such as missing blank lines, unused imports, and trailing newlines. These were simple to correct since they only involved minor code formatting adjustments.  
- **Hardest fixes:** The warnings related to the `global` keyword and the `eval()` function were harder. These required refactoring the logic to remove unsafe practices while ensuring the program still worked as intended.

---

#### 2. Did the static analysis tools report any false positives? If so, describe one example.
- Most of the warnings were accurate, but the warning about the `global` variable (W0603) could be seen as a mild false positive. The variable was intentionally global to maintain the inventory state across functions. However, refactoring it still improved the code’s structure and clarity.

---

#### 3. How would you integrate static analysis tools into your actual software development workflow?
- I would integrate tools like **flake8**, **pylint**, and **bandit** into a **Continuous Integration (CI)** pipeline using GitHub Actions.  
- Each commit or pull request would automatically run these tools to catch issues early.  
- For local development, I would use **pre-commit hooks** or IDE extensions to automatically check for style and security issues before committing changes.

---

#### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- The final code became more **readable and consistent** due to proper naming conventions and spacing.  
- Removing `eval()` improved **security** and prevented code injection risks.  
- Using context managers (`with open()`) ensured better **resource management** and prevented file handling errors.  
- Overall, the fixes made the program cleaner, safer, and more maintainable.
