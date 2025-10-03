# hr_data.py

EMPLOYEES = {
    "EMP001": {
        "name": "Priya Sharma",
        "department": "Engineering",
        "leave_balance": 15,
        "sick_leave": 5,
        "joined_date": "2022-01-15"
    },
    "EMP002": {
        "name": "Rahul Verma",
        "department": "Marketing",
        "leave_balance": 20,
        "sick_leave": 8,
        "joined_date": "2021-06-01"
    },
    "EMP003": {
        "name": "Anjali Patel",
        "department": "HR",
        "leave_balance": 18,
        "sick_leave": 6,
        "joined_date": "2020-03-10"
    }
}

POLICIES = {
    "leave_policy": """
    Annual Leave Policy:
    - Employees get 20 days of annual leave per year.
    - Leave must be requested at least 2 weeks in advance.
    - Maximum consecutive leave: 15 days.
    - Unused leave carries over up to 5 days.
    """,
    "work_from_home": """
    Work From Home Policy:
    - Employees can work from home up to 3 days per week.
    - Must inform manager 1 day in advance.
    - Core hours: 10 AM - 4 PM must be available.
    """,
    "benefits": """
    Employee Benefits:
    - Health insurance (employee + family).
    - Annual performance bonus.
    - Professional development budget: ₹1,50,000/year.
    - Gym membership reimbursement.
    - Festival bonuses (Diwali, etc.).
    """
}
