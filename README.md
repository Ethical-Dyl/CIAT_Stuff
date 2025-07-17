# py_fun

![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)

> **Fun Python Scripts Collection**  
> A playground of useful and playful Python scripts to automate tasks, learn new things, and experiment with APIs.

---

## 📂 Scripts Overview

| Script             | Description                                                                                     | API Key Required |
|--------------------|-------------------------------------------------------------------------------------------------|------------------|
| **CANVAS.py**      | Submit assignments to Canvas automatically via the Canvas API.                                  | ⚠️ **Yes**       |
| **Earth-Facts.py** | Print random Earth facts—no external keys or auth needed.                                       | ❌ **No**        |
| **bmi.py**         | Calculate BMI from inches/lbs to meters/kg, showcasing best practices with docstrings & functions.| ❌ **No**        |
| **sum_string.py**  | Sum digits in a string (ignores non-digits) and report invalid characters.                      | ❌ **No**        |
| **weather.py**     | Check local weather and receive clothing recommendations.                                       | ⚠️ **Yes**       |

---

## 🚀 Quick Start

1. **Clone this repository**  
   ```bash
   git clone https://github.com/YOUR-USERNAME/CIAT_Stuff.git
   cd CIAT_Stuff
   ```

2. **Create and activate a virtual environment (optional)**  
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API keys**  
   Create a `.env` file in the project root (or export directly in your shell):
   ```bash
   # For CANVAS.py
   CANVAS_API_KEY="your_canvas_api_key"
   CANVAS_API_URL="https://canvas.instructure.com"

   # For weather.py
   WEATHER_API_KEY="your_openweathermap_api_key"
   ```

4. **Run any script**  
   ```bash
   python Earth-Facts.py
   python bmi.py
   python sum_string.py
   python CANVAS.py --file path/to/your/assignment.pdf --course-id 12345
   python weather.py
   ```

---

## 🔧 Dependencies

- **Python 3.6+**  
- [requests](https://pypi.org/project/requests/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

Install all requirements with:
```bash
pip install -r requirements.txt
```

---

## 📖 Script Details

### CANVAS.py ⚠️  
**Submit assignments to Canvas LMS**  
Automate your homework uploads using your Canvas API key and endpoint.

### Earth-Facts.py  
**Random Earth Facts**  
Run with no setup—just enjoy a fun science tidbit each time.

### bmi.py  
**BMI Calculator**  
Convert inches & lbs → meters & kg. Demonstrates clean docstrings and function design.

### sum_string.py  
**Sum Digits in a String**  
Type any string of characters; it sums the digits and flags non-digit inputs.

### weather.py ⚠️  
**Local Weather + Clothing Tips**  
Fetch your local forecast and get outfit recommendations.

---

## 📝 Contributing

Pull requests welcome!  
1. Fork the repo  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/fooBar
   ```  
3. Commit your changes:  
   ```bash
   git commit -m 'Add new script'
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature/fooBar
   ```  
5. Open a Pull Request

Please follow PEP 8, include clear docstrings, and update this README if you add or modify scripts.

---

## 📧 Contact

Questions or feedback?  
- Open an [issue](https://github.com/YOUR-USERNAME/CIAT_Stuff/issues)

---

## ⭐ Show Your Support

If you find these scripts useful:  
- ⭐ Star the repo  
- ➕ Follow me on GitHub  
- 🔄 Share with your network  
- 🔗 Connect on [LinkedIn](https://www.linkedin.com/in/dylan-paynter)  

*Happy coding!*  
