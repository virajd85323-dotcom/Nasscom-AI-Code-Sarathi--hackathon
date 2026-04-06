# skills.md — UC-0A Complaint Classifier
# Path: UC-0A/skills.md

skills:

  - name: load_complaint_data
    description: Load complaint records from a CSV file into a structured dataframe.
    input: >
      file_path (string) — relative or absolute path to CSV file 
      (expected columns include at least: complaint)
    output: >
      pandas.DataFrame — dataframe containing all complaint records
    error_handling: >
      If file is missing, unreadable, or improperly formatted → raise a clear exception.
      If required column 'complaint' is missing → stop execution with error.

  - name: classify_complaint
    description: Assign exactly one valid category to a complaint based on its text content.
    input: >
      complaint_text (string) — raw complaint description
    output: >
      category (string) — one of the predefined labels: Billing, Service, Network, Other
    error_handling: >
      If input is null, empty, or not a string → return "Other".
      If classification is ambiguous or does not match known patterns → return "Other".

  - name: apply_classification
    description: Apply classification logic to all complaint records in the dataset.
    input: >
      dataframe (pandas.DataFrame) — must contain 'complaint' column
    output: >
      pandas.DataFrame — original dataframe with an additional 'category' column
    error_handling: >
      If 'complaint' column is missing → raise validation error.
      If dataframe is empty → return empty dataframe with 'category' column added.

  - name: save_output_data
    description: Save the classified dataframe to a CSV file for submission.
    input: >
      dataframe (pandas.DataFrame), output_path (string)
    output: >
      CSV file written to disk with classification results
    error_handling: >
      If write operation fails → raise file I/O error.
      Ensure output format remains consistent (no index column, correct headers).