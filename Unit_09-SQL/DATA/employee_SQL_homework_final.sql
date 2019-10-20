-- Donald Stegman    SMU Data Science -- Unit 09 Homework

-- DROP TABLE commands if needed
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;


-- Data Engineering
--Prior to exporting from QuickDBD, my table creation is in the working file. Queries ran properly
--but did not have key set up at that time.

-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "departments" (
    "dept_no" INT   NOT NULL,
    "dept_name" VARCHAR(25)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "dept_emp" (
    "dept_no" INT   NOT NULL,
 	-- Some employees are in multiple departments since it is not unique it cannot be a primary key
	"emp_no" INT   NOT NULL,
    "from_date" DATE()   NOT NULL,
    "to_date" DATE()   NOT NULL
);

CREATE TABLE "dept_man" (
    "dept_no" INT   NOT NULL,
    "emp_no" INT   NOT NULL,
    "from_date" DATE()   NOT NULL,
    "to_date" DATE()   NOT NULL
);

CREATE TABLE "employees" (
    "emp_no" INT   NOT NULL,
    "birth_date" DATE   NOT NULL,
    "first_name" VARCHAR(100)   NOT NULL,
    "last_name" VARCHAR(100)   NOT NULL,
    "gender" VARCHAR(10)   NOT NULL,
    "hire_date" DATE()   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "salaries" (
    "emp_no" INT()   NOT NULL,
    "salary" BIGINT()   NOT NULL,
    "from_date" DATE()   NOT NULL,
    "to_date" DATE()   NOT NULL
);

CREATE TABLE "titles" (
    "emp_no" INT   NOT NULL,
    "title" VARCHAR()   NOT NULL,
    "from_date" DATE()   NOT NULL,
    "to_date" DATE()   NOT NULL
);

--Altering to add key constraints

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_man" ADD CONSTRAINT "fk_dept_man_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_man" ADD CONSTRAINT "fk_dept_man_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");
-- END of export from QuickDBD: https://www.quickdatabasediagrams.com/

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