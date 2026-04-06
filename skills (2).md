# skills.md — UC-0C Budget Analysis
# Path: uc-0c/skills.md

skills:

  - name: load_budget_data
    description: Load ward budget data from CSV.
    input: >
      file_path (string)
    output: >
      pandas.DataFrame
    error_handling: >
      Raise error if file missing or corrupted.

  - name: compute_growth
    description: Calculate percentage growth between two values.
    input: >
      previous_year (float), current_year (float)
    output: >
      growth_percentage (float or None)
    error_handling: >
      If previous_year is zero or null → return None.

  - name: apply_growth_calculation
    description: Apply growth computation across dataset.
    input: >
      dataframe
    output: >
      dataframe with growth column
    error_handling: >
      Skip invalid rows safely.

  - name: save_output
    description: Save processed data to CSV.
    input: >
      dataframe, output_path
    output: >
      CSV file
    error_handling: >
      Raise error if write fails.