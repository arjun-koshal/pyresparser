from nltk.corpus import stopwords

# Omkar Pathak
NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

# Education (Upper Case Mandatory)
EDUCATION = [
            'BE', 'B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E',
            'M.E.', 'MS', 'M.S', 'BTECH', 'MTECH',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII',
            'BACHELOR', 'MASTER', 'DOCTORATE', 'DOCTORAL',
            'BACHELORS', 'MASTERS', 'DOCTORATES', 'DOCTORALS',
            'Bachelor', 'Master', 'Doctorate', 'Doctoral',
            'Bachelors', 'Masters', 'Doctorates', 'Doctorals',
            'Bachelor’s', 'Master’s',
            'Bachelors of Science', 'Masters of Science', 'Doctorates of Science',
            'Bachelors of Arts', 'Masters of Arts', 'Doctorates of Arts',
            'Bachelors of Engineering', 'Masters of Engineering', 'Doctorates of Engineering',
            'Bachelors of Technology', 'Masters of Technology', 'Doctorates of Technology',
            'Bachelors of Business Administration', 'Masters of Business Administration', 'Doctorates of Business Administration'

        ]

NOT_ALPHA_NUMERIC = r'[^a-zA-Z\d]'

NUMBER = r'\d+'

# For finding date ranges
MONTHS_SHORT = r'''(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)
                   |(aug)|(sep)|(oct)|(nov)|(dec)'''
MONTHS_LONG = r'''(january)|(february)|(march)|(april)|(may)|(june)|(july)|
                   (august)|(september)|(october)|(november)|(december)'''
MONTH = r'(' + MONTHS_SHORT + r'|' + MONTHS_LONG + r')'
YEAR = r'(((20|19)(\d{2})))'

STOPWORDS = set(stopwords.words('english'))

RESUME_SECTIONS_PROFESSIONAL = [
                "Contact Information",
                "Objective",
                "Summary",
                "Education",
                "Experience",
                "Skills",
                "Projects",
                "Certifications",
                "Licenses",
                "Awards",
                "Honors",
                "Publications",
                "References",
                "Technical Skills",
                "Computer Skills",
                "Programming Languages",
                "Software Skills",
                "Soft Skills",
                "Language Skills",
                "Professional Skills",
                "Transferable Skills",
                "Work Experience",
                "Professional Experience",
                "Employment History",
                "Internship Experience",
                "Volunteer Experience",
                "Leadership Experience",
                "Research Experience",
                "Teaching Experience",
            ]

RESUME_SECTIONS_GRAD = [
                    'Accomplishments',
                    'Experience',
                    'Education',
                    'Interests',
                    'Projects',
                    'Professional experience',
                    'Publications',
                    'Skills',
                    'Certifications',
                    'Objective',
                    'Career objective',
                    'Summary',
                    'Leadership'
                ]
