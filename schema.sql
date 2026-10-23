CREATE TABLE IF NOT EXISTS clinical_trials (
    subject_id INTEGER PRIMARY KEY,
    site_id INTEGER NOT NULL,
    age INTEGER,
    gender TEXT,
    enrollment_date TEXT,
    treatment_group TEXT,
    adverse_events INTEGER,
    dropout INTEGER CHECK (dropout IN (0, 1)),
    systolic_bp INTEGER,
    diastolic_bp INTEGER,
    cholesterol_level INTEGER
);