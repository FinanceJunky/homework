-- Donald Stegman    SMU Data Science -- Unit 09 Homework

-- DROP TABLE commands if needed
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;


-- Data Engineering
CREATE TABLE departments(
dept_no VARCHAR(4),
dept_name VARCHAR(25)
);

CREATE TABLE dept_emp(
emp_no INT,
dept_no VARCHAR(4),
from_date DATE,
to_date DATE
);

CREATE TABLE dept_manager(
dept_no VARCHAR(4),
emp_no INT,
from_date DATE,
to_date DATE
);

CREATE TABLE employees(
emp_no INT,
birth_date DATE,
first_name VARCHAR(20),
last_name VARCHAR(20),
gender VARCHAR(1),
hire_date DATE
);

CREATE TABLE salaries(
emp_no INT,
salary INT,
from_date DATE,
to_date DATE
);

CREATE TABLE titles(
emp_no INT,
title VARCHAR(20),
from_date DATE,
to_date DATE	
);

-- Data Analysis Questions

-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT e.emp_no, e.last_name, e.first_name,
       e.gender, s.salary
FROM employees AS e, salaries AS s
WHERE s.emp_no = e.emp_no
ORDER BY s.salary DESC
LIMIT(10);

-- 2. List employees who were hired in 1986.

SELECT e.last_name, e.first_name, e.hire_date
FROM employees AS e
WHERE e.hire_date >= '1986-01-01' AND e.hire_date < '1987-01-01'
ORDER BY last_name;

-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

  -- Question says manager not managers - therefore, returning current managers, not past managers

SELECT d.dept_no, d.dept_name, d_man.emp_no, e.last_name, e.first_name, d_man.from_date, d_man.to_date
FROM departments AS d
JOIN dept_manager AS d_man ON (d.dept_no = d_man.dept_no)
JOIN employees AS e ON (d_man.emp_no = e.emp_no)
WHERE d_man.to_date = '9999-01-01';

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT d_emp.emp_no, e.last_name, e.first_name, d.dept_name
FROM departments AS d
JOIN dept_emp AS d_emp ON (d.dept_no = d_emp.dept_no)
JOIN employees AS e ON (d_emp.emp_no = e.emp_no)
WHERE d_emp.to_date = '9999-01-01'  -- only listing current employees and current positions
ORDER BY emp_no;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."

SELECT e.last_name, e.first_name
FROM employees AS e
WHERE (e.first_name = 'Hercules') AND (e.last_name LIKE 'B%')
ORDER BY e.last_name;

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT d_emp.emp_no, e.last_name, e.first_name, d.dept_name
FROM departments AS d
JOIN dept_emp AS d_emp ON (d.dept_no = d_emp.dept_no)
JOIN employees AS e ON (d_emp.emp_no = e.emp_no)
WHERE (d.dept_name = 'Sales') AND (d_emp.to_date = '9999-01-01')  -- only listing current employees and current positions
ORDER BY emp_no;

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT d_emp.emp_no, e.last_name, e.first_name, d.dept_name
FROM departments AS d
JOIN dept_emp AS d_emp ON (d.dept_no = d_emp.dept_no)
JOIN employees AS e ON (d_emp.emp_no = e.emp_no)
WHERE (d.dept_name = 'Sales') OR (d.dept_name = 'Development') AND (d_emp.to_date = '9999-01-01')  -- only listing current employees and current positions
ORDER BY emp_no;

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT last_name,
COUNT(*)
FROM employees
GROUP BY last_name
ORDER BY COUNT DESC
LIMIT (300);

-- Just a double check on last name Baba
SELECT *
FROM employees
WHERE (last_name = 'Baba')
ORDER BY emp_no;

BONUS?