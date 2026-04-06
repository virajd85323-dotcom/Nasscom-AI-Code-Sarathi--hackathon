# skills.md — UC-0B Policy Summarization
# Path: uc-0b/skills.md

skills:

  - name: load_policy_document
    description: Load policy text file into memory.
    input: >
      file_path (string) — path to .txt file
    output: >
      string — full policy document text
    error_handling: >
      If file missing or unreadable → raise error.
      If empty → return empty string.

  - name: summarize_policy
    description: Generate a faithful summary of the policy text.
    input: >
      policy_text (string)
    output: >
      summary (string)
    error_handling: >
      If input is empty → return empty summary.
      Must not generate content not present in input.

  - name: save_summary
    description: Save generated summary to file.
    input: >
      summary (string), output_path (string)
    output: >
      text file written to disk
    error_handling: >
      If write fails → raise file error.