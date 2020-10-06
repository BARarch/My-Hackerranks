SELECT c.company_code, c.founder, 
(SELECT COUNT(DISTINCT lead_manager_code) FROM lead_manager WHERE company_code = c.company_code),
(SELECT COUNT(DISTINCT senior_manager_code) FROM senior_manager WHERE company_code = c.company_code),
(SELECT COUNT(DISTINCT manager_code) FROM manager WHERE company_code = c.company_code),
(SELECT COUNT(DISTINCT employee_code) FROM employee WHERE company_code = c.company_code)
FROM Company AS c ORDER BY c.company_code;